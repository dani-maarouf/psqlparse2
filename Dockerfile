FROM --platform=linux/amd64 python:3.8-slim-bookworm

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    gdb \
    valgrind \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

ENV PROTOC_VERSION=26.1

WORKDIR /tmp
RUN curl -sSLO https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip
RUN unzip protoc-${PROTOC_VERSION}-linux-x86_64.zip
RUN mv bin/protoc /usr/local/bin/protoc

RUN addgroup --system app && adduser app --system --ingroup app --home /home/app
WORKDIR /app
USER app

ENV PATH="/home/app/.local/bin:${PATH}"

RUN python -m pip install --user --upgrade pip setuptools wheel
COPY --chown=app:app . .
RUN python -m pip install --user -v '.[dev]'
ENV SHELL /bin/bash
CMD ["/bin/bash"]
