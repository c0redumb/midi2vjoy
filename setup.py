#!/usr/bin/env python

from setuptools import setup

setup(name='midi2vjoy',
	version='0.1',
	description='Midi to vJoystick',
	author='c0redumb',
	packages=['midi2vjoy'],
	install_requires=[
		'pygame',
	],
	zip_safe=False,
	entry_points = {
		'console_scripts': [
			'midi2vjoy=midi2vjoy.midi2vjoy:main',
		],
	},
)
