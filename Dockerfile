FROM gitpod/workspace-full
USER gitpod
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod +x *
USER root
RUN yarn install
RUN bash setup_pycalc.sh
USER root