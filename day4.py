# day 4
from typing import List
from collections import Counter

input_range = [[int(i) for i in str(d)] for d in range(347312, 805915)]

# six-digit number
# password value is within given range of inigers

# digit i+1 >= i for digit in password=
def non_decreasing(password: List[int]) -> bool:
    return all(i<=j for i, j in zip(password, password[1:]))

# two adjacent digits are the same (at least two can be more)
def has_pair(password: List[int]) -> bool:
    return not all(i!=j for i, j in zip(password, password[1:]))

# pair not in larger group
def has_right_pair(password):
    pairs = [(i,j) for i ,j in zip(password, password[1:]) if i == j]
    pair_count = Counter(pairs)
    if 1 in pair_count.values():
        return True
    return False

def password_format(password: List[int]) -> bool:

    return all((non_decreasing(password), has_right_pair(password)))
    
#part 1
# result = sum(password_format(password) for password in input_range)

#part 2
result = sum(password_format(password) for password in input_range)
print(result)