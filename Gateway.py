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


import zmq
import argparse # for argument parsing

class Gateway():
  
  def __init__(self, args):
    self.name = args.name
    self.port = args.port

    # Set up a router socket to receive requests
    context = zmq.Context()
    self.poller = zmq.Poller ()
    self.router = context.socket (zmq.ROUTER)
    self.poller.register (self.router, zmq.POLLIN) 
    bind_string = "tcp://*:" + str(self.port)
    self.router.bind (bind_string)

    # Set up dealer requests to connect to microservices
    self.basic_svc_dealer = context.socket (zmq.DEALER)
    self.io_svc_dealer = context.socket (zmq.DEALER)
    self.cpu_svc_dealer = context.socket (zmq.DEALER)

    self.poller.register (self.basic_svc_dealer, zmq.POLLIN) 
    self.poller.register (self.io_svc_dealer, zmq.POLLIN) 
    self.poller.register (self.cpu_svc_dealer, zmq.POLLIN) 

    #self.basic_svc_dealer.connect("tcp://" + args.basic_svc_addr)
    #self.io_svc_dealer.connect("tcp://" + args.io_svc_addr)
    #self.cpu_svc_dealer.connect("tcp://" + args.cpu_svc_addr)

    
  def driver(self):
    print("Begin event loop")
    while True:
      events = dict (self.poller.poll (timeout=None))
      
      # Received a request from a client
      if self.router in events:
        self.handle_request()

      # If received something on any of the microservices dealers, then 
      # it is a response to a request we sent it earlier. Get the 
      # frames and send them back to whoever sent them
      elif self.basic_svc_dealer in events:
        framesRcvd = self.basic_svc_dealer.recv_multipart()
        self.router.send_multipart(framesRcvd)

      elif self.io_svc_dealer in events:
        framesRcvd = self.io_svc_dealer.recv_multipart()
        self.router.send_multipart(framesRcvd)

      elif self.cpu_svc_dealer in events:
        framesRcvd = self.cpu_svc_dealer.recv_multipart()
        self.router.send_multipart(framesRcvd)

      else:
        raise Exception ("Unknown event after poll")
        

  def handle_request(self):
    framesRcvd = self.router.recv_multipart()
    message = framesRcvd[-1]

    # Forward messages appropriately
    if message == b'basic':
      print("Recieved basic call")
      self.basic_svc_dealer.connect("tcp://" + args.basic_svc_addr)
      self.basic_svc_dealer.send_multipart(framesRcvd)
      self.basic_svc_dealer.disconnect("tcp://" + args.basic_svc_addr)
    elif message == b'cpu':
      print("Recieved cpu call")
      self.cpu_svc_dealer.connect("tcp://" + args.cpu_svc_addr)
      self.cpu_svc_dealer.send_multipart(framesRcvd)
      self.cpu_svc_dealer.disconnect("tcp://" + args.cpu_svc_addr)
    elif message == b'io':
      print("Recieved io call")
      self.io_svc_dealer.connect("tcp://" + args.io_svc_addr)
      self.io_svc_dealer.send_multipart(framesRcvd)
      self.io_svc_dealer.disconnect("tcp://" + args.io_svc_addr)


def parseCmdLineArgs ():
  # instantiate a ArgumentParser object
  parser = argparse.ArgumentParser (description="Service Application")
  
  parser.add_argument ("-n", "--name", default="gateway", help="Some name assigned to us. Keep it unique.")

  parser.add_argument ("-p", "--port", type=int, default=5555, help="Port on which we are rnning, default=5555")
  
  parser.add_argument ("-b", "--basic_svc_addr", default="localhost:5557", help="IP:port of basic microservice (echo)")
  parser.add_argument ("-i", "--io_svc_addr", default="localhost:5558", help="IP:port of IO microservice")
  parser.add_argument ("-c", "--cpu_svc_addr", default="localhost:5559", help="IP:port of CPU microservice")
  
  return parser.parse_args()



if __name__ == "__main__":
  args = parseCmdLineArgs ()

  # Create and configure Gateway object
  gateway_app = Gateway(args)

  # Run the gateway
  gateway_app.driver ()
