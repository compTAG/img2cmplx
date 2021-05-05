ENV_NAME=img2cmplx

default: test


################################################
# ENV
################################################
env-init:
	conda create --name $(ENV_NAME) pip

env-clean:
	conda remove --name $(ENV_NAME) --all

################################################
# TESTING
################################################
test:
	pytest

################################################
# CLEANUP
################################################
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
	rm -rf build/ dist/ *.egg-info


