# This is the API Gateway application. It should define the same endpoints as
# the server, but instead it just forwards those requests to the appropriate
# microservice. You should basically just be able to copy all of the server
# code, but get rid of all of the implementations and just forward the requests instead.
# The tough part of this one is that the gateway is responsible for managing the
# various microservices and the client(s), so it's acting like a discovery service as well.
# We *could* extend this to be able to handle any number of microservices (that is, replicas of
# the current microservices; it doesn't have to be so extensible that any microservice could be
# plugged in), but I'm not sure if it's worth the effort.
# This app should manage a ROUTER socket for communication with the client, which it binds to.
# It should also manage a DEALER socket (I think; I'm not exactly sure if this is necessary 
# since it's possible that the ROUTER could handle both) for communication with the microservices,
# which it connects to. This should not wait for a response from the microservice. Instead,
# the microservice will return the result back to the client directly.
