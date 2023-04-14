# This is implementation for the various functions needed by the service.
# With the current implementation, both functions should take about 0.1s
import random
import time
import csv

# Precompute the output data for the IO op so that the time is all spent on IO, not on generating this data (which is a CPU bound op)
out = [[random.randint(100, 1000)] for i in range(100000)]

def CPU():
  # uncomment more numbers to make this run longer
  NUMBERS = [127, 15299, 87803, 219613, 318211, 506683, 919913]#, 1254739, 1471343, 1828669, 2364361, 3338989, 3509299, 4030889, 5054303, 5823667, 6478961, 6816631]
  
  # Sample `num_primes` numbers from the list of `nums_to_sample` numbers
  #sample = random.sample(NUMBERS, num_primes)
    
  # Check if each sampled number is prime and count the number of primes
  num_primes = 0
  for num in NUMBERS:
    is_prime = True
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
        break
  return
  
def IO(input_file_path = "test.csv"):
  # Read in all lines from the input CSV file
  with open(input_file_path, 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
  # Write `num_lines` random numbers to the input CSV file
  with open(input_file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(out)
  return
  
'''
#Testing
print("Start")
s = time.time()
IO()
e = time.time()
print("Done. Time was:", e-s)
'''

