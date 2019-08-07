#! /bin/bash


# Setup Ubuntu
apt update --yes
apt upgrade --yes

# Get Miniconda and make it the main Python interpreter
wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh
/bin/bash ~/miniconda.sh -b -p /opt/conda
rm ~/miniconda.sh
/opt/conda/bin/conda clean -tipsy
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
echo "conda activate base" >> ~/.bashrc
env USER='gitpod'
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini