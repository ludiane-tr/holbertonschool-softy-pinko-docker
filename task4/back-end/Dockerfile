# This Dockerfile is based on the latest ubuntu version
FROM ubuntu:latest

# Command to execute the image and the configuration
RUN apt-get update && apt-get upgrade -y

# Install Python3 and pip3
RUN apt-get install -y python3 python3-pip

RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Install Flask using pip3
RUN pip3 install flask
RUN pip3 install flask-cors

# The working directory
WORKDIR /app

# Copy the Python file into the image
COPY ./api.py /app/api.py

# Expose port 5252 for the Flask application
EXPOSE 5252

# Run the Flask application
CMD ["python3", "api.py"]
