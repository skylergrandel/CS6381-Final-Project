#!/bin/bash

# Run service

for i in 1 2 3
do
	gnome-terminal -- bash -c "python3 Service.py -n svc -p $((i + 5550))"
done

x=30
# Run clients
for i in 1 3 5 7 9
do
	gnome-terminal -- bash -c "python3 Client.py -n client_io$i -s localhost:5551 -t io -e exp_svc2_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_cpu$i -s localhost:5551 -t cpu -e exp_svc2_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_basic$i -s localhost:5552 -t basic -e exp_svc2_client$x"
	
	gnome-terminal -- bash -c "python3 Client.py -n client_io$((i+1)) -s localhost:5552 -t io -e exp_svc2_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_cpu$((i+1)) -s localhost:5553 -t cpu -e exp_svc2_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_basic$((i+1)) -s localhost:5553 -t basic -e exp_svc2_client$x"
done
