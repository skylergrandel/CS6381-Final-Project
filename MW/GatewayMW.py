# This is the gateway middleware.
# You can choose to implement this or just put everything in the appln.
# This MW should manage a ROUTER socket for communication with the client, which it binds to.
# It should also manage a DEALER socket (I think; I'm not exactly sure if this is necessary 
# since it's possible that the ROUTER could handle both) for communication with the microservices,
# which it connects to. This should not wait for a response from the microservice. Instead,
# the microservice will return the result back to the client directly.
