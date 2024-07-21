# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project code into the container
COPY . /app/

# Expose the port your app runs on
EXPOSE 8000

# Run Gunicorn to serve your Django app
CMD ["gunicorn", "shedproj.wsgi:application", "--bind", "0.0.0.0:8000"]
