# Use an official Python runtime as a base image
FROM python:3.9-slim

RUN addgroup -S nonroot \
&& adduser -S nonroot -G nonroot 

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app.py /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

USER nonroot

# Define the command to run the app
CMD ["python", "app.py"]