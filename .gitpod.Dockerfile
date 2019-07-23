FROM gitpod/workspace-full
USER root
USER root
# Install custom tools, runtime, etc.
RUN apt-get update && apt-get install -y \
        screenfetch \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

USER gitpod
# Apply user-specific settings

# Give back control
USER root