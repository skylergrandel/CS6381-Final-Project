# This is the server application. It serves as the baseline with which we
# will compare the microservice architecture implementation.
# It's role is to receive requests from the client at 3 endpoints.
# 1) Standard endpoint that just returns some constant value or maybe the current time or something
# 2) A CPU bound endpoint that takes an integer and computes that many digits of pi using the Leibniz algorithm
# 3) An IO bound endpoint that reads in a CSV file and then writes back out to it. This could be
# just like printing the first 10,000 lines integers to the CSV, but I'm not sure if python will optimize this
# if it isn't actually changing anything, so we might want to output random numbers or something because
# we don't want it to optimize, because the point is to waste time on IO.
# This MW should manage a ROUTER socket for consistency, which it binds to.

import zmq
import argparse # for argument parsing
from Functions import CPU, IO

class Service():
  
  def __init__(self):
    self.name = None
    self.ret_addr = None
    self.port = None
    self.poller = None
    self.rout = None
    self.deal = None
    
  def configure(self,args):
    self.name = args.name
    self.ret_addr = args.ret
    self.port = args.port
    
    context = zmq.Context()
    self.poller = zmq.Poller ()
    self.rout = context.socket (zmq.ROUTER)
    self.deal = context.socket (zmq.DEALER)
    
    # dealer will never receive anything, so there is no need to register it with the poller.
    self.poller.register (self.rout, zmq.POLLIN) 
    
    bind_string = "tcp://*:" + str(self.port)
    self.rout.bind (bind_string)
    
    connect_string = "tcp://" + self.ret_addr
    self.deal.connect(connect_string)
    
  def driver(self):
    print("Begin event loop")
    while True:
      events = dict (self.poller.poll (timeout=None))
      
      if self.rout in events:
        self.handle_event()

      else:
        raise Exception ("Unknown event after poll")
        
  def handle_event(self):
    message = self.rout.recv_multipart()[1]
    if message == b'basic':
      print("Recieved basic call")
      self.deal.send(message)
    elif message == b'cpu':
      print("Recieved cpu call")
      CPU()
      self.deal.send(message)
    elif message == b'io':
      print("Recieved io call")
      IO()
      self.deal.send(message)

def parseCmdLineArgs ():
  # instantiate a ArgumentParser object
  parser = argparse.ArgumentParser (description="Service Application")
  
  #parser.add_argument ("-a", "--addr", default="localhost", help="IP addr to advertise (default: localhost)")
  
  parser.add_argument ("-n", "--name", default="server", help="Some name assigned to us. Keep it unique.")

  parser.add_argument ("-p", "--port", type=int, default=5555, help="Port number, default=5555")
  
  parser.add_argument ("-r", "--ret", default="localhost:5556", help="Return addr/port combination. Default: localhost:5556")
  
  return parser.parse_args()

if __name__ == "__main__":
  args = parseCmdLineArgs ()
  service_app = Service()
  service_app.configure (args)
  service_app.driver ()
