from functools import reduce

file = open("day1.txt")
file_line = "placeholder"
first, second = [], []

while(True):
    file_line = file.readline().strip("\n").split("   ")
    if(file_line==[""]):
        break
    first.append(file_line[0])
    second.append(file_line[1])

first.sort()
second.sort()

result_1 = reduce(
     lambda acc, diff: acc + diff ,
     map(lambda pair: abs(int(pair[0])-int(pair[1])),zip(first, second)),
     0
    )

print(result_1)

result_2 = reduce(
    lambda acc, diff: acc + diff ,
    map(lambda pair: int(pair[0]) * second.count(pair[0]) , zip(first)),
    0
)

print(result_2)