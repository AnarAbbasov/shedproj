# Use the official Python image from the Docker Hub
FROM python:3.10

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ unixodbc-dev curl gnupg lsb-release && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Collect static files


# Copy the rest of the application code
COPY . /code/
RUN python manage.py collectstatic --noinput
# Set environment variables
ENV DJANGO_SETTINGS_MODULE=shedproj.settings

# Run the Gunicorn server
CMD ["gunicorn", "shedproj.wsgi:application", "--bind", "0.0.0.0:8000"]
