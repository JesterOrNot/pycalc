#! /bin/bash
echo 'installing dependencies....'
bash setup_depend.sh
echo 'dependencies installed.'
echo 'installing python packages....'
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 setup.py install
echo 'installed python packages'
echo 'installing additional dependencies....'
bash setup_conda.sh
bash setup_sdkman.sh
bash setup_heroku.sh
echo 'setup completed'