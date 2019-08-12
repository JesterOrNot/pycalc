FROM gitpod/workspace-full
USER gitpod
EXPOSE 3000
EXPOSE 5000
USER root
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod +x *
USER root
RUN yarn install
RUN bash setup_pycalc.sh
USER root