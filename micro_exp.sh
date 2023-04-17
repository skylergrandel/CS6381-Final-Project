#!/bin/bash

# Run microservices
gnome-terminal -- bash -c "python3 Service.py -n basic_svc -p 5555"
gnome-terminal -- bash -c "python3 Service.py -n io_svc -p 5556"
gnome-terminal -- bash -c "python3 Service.py -n cpu_svc -p 5557"

# Run gateway
gnome-terminal -- bash -c "python3 Gateway.py -n gateway -p 5558 -b localhost:5555 -i localhost:5556 -c localhost:5557"

# Run clients
for i in 1 2 3 4 5 6 7 8 9 10 #11 12 13 14 15 16 17 18 19 20
do
	gnome-terminal -- bash -c "python3 Client.py -n client_io$i -s localhost:5558 -t io -e exp_svc3_client30"
	gnome-terminal -- bash -c "python3 Client.py -n client_cpu$i -s localhost:5558 -t cpu -e exp_svc3_client30"
	gnome-terminal -- bash -c "python3 Client.py -n client_basic$i -s localhost:5558 -t basic -e exp_svc3_client30"
done
