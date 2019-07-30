

# Requirements

ONLY IF RUN WITHOUT DOCKER:

The solution is designed to be installed on a unix station (Linux or MacOS).
The following software is suggested to be installed on the station:

- Anaconda (Python 3.6)

For example on a Debian station, one can install Anaconda with the following commands :

Install python:
```
  wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh
  chmod 755 ./Anaconda3-5.1.0-Linux-x86_64.sh
  # install folder : /home/kernix/anaconda3
  bash ./Anaconda3-5.1.0-Linux-x86_64.sh
```

The python package can then be readily installed

On an unix server you might need to do the following :

```
    sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo groupadd docker
    sudo gpasswd -a username docker
    sudo service docker restart 
```

# Dockerised full application

If you need to clean your docker files :

	# Delete all containers
	docker rm $(docker ps -a -q)
	# Delete all images
	docker rmi $(docker images -q)

Then you can (if needed) build the containers :

1. Clone the repo :

```
    git clone https://github.com/kernix/epex-spot-data.git
```

2. Go to the root directory of the project, replace IP to server IP (or docker machine) :

```
	cd ./epex-spot-data/pilot1/kbot
    sed -i.bak s/192.168.99.100/139.162.228.84/g ./src/js/front.js
    sed -i.bak s/192.168.99.100/139.162.228.84/g ./dist/js/main.min.js
```

3. Build the docker images with:

```
	docker build -t mkoutero/epex-api:latest -f docker/api/Dockerfile .
	docker build -t mkoutero/epex-webapp:latest -f docker/webapp/Dockerfile .
```


6. Start the docker containers : 

```
    docker-compose up -d
```

Or on a local machine : 

```
    docker-compose -f ./docker/docker-compose.yml up -d
```


