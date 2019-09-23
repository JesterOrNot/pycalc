FROM gitpod/workspace-full-vnc
USER root
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN python3 setup.py install
