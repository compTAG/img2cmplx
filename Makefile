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
# DATA
################################################
data-init:
	mkdir data
	cd data \
		&& wget http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/matlab.zip \
		&& unzip matlab.zip \
		&& mv matlab emnist
	cd data \
		&& wget https://dabi.temple.edu/external/shape/MPEG7/MPEG7dataset.zip \
		&& unzip MPEG7dataset.zip \
		&& mv original mpeg7

data-clean:
	rm -rf data


################################################
# DEPLOYMENT
################################################
deploy:
	python setup.py sdist bdist_wheel
	twine upload --skip-existing dist/*


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


