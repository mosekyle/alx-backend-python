# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port your app runs on (default: 8000)
EXPOSE 8000

# Set the command to start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

