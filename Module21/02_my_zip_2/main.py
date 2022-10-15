def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))

def my_zip(first, second):
    answer = [(first[index], second[index]) for index in shortest_sequence_range(first, second)]
    return answer

a = [{'x': 4}, 'b', 'z', 'd']
b = (10, {20,}, [30], 'z')

check = my_zip(a, b)
print(check)