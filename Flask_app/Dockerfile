# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]


# Stage 1: Build Stage
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --prefix=/requirements -r requirements.txt

# Stage 2: Production Stage
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /requirements /usr/local
COPY . .

# Expose port 5000
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]