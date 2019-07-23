FROM gitpod/workspace-full
USER root
# Install custom tools, runtime, etc.
RUN apt-get update && apt-get install -y \
        screenfetch zsh \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

# Give back control
USER root