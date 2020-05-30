## Work server
I decided I didn't need a work server after all. Leaving this here in case I later want to deploy a python server in docker

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
