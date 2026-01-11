# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 7860

# Run the command to start the Uvicorn server, using the Procfile command
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]