FROM python:3.7-buster
WORKDIR /code

RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc
RUN python -m pip install ipython

RUN pip install --upgrade pip

COPY . .

ENTRYPOINT ["tail", "-f", "/dev/null"]

