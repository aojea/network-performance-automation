FROM ubuntu:18.04

ENV TREX_VER "v2.61"

RUN apt-get update && apt-get install -y \
       git \
       kmod \
       pciutils \
       python \
       python-pip \
       vim \
       wget \
       net-tools \
       iproute2 \
       && mkdir -p /opt/trex \
       && wget --no-cache https://trex-tgn.cisco.com/trex/release/$TREX_VER.tar.gz \
       && tar xzf $TREX_VER.tar.gz -C /opt/trex --strip-components=1 \
       && rm -f /$TREX_VER.tar.gz \
       && tar xzf /opt/trex/trex_client_$TREX_VER.tar.gz -C /usr/local/lib/python2.7/dist-packages/ \
       && rm -f /opt/trex/trex_client_$TREX_VER.tar.gz \
       && cp -a /opt/trex/automation/trex_control_plane/interactive/trex /usr/local/lib/python2.7/dist-packages/ \
       && rm -rf /opt/trex/automation/trex_control_plane/interactive/trex \
       && pip install -U pytest \
       && pip install -U pyyaml \
       && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV TREX_EXT_LIBS "/opt/trex/external_libs"
ENV PYTHONPATH "/usr/local/lib/python2.7/dist-packages/trex_client/interactive/"
WORKDIR /opt/trex

ENTRYPOINT ["/bin/bash"]
