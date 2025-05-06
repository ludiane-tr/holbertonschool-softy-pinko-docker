# Use the latest Ubuntu base image
FROM ubuntu:latest

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and upgrade APT packages
RUN apt-get update && apt-get upgrade -y

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Workaround for 'externally managed' Python environments
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

# Install Flask using pip3
RUN pip3 install flask

# Install Flask cors
RUN pip3 install flask-cors

# Set the working directory to /app
WORKDIR /app

# Copy the Flask app into the container
COPY ./api.py /app/api.py

# Set the default command to run the Flask server
CMD ["python3", "api.py"]
