import numpy as np

m, s = map(int, input().split())
n = int(input())

data = {}
for _ in range(n):
    line = list(map(int, input().split()))
    week, day, hour = line[:3]
    requests = line[3:]
    data[(week, day, hour)] = requests

q = int(input())
predictions = []
for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        week, day, hour = line[1:4]
        requests = line[4:]
        data[(week, day, hour)] = requests
    elif line[0] == 2:
        week, day, hour = line[1:4]
        # Predict the number of requests for each type
        prediction = [0] * m
        for key in data:
            if key[1] == day and key[2] == hour:
                for i in range(m):
                    prediction[i] += data[key][i]
        prediction = [x / 10 for x in prediction]
        predictions.append(prediction)

# Calculate the average number of requests of each type that need to be "cut"
cuts = [0] * m
for prediction in predictions:
    remaining_requests = prediction[:]
    remaining_couriers = s
    while remaining_couriers > 0 and sum(remaining_requests) > 0:
        for i in range(m):
            if remaining_requests[i] > 0:
                remaining_requests[i] -= 1
                remaining_couriers -= 1
                if remaining_couriers == 0:
                    break
    for i in range(m):
        cuts[i] += remaining_requests[i]
cuts = [abs(x / len(predictions)) for x in cuts]

# Print the result
print(' '.join(map(str, cuts)))