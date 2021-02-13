FROM gitpod/workspace-postgres

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

# Make sure we don't link against GPL code
ENV SLUGIFY_USES_TEXT_UNIDECODE yes
ENV LC_ALL en_US.utf8
ENV LANG en_US.utf8

RUN wget -qO- "https://repo.continuum.io/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh" -O /tmp/miniconda.sh && \
  chmod +x /tmp/miniconda.sh &&  sudo mkdir -p /usr/local &&  sudo /tmp/miniconda.sh -b -p /usr/local/miniconda

ENV PATH="/usr/local/miniconda/bin:${PATH}"
RUN sudo /usr/local/miniconda/bin/conda install -y conda-build conda-verify anaconda-client && sudo chown -R gitpod /usr/local
