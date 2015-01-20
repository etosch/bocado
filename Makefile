PHONY: test install clean

clean: 
	sudo rm -rf build
	sudo rm -rf /usr/local/lib/python2.7/site-packages/bocado

install: clean
	sudo python setup.py install

test: install
	python -m unittest tests.classes_test
	python -m unittest tests.value_sampler_test
