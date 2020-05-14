#!/usr/bin/bash
set -xe
heroku container:push web -a latex-compiler &&
heroku container:release web -a latex-compiler
