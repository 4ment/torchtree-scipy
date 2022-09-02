install: FORCE
	pip install -e .[dev,test]

uninstall: FORCE
	pip uninstall torchtree-scipy

lint: FORCE
	flake8 --exit-zero torchtree_scipy test
	black --check .
	isort --check .

format: license FORCE
	black .
	isort .

test: FORCE
	pytest

clean: FORCE
	git clean -dfx -e torchtree_scipy.egg-info

FORCE: