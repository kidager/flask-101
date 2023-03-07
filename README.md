# Flask 101

This repo is just for testing Flask in Python.

There are some classes and tests that are not really related. You can the tests using `make test`

## Requirements

- Docker
- Docker compose
- Traefik already running on the `traefik-network` network

## Getting started

If you don't have Traefik running, follow the next steps:

- Create the `traefik-network` network

  ```shell
  docker network create 'traefik-network'
  ```

- Create a file named : `docker-compose.override.yaml`
- Put the following content into it

  ```yaml
  version: '3.9'

  services:
    traefik:
      image: traefik:latest
        restart: unless-stopped
        command:
          - --providers.docker
          - --providers.docker.exposedByDefault=false
          - --providers.docker.network=traefik-network
          - --entryPoints.web.address=:80
          - --entryPoints.websecure.address=:443
        ports:
          - "80:80"
          - "443:443"
        labels:
          # Traefik
          traefik.enable: true
          # Global Middlewares
          traefik.http.middlewares.whitelist-local-ips.ipwhitelist.sourcerange: 127.0.0.0/8, 172.0.0.0/8, 192.168.0.0/16
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
        networks:
          traefik-network:

  networks:
    traefik-network:
      external: true
      name: traefik-network
  ```

## Usage

### Flask

- Run `make up`
- Access `http://flask.dev.localhost` (or `https://flask.dev.localhost` if you have ssl configured)

### Tests

- Run `make test`
