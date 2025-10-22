# Use a lightweight Python image
FROM python:3.12-alpine

# Disable output buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy files into the container
COPY . /app

# Run the script
CMD ["python", "joke.py"]
