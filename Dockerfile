FROM ubuntu:focal
WORKDIR /app

# We get $PORT as env from heroku, no EXPOSE

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y python3 tzdata texlive texlive-latex-recommended texlive-latex-extra texlive-science texlive-pictures \
    && ln -fs /usr/share/zoneinfo/Europe/Oslo /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && mkdir -p /app

COPY . /app/

ENTRYPOINT ["python3", "workserver.py"]