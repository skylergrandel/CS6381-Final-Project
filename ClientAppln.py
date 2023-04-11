# This is the client application. It should be the same for both the 
# standard client-server architecture and the microservice architecture.
# It's role is to make requests to the server implementation we are using
# and time the results. We want to be able to make as many clients as we want
# so that we can measure the scalability of the system, and we want to be able
# to be able to change which endpoint we make requests to so that we can 
# measure latency of different types of services.
