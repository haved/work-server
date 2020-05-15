## Work server
This is the repo for a docker image that exposes whatever features I may want to have a server do.
Currently its only task is compiling my latex when asked by netlify.

### Deploying
I use `manage.py`. To deploy to heroku with the CLI (assuming logged in):
```
./manage.py deploy
```

To deploy locally, do:
```
./manage.py docker_build
./manage.py docker_run
```

You may be able to just run the server on your host, try
```
./manage.py run
```
