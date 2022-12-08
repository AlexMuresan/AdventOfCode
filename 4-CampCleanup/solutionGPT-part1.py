def fully_contains(range1, range2):
  return range1[0] <= range2[0] and range1[1] >= range2[1]

def solve(input):
  # Parse the input into pairs of ranges
  pairs = [((int(x), int(y)), (int(a), int(b))) for x, y, a, b in [pair.split('-') for pair in input.split(',')]]

  # Keep track of the number of pairs in which one range fully contains the other
  count = 0
  for pair in pairs:
    range1, range2 = pair
    if fully_contains(range1, range2) or fully_contains(range2, range1):
      count += 1

  return count

# Read the input from the test.txt file
with open('test.txt') as file:
  input = file.read()

print(solve(input))