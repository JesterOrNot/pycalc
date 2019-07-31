FROM gitpod/workspace-full
USER root
RUN apt-get update && apt-get install -y \
    screenfetch zsh curl nano \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
RUN pip3 install --upgrade pip