#!/bin/bash

# Run service
gnome-terminal -- bash -c "python3 Service.py -n svc -p 5555"

# Run clients
for i in 1 2 3 4 5 6 7 8 9 10 #11 12 13 14 15 16 17 18 19 20
do
	gnome-terminal -- bash -c "python3 Client.py -n client_io$i -s localhost:5555 -t io -e exp_svc1_client30"
	gnome-terminal -- bash -c "python3 Client.py -n client_cpu$i -s localhost:5555 -t cpu -e exp_svc1_client30"
	gnome-terminal -- bash -c "python3 Client.py -n client_basic$i -s localhost:5555 -t basic -e exp_svc1_client30"
done
