#!/bin/bash

# Run microservices
python3 Service.py -n basic_svc -p 5555 > basic_svc.out 2>&1 &
python3 Service.py -n io_svc -p 5556 > io_svc.out 2>&1 &
python3 Service.py -n cpu_svc -p 5557 > cpu_svc.out 2>&1 &

# Run gateway
python3 Gateway.py -n gateway -p 5558 -b localhost:5555 -i localhost:5556 -c localhost:5557 > gateway.out 2>&1 &

# Run clients
python3 Client.py -n client_basic -s localhost:5558 -t basic -e exp_svc3_client3 > client_basic.out 2>&1 &
python3 Client.py -n client_io -s localhost:5558 -t io -e exp_svc3_client3 > client_io.out 2>&1 &
python3 Client.py -n client_cpu -s localhost:5558 -t cpu -e exp_svc3_client3 > client_cpu.out 2>&1 &
