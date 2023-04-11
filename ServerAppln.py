# This is the server application. It serves as the baseline with which we
# will compare the microservice architecture implementation.
# It's role is to receive requests from the client at 3 endpoints.
# 1) Standard endpoint that just returns some constant value or maybe the current time or something
# 2) A CPU bound endpoint that takes an integer and computes that many digits of pi using the Leibniz algorithm
# 3) An IO bound endpoint that reads in a CSV file and then writes back out to it. This could be
# just like printing the first 10,000 lines integers to the CSV, but I'm not sure if python will optimize this
# if it isn't actually changing anything, so we might want to output random numbers or something because
# we don't want it to optimize, because the point is to waste time on IO.
