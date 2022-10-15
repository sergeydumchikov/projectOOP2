from random import randint
import random

# 1-й способ
orig_list = [randint(0, 100) for _ in range(10)]
sec_list = orig_list.copy()
fir_list = random.sample(orig_list, 5)
for i in fir_list:
    if i in sec_list:
        sec_list.pop(sec_list.index(i))
print(list(zip(fir_list, sec_list)))

# 2-й способ
print(list(zip([i for i in range(0, 11, 2)], [i for i in range(1, 11, 2)] )))



