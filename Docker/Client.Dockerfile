# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Client.py /app

# Define environment variables for IP address, port number, and message
ENV SERVER_ADDRESS=localhost:5555
ENV TYPE_OF_MESSAGE=Hello
ENV EXPERIMENT_NAME=Experiment
ENV NAME=Client

# Install any needed packages specified in requirements.txt (if applicable)
COPY requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define the entry point to run the script
ENTRYPOINT ["python", "Client.py", "--name", "${NAME}", "--server", "${SERVER_ADDRESS}", "--experiment_name", "${EXPERIMENT_NAME}", "--type_of_message", "${TYPE_OF_MESSAGE}"]