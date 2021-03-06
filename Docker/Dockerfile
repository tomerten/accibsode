
ARG PYTHON_VERSION=3.7.0-alpine3.8

FROM python:${PYTHON_VERSION} as builder

RUN apk add --update make \
    cmake \
    g++

RUN apk add \
    git \
    bash \
    build-base \
    linux-headers \
    bzip2 \
    bzip2-dev \
    sqlite-dev \
    zlib-dev \
    curl \
    libffi-dev \
    ncurses-dev \
    openssl-dev \
    readline-dev \
    tk-dev \
    xz-dev \
    zlib-dev


ENV HOME  /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN curl https://pyenv.run | bash
#see https://www.loganasherjones.com/2018/03/setting-up-your-python-environment/

RUN pyenv install 3.5.6
RUN pyenv install 3.6.8
RUN pyenv install 3.7.2
RUN pip install pytest tox
RUN pip install tox-globinterpreter

WORKDIR /usr/src/agogosml_cli

RUN echo "3.5.6" >> .python-version
RUN echo "3.6.8" >> .python-version
RUN echo "3.7.2" >> .python-version

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN make clean && \
    make lint && \
    make test && \
    make test-all && \
    make docs && \
    make dist

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/src/agogosml_cli/dist /dist

# G++ is a runtime dependency if you want to be able to use this docker container
RUN apk add --no-cache --update --virtual .build-deps make cmake && \
    apk add --no-cache --update --virtual .rt-deps g++ && \
    pip install --no-cache-dir /dist/agogosml_cli-*.tar.gz && \
    apk del .build-deps

WORKDIR /home

ENTRYPOINT ["agogosml"]
