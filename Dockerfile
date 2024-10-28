# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose the port Flask will run on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]