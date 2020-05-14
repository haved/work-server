FROM ubuntu:bionic
WORKDIR /app

# We get $PORT as env from heroku, no EXPOSE

#Is it a good idea to update and upgrade first?
RUN apt-get install texlive-full

RUN mkdir -p /app
COPY latexserver.py /app/
COPY README.md /app/

ENTRYPOINT ["python", "latexserver.py"]