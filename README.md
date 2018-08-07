# TL;DL
Run Travis-CI builds locally using Docker. Source: https://stackoverflow.com/questions/21053657/how-to-run-travis-ci-locally

# About
Run Travis-CI builds locally using Docker. It parses your local .travis.yml file, captures the commands required and execute them.
It bind-mounts the local directory to /home/travis/src inside the container, so no git clone is required.

Contributions are welcome!

### Important
This was written in 20 minutes over a lunch break because I was too lazy to do it properly. It makes several assumptions and I've only tested it for Python 3.6 builds.

# Install/Build
```
docker build -t travisbuild .
```

# Run Travis Locally
Go to your project directory.

Start the container:
```
CONTAINER_NAME=$(basename `pwd`)
docker run --rm -dit \
  --name $CONTAINER_NAME \
  --mount "source=$(pwd),destination=/home/travis/src,type=bind" \
  travisbuild \
  /sbin/init
```

Run the build:
```
docker exec -u travis \
  $CONTAINER_NAME \
  /home/travis/build.sh
```

# ToDo:
- Implement build for other languages, currently only Python 3.6 supported
- Implement parsing of environment variables from .travis.yml
- Better document
- Add Tests!
