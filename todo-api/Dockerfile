# Starts from an official Python base image
FROM python:3.11-slim

# Sets the working directory inside the container
WORKDIR /app

# Copy requirements
COPY app/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of app
COPY app/ .

# Tells Docker what command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
