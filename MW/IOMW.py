# This is the middleware for the IO bound appln.
# You can choose to implement this or just put everything in the appln.
# This MW should manage a ROUTER socket for communication with the gateway, which it binds to.
# Requests should not be returned to the caller but should instead be
# asynchronously routed back to the client.
