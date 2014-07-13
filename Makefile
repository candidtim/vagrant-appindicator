build: clean venv tests sdist

clean:
	cd src; rm -f *.pyc
	cd test; rm -f *.pyc
	rm -rf dist
	rm -f MANIFEST
	rm -rf coverage
	rm -f .coverage

venv:
	rm -rf ./.venv/
	virtualenv --system-site-packages .venv
	.venv/bin/pip install nose==1.3.3 coverage==3.7.1

vevn: venv

tests:
	export PYTHONPATH=src:test; export VAGRANT_HOME=/tmp/.vagrat.d; .venv/bin/nosetests --where=test

cover:
	export PYTHONPATH=src:test; export VAGRANT_HOME=/tmp/.vagrat.d; .venv/bin/nosetests --where=test --with-coverage --cover-branches --cover-package=src --cover-html --cover-html-dir=../coverage

run:
	export PYTHONPATH=src; python3 src/vagrantindicator.py

sdist: clean
	python setup.py sdist
