FROM gitpod/workspace-full
USER root
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod +x *
RUN yarn install
RUN bash setup_pycalc.sh