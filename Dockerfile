FROM gitpod/workspace-full
USER gitpod
USER root
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN npm install readline-sync
RUN python3 setup.py install
