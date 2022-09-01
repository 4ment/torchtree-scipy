install: FORCE
	pip install -e .[dev,test]

uninstall: FORCE
	pip uninstall project_name

lint: FORCE
	flake8 --exit-zero project_name test
	black --check .
	isort --check .

format: license FORCE
	black .
	isort .

test: FORCE
	pytest

clean: FORCE
	git clean -dfx -e project_name.egg-info

FORCE: