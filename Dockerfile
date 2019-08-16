FROM gitpod/workspace-full
USER gitpod
ENV JAVA_HOME /home/gitpod/.sdkman/candidates/java/8.0.202-zulufx/bin/java
RUN export JAVA_HOME
EXPOSE 3000
EXPOSE 5000
USER root
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod +x *
USER root
RUN bash -c "apt install python3-dev"
RUN yarn install
RUN bash setup_pycalc.sh
USER root