# Docker Commands Cheat Sheet

## Basic Docker Commands

1. **`docker --version`**
   - Displays the installed version of Docker.

2. **`docker pull <image>`**
   - Downloads a Docker image from a Docker registry (e.g., Docker Hub) to your local machine.
   - Example: `docker pull ubuntu`

3. **`docker images`**
   - Lists all the Docker images that are currently stored on your local machine.

4. **`docker rmi <image>`**
   - Removes a specified image from your local machine.
   - Example: `docker rmi ubuntu`

5. **`docker run <options> <image>`**
   - Creates and starts a new container from a specified image.
   - Example: `docker run -d ubuntu` (runs Ubuntu in detached mode).

6. **`docker ps`**
   - Lists all currently running containers.

7. **`docker ps -a`**
   - Lists all containers, including those that are stopped.

8. **`docker stop <container_id>`**
   - Stops a running container.
   - Example: `docker stop mycontainer`

9. **`docker start <container_id>`**
   - Starts a stopped container.
   - Example: `docker start mycontainer`

10. **`docker restart <container_id>`**
    - Restarts a running or stopped container.
    - Example: `docker restart mycontainer`

11. **`docker rm <container_id>`**
    - Removes a stopped container from your local machine.
    - Example: `docker rm mycontainer`

## Working with Volumes

12. **`docker volume create <volume_name>`**
    - Creates a new volume that can be shared among containers.
    - Example: `docker volume create myvolume`

13. **`docker volume ls`**
    - Lists all Docker volumes on your local machine.

14. **`docker volume rm <volume_name>`**
    - Removes a specified volume.
    - Example: `docker volume rm myvolume`

15.  **`docker volume inspect <volume_name>`**
    - Displays detailed information about a specified volume.
    - Example: `docker volume inspect myvolume`

16. **`docker run -v <volume_name>:/path/in/container <image>`**
    - Creates and starts a new container, mounting a specified volume.
    - Example: `docker run -d -v myvolume:/data ubuntu`

17. **`docker run -v <host_path>:/path/in/container <image>`**
    - Creates and starts a new container, mounting a host directory as a volume.
    - Example: `docker run -d -v ~/mydata:/data ubuntu`

18. **Sharing Volumes Between Containers**
    - You can share a volume between multiple containers by specifying the same volume name when starting them.
    - Example:

      ```bash
      docker run -d --name container1 -v myvolume:/data ubuntu
      docker run -d --name container2 -v myvolume:/data ubuntu
      ```

19. **`docker volume prune`**
    - Removes all unused volumes. Be careful, as this will delete any volumes not currently in use.
    - Example: `docker volume prune`

## Inspecting Containers and Images

20. **`docker inspect <container_id>`**
    - Displays detailed information about a specified container or image in JSON format.
    - Example: `docker inspect mycontainer`

21. **`docker logs <container_id>`**
    - Retrieves logs from a specified container.
    - Example: `docker logs mycontainer`

## Networking Commands

22. **`docker network ls`**
    - Lists all Docker networks available on your local machine.

23. **`docker network create <network_name>`**
    - Creates a new user-defined network.
    - Example: `docker network create mynetwork`

24. **`docker network rm <network_name>`**
    - Removes a specified network.
    - Example: `docker network rm mynetwork`

    Inspect a Network:

bash
Insert Code
Edit
Copy code
docker network inspect my_network
Connect a Container to a Network:

bash
Insert Code
Edit
Copy code
docker network connect my_network my_container
Disconnect a Container from a Network:

bash
Insert Code
Edit
Copy code
docker network disconnect my_network my_container
Remove a Network:

bash
Insert Code
Edit
Copy code
docker network rm my_network
Example of Using Docker Networks


## Advanced Commands

25. **`docker exec -it <container_id> <command>`**
    - Executes a command inside a running container, with interactive terminal access.
    - Example: `docker exec -it mycontainer bash` (opens a bash shell in the container).

26. **`docker-compose up`**
    - Starts up all the services defined in a `docker-compose.yml` file.

27. **`docker-compose down`**
    - Stops and removes all containers defined in a `docker-compose.yml` file.

    **`docker-compose logs`**
    - Displays the logs for all services.

    **`docker-compose exec:`** 
    - Executes a command in a running container.

    docker-compose ps

    The docker-compose ps command lists the containers defined in your Docker Compose configuration file (docker-compose.yml). It provides a summary of the current state of each service and its respective containers, including their names, status (running, exited, etc.), and any port mappings. This command is useful for managing and monitoring multi-container applications, as well as for troubleshooting issues with the containers.

    -q or --quiet: Only display container IDs.

bash
Insert Code
Edit
Copy code
docker-compose ps -q

--services: List only the services defined in the Compose file, without additional details.

bash
Insert Code
Edit
Copy code
docker-compose ps --services

--all: Show all containers, including those that are stopped.

bash
Insert Code
Edit
Copy code
docker-compose ps --all



    Docker Compose allows you to scale services easily.Mutiple containers will be created. For example, if you need multiple instances of a web service, you can use:
    **`docker-compose up --scale web=3`**
    - This command will create three instances of the web service.


## Cleanup Commands

28. **`docker system prune`**
    - Removes all stopped containers, unused networks, dangling images, and build cache.
    - Be careful, as this command can free up space but also remove data you might need.

29. **`docker rm $(docker ps -a -q)`**
    - Removes all stopped containers. The command inside the parentheses lists all container IDs.

30. **`docker rmi $(docker images -q)`**
    - Removes all images from your local machine. The command inside the parentheses lists all image IDs.

---

This cheat sheet covers a wide range of Docker functionalities, from basic image and container management to more advanced networking and volume handling.