def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))


string = 'abcd'
tuple = (10, 20, 30)

fun_zip = ((string[i], tuple[i])
for i in shortest_sequence_range(string, tuple))

for item in fun_zip:
    print(item)

print(zip(string, tuple))
