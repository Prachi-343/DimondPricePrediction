FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update and install dependencies
RUN apt-get update -y && \
    apt-get install -y && \
    pip install -r requirements.txt

# Run the application
CMD ["python3", "app.py"]
