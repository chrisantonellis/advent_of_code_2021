from pathlib import Path

# read lines from input file
ROOT = Path(__file__).parent.resolve()
INPUT = Path(ROOT, "large")
with open(INPUT) as file_handle:
    file_contents = file_handle.read()
file_lines = file_contents.split("\n")

# determine depth increases
depth_increases = 0
measurements = [int(m) for m in file_lines[:-1]]
for i, measurement in enumerate(measurements):
    if i == 0:
        continue
    if int(measurements[i]) > int(measurements[i-1]):
        depth_increases += 1

print(depth_increases)
