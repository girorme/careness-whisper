# Use Python 3.8 as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script (this can be overridden with arguments)
ENTRYPOINT ["python", "main.py"]

# Default command (this can be overridden with arguments in 'docker run')
CMD ["--help"]
