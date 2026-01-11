# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Change working directory to the source folder
WORKDIR /app/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r ../requirements.txt

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Run the command to start the Uvicorn server from the src directory
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 7860"]