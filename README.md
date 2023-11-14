# torchtree-scipy 
[![Testing](https://github.com/4ment/torchtree-scipy/actions/workflows/python-package.yml/badge.svg)](https://github.com/4ment/torchtree-scipy/actions/workflows/python-package.yml)


## About torchtree-scypi
`torchtree-scipy` is a package that enhances the functionalities of [torchtree] by incorporating additional features from [SciPy].

## Dependencies
 - [SciPy]
 - [torchtree]

## Installation

### Installing from source
```bash
git clone https://github.com/4ment/torchtree-scipy
pip install torchtree-scipy/
```

### Installing latest stable version
You can install `torchtree-scipy` and its dependencies from PyPI with:
```
pip install torchtree-scipy
```

## Check install
If the installation was succesfull, this command should print the version of the `torchtree_scipy` library
```bash
python -c "import torchtree_scipy;print(torchtree_scipy.__version__)"
```

## Command line arguments
The `torchtree-scipy` plugin adds these arguments to the torchtree CLI:

```bash
torchtree-cli advi --help
  ...
  --scipy_gamma_site    use the GammaSiteModel implemented with scipy
```

## Features
### Discrete gamma site model
This model implements the discretized gamma distribution to model rate heterogeity accross sites. The gradient of this model with respect to the shape parameter is calculated numerically using finite differences.
The easiest way to use this model is to use the argument `--scipy_gamma_site`. This sets the type of the site model to `torchtree_scipy.GammaSiteModel` in the JSON configuration file. The default step size is `epsilon=1.0e-6` but it can be changed manually in the JSON file.

## License

Distributed under the GPLv3 License. See [LICENSE](LICENSE) for more information.

## Acknowledgements

torchtree-scipy makes use of the following libraries and tools, which are under their own respective licenses:

 - [PyTorch]
 - [SciPy]
 - [torchtree]

[PyTorch]: https://pytorch.org
[scipy]: https://github.com/scipy/scipy
[torchtree]: https://github.com/4ment/torchtree
