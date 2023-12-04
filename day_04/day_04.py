import re
from collections import defaultdict

pat = re.compile(r"(\d+)")

d = defaultdict(int)
part1 = 0
part2 = 0
day = 1

for line in open(r"input.txt"):
    win, me = map(
        lambda x: set(pat.findall(x.strip())), line.split(":")[1].strip().split("|")
    )
    temp = 0
    for i in me:
        if i in win:
            temp += 1
    part1 += 2 ** (temp - 1) if temp else 0

    # for part 2
    d[day] += 1
    for i in range(day+1, day+temp+1):
        d[i] += 1 * d[day]
        # part2 += 1 * d[day]
    # part2 += 1
    day += 1

print(part1)
print(sum(d.values()))
