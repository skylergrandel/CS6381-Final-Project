
# use python 3.10
FROM python:3.10.11-alpine3.17


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variables for the service application
ENV NAME=server
ENV PORT=5555

# Install any needed packages specified in requirements.txt (if applicable)
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Define the entry point to run the script
CMD python Service.py --name $NAME --port $PORT