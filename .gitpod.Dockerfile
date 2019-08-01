FROM gitpod/workspace-full
RUN chmod +x setup.sh
RUN bash setup.sh
RUN \
  apt-get update && \
  apt upgrade -y --force-yes && apt-get -y install \
    apt-utils \
    screenfetch \
    ant \
    zsh \
    curl \
    nano \
    vim \
    make \
    makefile \
    cmake
RUN pip3 install --upgrade pip