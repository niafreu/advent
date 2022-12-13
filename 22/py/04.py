with open('../4.txt', 'r') as f:
  part1, part2 = 0, 0
  for line in f.readlines():
    pair = [int(x) for x in line.strip().replace('-', ',').split(',')]

    if ((pair[0] >= pair[2] and pair[1] <= pair[3]) or (pair[2] >= pair[0] and pair[3] <= pair[1])):
      part1 += 1

    overlaps = [x for x in range(pair[0], pair[1] + 1) if x in range(pair[2], pair[3] + 1)]
    overlaps2 = x for x in range(pair[2], pair[3] + 1) if x in range(pair[0], pair[1] + 1)]
    if(overlaps or overlaps2):
      part2 += 1

print(f'Part 1: {part1} pairs contained in each other')
print(f'Part 2: {part2} pairs overlap')
