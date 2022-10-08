FROM python:latest

# Install packages
#RUN apt update && apt add \
    #git \
    #bash \
    #curl \
    #openssh \
    #python3 \
    #py3-pip \
    #py-cryptography \
    #wget \
    #curl

RUN mkdir -p /tmp/test && cd /tmp/test \
 && git clone https://github.com/salmanmak1/tsofenaws

CMD [ "python", "/tmp/test/tsofenaws/python/test/a.py" ]
