FROM gitpod/workspace-full
USER gitpod
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod +x *
USER root
RUN yarn install
RUN bash setup_pycalc.sh