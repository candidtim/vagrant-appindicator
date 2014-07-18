all: clean venv test sdist

clean:
	find vgapplet -type d -name __pycache__ | xargs rm -rf
	rm -rf coverage
	rm -f .coverage
	rm -rf dist
	rm -f MANIFEST
	rm -rf vagrantappindicator.egg-info/
	rm -rf /tmp/.vagrant.d/data/machine-index

venv:
	rm -rf ./.venv/
	virtualenv --python=python3 --system-site-packages .venv
	.venv/bin/pip install nose==1.3.3 coverage==3.7.1

test:
	export VAGRANT_HOME=/tmp/.vagrant.d; .venv/bin/nosetests

cover:
	export VAGRANT_HOME=/tmp/.vagrant.d; .venv/bin/nosetests --with-coverage --cover-branches --cover-package=vgapplet --cover-html --cover-html-dir=coverage

run:
	bin/vgapplet

sdist: clean
	python3 setup.py sdist
