# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Flask
RUN pip install Flask

# Run the static site generation script
CMD ["python", "app.py"]
