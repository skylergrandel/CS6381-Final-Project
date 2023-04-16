# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY Gateway.py /app

# Define environment variables for the gateway application
ENV NAME=gateway
ENV PORT=5555
ENV BASIC_SVC_ADDR=localhost:5557
ENV IO_SVC_ADDR=localhost:5558
ENV CPU_SVC_ADDR=localhost:5559

# Install any needed packages specified in requirements.txt (if applicable)
COPY requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define the entry point to run the script
ENTRYPOINT ["python", "Gateway.py", "--name", "${NAME}", "--port", "${PORT}", "--basic_svc_addr", "${BASIC_SVC_ADDR}", "--io_svc_addr", "${IO_SVC_ADDR}", "--cpu_svc_addr", "${CPU_SVC_ADDR}"]