FROM python:3.10.10-slim-bullseye
ENV packages="curl git make cmake build-essential libjpeg-dev libpng-dev libpng16-16"
RUN apt-get update && apt-get install -y --no-install-recommends $packages

RUN git clone --depth 1 https://github.com/davisking/dlib.git
RUN cd dlib && python3 setup.py install && cd ..

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock


RUN pip install poetry && poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir -r requirements.txt

COPY findFace.py findFace.py

RUN apt-get purge -y --auto-remove curl git make cmake build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN python findFace.py