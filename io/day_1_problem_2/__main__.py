from pathlib import Path
from itertools import zip_longest

# read lines from input file
ROOT = Path(__file__).parent.resolve()
INPUT = Path(ROOT, "large")
with open(INPUT) as file_handle:
    file_contents = file_handle.read()
file_lines = file_contents.split("\n")

# cast to int and drop last value
measurements = [int(measurement) for measurement in file_lines[:-1]]

# calculate three-measurement sliding window
NO_VALUE = object()
calculated_measurements = []
measurements_offset = [([NO_VALUE for _ in range(i)] + measurements) for i in range(3)]
for measurements_window in zip_longest(*measurements_offset, fillvalue=NO_VALUE):
    if any((measurement is NO_VALUE for measurement in measurements_window)):
        continue

    calculated_measurements.append(sum(measurements_window))

# determine depth increases
depth_increases = 0
for i, measurement in enumerate(calculated_measurements):
    if i == 0:
        continue
    if int(calculated_measurements[i]) > int(calculated_measurements[i-1]):
        depth_increases += 1

print(depth_increases)
