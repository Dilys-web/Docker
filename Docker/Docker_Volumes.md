# Docker Volumes

Volume is simply a directory inside our containers.
Firstly, we have to declare the directory as a volume and then share volume
Even if we stop container, still we can access volume.

Volume will be created in one container.
You can declare a directory as a volume only while creating container.
You cant create volume from existing container.
You can share one volume across any number of containers.
Volume will not be included when you update an image.

## You can map volume in two ways:
Container to Container
Host to Container: When you create a volume, you can link it to a specific directory on the host machine. This is what we call a host to container volume.

## Benefits of Volume
• Decoupling container from storage

• Share volume among different containers

• Attach volume to containers
On deleting container, volume does not delete

## Creating volume with commands
Create a container with volume
```bash
$ docker run -it --name container -v /volume2 ubuntu /bin/bash
```
Share volume with another container
```bash
$ docker run -it --name container2 --privileged=true —volumes-from containerl ubuntu /bin/bash

### Creating volume from Dockerfile
Create a Dockerfile and write

FROM ubuntu
VOLUME ["/myvolumel"]

#### Create image from this Dockerfile
```bash
$ docker built -t myimage .
```

Create a container from this image
```bash
$ docker run -it --name containerl myimage Ibin/bash
```

Share volume with Other container(Container to Container)
```bash
$ docker run -it --name container2 —privileged—true —volumefrom containerl ubuntu /bin/bash
```