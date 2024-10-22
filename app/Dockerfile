# Start by pulling the Python image
FROM python:3.13-alpine

# Switch working directory
WORKDIR /app

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

# Set the Python path
ENV PYTHONPATH=/app

# Configure the container to run with Gunicorn
ENTRYPOINT ["gunicorn"]

# Set the command to run your application
CMD ["--bind", "0.0.0.0:8000", "Journal:app"]