all: clean venv test sdist

clean:
	find vgapplet -type f -name *.pyc | xargs rm -rf
	find vgapplet -type d -name __pycache__ | xargs rm -rf
	rm -rf coverage
	rm -f .coverage
	rm -rf dist
	rm -f MANIFEST
	rm -rf vagrantappindicator.egg-info/
	rm -rf /tmp/.vagrant.d/data/machine-index

venv2:
	rm -rf ./.venv/
	virtualenv --python=python2.7 --system-site-packages .venv
	.venv/bin/pip install nose==1.3.3 coverage==3.7.1 mock==1.0.1

venv3:
	rm -rf ./.venv3/
	virtualenv --python=python3 --system-site-packages .venv3
	.venv3/bin/pip install nose==1.3.3 coverage==3.7.1 mock==1.0.1

venv: venv2 venv3

test2:
	export VAGRANT_HOME=/tmp/.vagrant.d; .venv/bin/nosetests

test3:
	export VAGRANT_HOME=/tmp/.vagrant.d; .venv3/bin/nosetests

test: test2 test3

cover:
	export VAGRANT_HOME=/tmp/.vagrant.d; .venv3/bin/nosetests --with-coverage --cover-branches --cover-package=vgapplet --cover-html --cover-html-dir=coverage

run:
	bin/vgapplet

sdist2: clean
	python2.7 setup.py sdist

sdist3: clean
	python3 setup.py sdist

sdist: sdist2 sdist3

install: sdist2
	pip install dist/vagrantappindicator-*.tar.gz

uninstall:
	pip uninstall vagrantappindicator
