# Use the latest version of Ubuntu as the base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Upgrade installed packages
RUN apt-get upgrade -y

# Install Python 3 and pip 3
RUN apt-get install -y python3 python3-pip

# Fix permission issue for pip installations
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

# Install Flask using pip3
RUN pip3 install flask

# Set the working directory in the container to /app
WORKDIR /app

# Copy the api.py file into the container at /app
COPY ./api.py /app/api.py

# Use JSON syntax for CMD to ensure proper signal handling
CMD ["python3", "api.py"]
