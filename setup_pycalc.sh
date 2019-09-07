#!/bin/bash
echo 'installing python packages....'
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 setup.py install
echo 'installed python packages'