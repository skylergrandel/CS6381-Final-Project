
FROM python:3.9-slim


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variables for the service application
ENV NAME=server
ENV PORT=5555

# Install any needed packages specified in requirements.txt (if applicable)
# COPY requirements.txt /app
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define the entry point to run the script
ENTRYPOINT ["python", "Service.py", "--name", "${NAME}", "--port", "${PORT}"]