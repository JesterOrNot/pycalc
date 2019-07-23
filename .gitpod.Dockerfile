FROM gitpod/workspace-full
USER root
RUN apt-get update && apt-get install -y \
        screenfetch zsh \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
USER gitpod
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN git pull
USER root