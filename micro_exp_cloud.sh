#!/bin/bash

x=30
# Run clients
for i in 1 2 3 4 5 6 7 8 9 10 #11 12 13 14 15 16 17 18 19 20
do
	gnome-terminal -- bash -c "python3 Client.py -n client_io$i -s 18.212.231.14:30000 -t io -e exp_svc3_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_cpu$i -s 18.212.231.14:30000 -t cpu -e exp_svc3_client$x"
	gnome-terminal -- bash -c "python3 Client.py -n client_basic$i -s 18.212.231.14:30000 -t basic -e exp_svc3_client$x"
done
