FROM ubuntu:focal
WORKDIR /app

# We get $PORT as env from heroku, no EXPOSE

ENV DEBIAN_FRONTEND=noninteractive

#Is it a good idea to update and upgrade first?
RUN apt-get update
#RUN apt-get upgrade -y
RUN apt-get install -y python3 tzdata texlive texlive-latex-recommended texlive-latex-extra texlive-science texlive-pictures

# tzdata texlive texlive-lang-european texlive-lang-english texlive-latex-recommended texlive-latex-extra texlive-generic-recommended texlive-fonts-recommended texlive-extra-utils texlive-font-utils texlive-science texlive-publishers texlive-pictures

RUN ln -fs /usr/share/zoneinfo/Europe/Oslo /etc/localtime \
&& dpkg-reconfigure --frontend noninteractive tzdata

RUN mkdir -p /app
COPY latexserver.py /app/
COPY README.md /app/

ENTRYPOINT ["python3", "latexserver.py"]