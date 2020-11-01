FROM python:3.7-buster
WORKDIR /code
RUN mkdir /code/testdir
RUN mkdir /code/testdir/jpg_example

RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc
RUN python -m pip install ipython
RUN pip install --upgrade pip

COPY . .

RUN python example_maker.py

ENTRYPOINT ["tail", "-f", "/dev/null"]

