# -*- coding=utf8 -*-
from setuptools import setup

setup(
    name='segjb',
    version='1.0',
    description='A wrapper for jieba segmentation',
    long_description=open('README.rst').read(),
    author='Travis Chen',
    author_email='teckiechen@gmail.com',
    url='https://github.com/kn45/SegJb',
    license='MIT',
    classifiers=[
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    packages=['segjb'],
    package_data={'segjb': ['*.*']},
    keywords='nlp, tokenizing, segmentation',
    install_requires=[
        'jieba']
    )
