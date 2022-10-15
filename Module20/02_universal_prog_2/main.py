def crypto(string, nums):
    return [sym for cou, sym in enumerate(string) if cou in simple_nums]

inp_string = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
simple_nums = [2, 3, 5,	7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73,	79,	83,	89,	97]

print(crypto(inp_string, simple_nums))
