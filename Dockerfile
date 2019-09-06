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
RUN python3 setup.py install