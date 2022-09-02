from typing import Optional

import torch
from scipy.stats import gamma
from torchtree.core.abstractparameter import AbstractParameter
from torchtree.core.utils import process_object
from torchtree.evolution.site_model import UnivariateDiscretizedSiteModel


class GammaSiteModel(UnivariateDiscretizedSiteModel):
    def __init__(
        self,
        id_: Optional[str],
        parameter: AbstractParameter,
        categories: int,
        epsilon: float = 1.0e-6,
        invariant: AbstractParameter = None,
        mu: AbstractParameter = None,
    ) -> None:
        self.epsilon = epsilon
        super().__init__(id_, parameter, categories, invariant, mu)

    @property
    def shape(self) -> torch.Tensor:
        return self._parameter.tensor

    def inverse_cdf(
        self, parameter: torch.Tensor, quantile: torch.Tensor, invariant: torch.Tensor
    ) -> torch.Tensor:
        if invariant is not None:
            rates = torch.cat(
                (
                    torch.zeros_like(invariant),
                    GammaQuantileFunction.apply(quantile, parameter, self.epsilon),
                )
            )
        else:
            rates = GammaQuantileFunction.apply(quantile, parameter, self.epsilon)
        return rates

    @classmethod
    def from_json(cls, data, dic):
        id_ = data['id']
        shape = process_object(data['shape'], dic)
        epsilon = data.get('epsilon', 1.0e-6)
        categories = data['categories']
        invariant = None
        if 'invariant' in data:
            invariant = process_object(data['invariant'], dic)
        if 'mu' in data:
            mu = process_object(data['mu'], dic)
        else:
            mu = None
        return cls(id_, shape, categories, epsilon, invariant, mu)


class GammaQuantileFunction(torch.autograd.Function):
    @staticmethod
    def forward(
        ctx, quantiles: torch.Tensor, shape: torch.Tensor, epsilon: float
    ) -> torch.Tensor:
        ctx.epsilon = epsilon
        ctx.shape = shape
        ctx.quantiles = quantiles.numpy()
        rates = gamma.ppf(quantiles.numpy(), shape.numpy(), scale=1.0 / shape.numpy())
        return torch.tensor(rates, dtype=shape.dtype, device=shape.device)

    def backward(ctx, grad_output: torch.Tensor) -> torch.Tensor:
        shape_plus = ctx.shape.numpy() + ctx.epsilon
        shape_minus = ctx.shape.numpy() - ctx.epsilon
        grad = torch.tensor(
            (
                gamma.ppf(ctx.quantiles, shape_plus, scale=1.0 / shape_plus)
                - gamma.ppf(ctx.quantiles, shape_minus, scale=1.0 / shape_minus)
            )
            / (2.0 * ctx.epsilon),
            dtype=ctx.shape.dtype,
            device=ctx.shape.device,
        )
        return (
            None,
            grad * grad_output,
            None,
        )
