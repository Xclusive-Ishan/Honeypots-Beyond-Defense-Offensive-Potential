# Use an official Python runtime as the base image
FROM python:3.11-slim

# Install system dependencies required for cryptography
RUN apt-get update && apt-get install -y libssl-dev libffi-dev build-essential

#install proxychains for docker enviroment 
RUN apt update && apt install -y proxychains

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

#copy config file for proxychain 

# Copy the application code into the container
COPY app.py .

# Expose port 443 for HTTPS
EXPOSE 9000

# Run the application
CMD ["python", "app.py"]