# [microservice-name]

[microservice-name] is a microservice oriented to the payment processing of the Elenas platform, focused on handling a large number of transactions

## Dependencies
To work with [microservice-name] it is necessary to have docker and Compose installed in versions that can work with the YAML compose configuration file in version Tree.

- [Docker compose file V3 reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
- [Docker Engine 23.10.3+](https://docs.docker.com/engine/installation/) - Installation guide in Linux
- [Compose 2.17.2+](https://docs.docker.com/compose/install/#/install-using-pip) - Installation guide in Linux

## Install development enviroment
* [Clone the repository](#clone-the-repository)
* [Start development](#start-development)
* [Build images](#build-images)
* [Build images whiout cache](#build-images-whiout-cache)
* [Debug in Visual Studio Code](#debug-in-visual-studio-code)
* [Debug in Visual Studio Code and build images whiout cache](#debug-in-visual-studio-code-and-build-images-whiout-cache)
* [Create network](#create-network)
* [Load SQL](#load-sql)
* [Stop development](#stop-development)
* [Debugging](#debugging)

### Clone the repository
```
$ git clone git@gitlab.com:elenasMujeresPoderosas/[microservice-name].git
$ cd [microservice-name]
```
[Back to Install development enviroment](#install-development-enviroment)

### Start development
```
$ make start-development
```

[Back to Install development enviroment](#install-development-enviroment)

### Build images 
```
$ make start-development BUILD_IMAGE=true
```
[Back to Install development enviroment](#install-development-enviroment)

### Build images whiout cache
```
$ make start-development BUILD_IMAGE=true BUILD_OPTIONS=--no-cache
```
[Back to Install development enviroment](#install-development-enviroment)

### Debug in Visual Studio Code
```
$ make start-development DEBUG=true
```
[Back to Install development enviroment](#install-development-enviroment)

### Debug in Visual Studio Code and build images whiout cache
```
$ make start-development DEBUG=true BUILD_IMAGE=true BUILD_OPTIONS=--no-cache
```
[Back to Install development enviroment](#install-development-enviroment)

### Create network
```
$ make create-network
```
[Back to Install development enviroment](#install-development-enviroment)

### Stop development
```
$ make stop-development
```

[Back to Install development enviroment](#install-development-enviroment)

### Help
```
$ make help
```

[Back to Install development enviroment](#install-development-enviroment)


### Debugging

#### Visual Studio Code
[./docker/docs/VisualStudioCode.md](./docker/docs/VisualStudioCode.md)

#### Pycharm professional edition
[./docker/docs/Pycharm.md](./docker/docs/PycharmProfessionalEdition.md)
