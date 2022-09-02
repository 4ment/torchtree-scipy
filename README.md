# torchtree-scipy 
[![Python package](https://github.com/4ment/torchtree-scipy/actions/workflows/python-package.yml/badge.svg)](https://github.com/4ment/torchtree-scipy/actions/workflows/python-package.yml)

torchtree-scipy is a package providing extra functionalities from [scipy] for [torchtree]

## Dependencies
 - [torchtree]
 - [scipy]
## Installation

### Get the source code
```bash
git clone https://github.com/4ment/torchtree-scipy
cd torchtree-scipy
```

### Install using pip
```bash
pip install .
```

## Check install

```bash
torchtree --help
```

```bash
python -c "import torchtree_scipy"
```

## Features
### Discrete gamma site model
This class implements a discretized gamma distribution to model rate heterogeity accross sites. The gradient of this model with respect to the shape parameter is calculated numerically using finite differences.
The easiest way to use this model is to generate a json configuration file with a Weibull site model with the appropriate number of rate categories and then replace `WeibullSiteModel` with `torchtree_scipy.evolution.site_model.GammaSiteModel`:

```bash
torchtree-cli advi -i data.fa -t data.tree -C 4 > data.json
sed -i 's/WeibullSiteModel/torchtree_scipy.evolution.site_model.GammaSiteModel/' data.json
torchtree data.json
```

or in one line:
```bash
torchtree-cli advi -i data.fa -t data.tree -C 4 | sed 's/WeibullSiteModel/torchtree_scipy.evolution.site_model.GammaSiteModel/' | torchtree -
```

[torchtree]: https://github.com/4ment/torchtree
[scipy]: https://github.com/scipy/scipy