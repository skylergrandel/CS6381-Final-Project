# This is the client application. It should be the same for both the 
# standard client-server architecture and the microservice architecture.
# It's role is to make requests to the server implementation we are using
# and time the results. We want to be able to make as many clients as we want
# so that we can measure the scalability of the system, and we want to be able
# to be able to change which endpoint we make requests to so that we can 
# measure latency of different types of services.
# This app should manage a DEALER socket which it connects to.

import zmq
import argparse # for argument parsing
import time

class Client():
  
  # Initialize and configure the object
  def __init__(self, args):
    self.name = args.name
    self.type_of_message = args.type_of_message
    self.experiment_name = args.experiment_name

    # we only need a dealer to send requests and receive responses to them
    context = zmq.Context()
    self.dealer = context.socket (zmq.DEALER)
    self.poller = zmq.Poller ()
    self.poller.register (self.dealer, zmq.POLLIN) 
    connect_string = "tcp://" + args.server
    self.deal.connect(connect_string)
    
  
    
  def driver(self):
    print("Send the request")
    message_to_send = [bytes(args.type_of_message)]
    self.dealer.send_multipart(message_to_send)

    # Record the timestamp when the request was sent
    timestamp_sent = time.time()

    print("Begin event loop to check for the response")
    while True:
      events = dict (self.poller.poll (timeout=None))
      
      if self.dealer in events:
        response_frames = self.dealer.recv_multipart()
        timestamp_received_response = time.time()

        latency = timestamp_received_response - timestamp_sent
        self.handle_latency_data(latency)

        # No tasks left, so we terminate the program
        break

      else:
        raise Exception ("Unknown event after poll")
      

  def handle_latency_data(self, latency):
    # TODO saving the data to a file or into a database
    print(f"Results for experiment \'{self.experiment_name}\': {self.type_of_message} {latency}")
    


def parseCmdLineArgs ():
  # instantiate a ArgumentParser object
  parser = argparse.ArgumentParser (description="Client Application")
  
  parser.add_argument ("-n", "--name", default="client", help="Name of the client application")
  
  parser.add_argument ("-s", "--server", default="localhost:5555", help="Server to send requests to (addr/port pair). Default: localhost:5555")

  parser.add_argument ("-t", "--type_of_message", default="basic", help="Type of message to send")
  
  parser.add_argument ("-e", "--experiment_name", default="experiment", help="Name of the experiment we are running")

  return parser.parse_args()

if __name__ == "__main__":
  args = parseCmdLineArgs ()

  # Instantiate and configure a client
  client_app = Client(args)

  # Run the client
  client_app.driver ()

  print("Termination of the program")
