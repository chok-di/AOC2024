import re

with open('./input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

def calculate_mul(match):
    x, y = map(int, match.groups())
    return x * y

mul_pattern = r"mul\((\d+),(\d+)\)"
res1 = sum(calculate_mul(match) for match in re.finditer(mul_pattern, content))

dont_do_pattern = r"don't\(\).*?do\(\)"
exclude_mul_sum = 0
dont_do_pairs = re.finditer(dont_do_pattern, content)

for dont_do_pair in dont_do_pairs:
    pair_content = dont_do_pair.group()
    exclude_mul_sum += sum(calculate_mul(match) for match in re.finditer(mul_pattern, pair_content))

res2 = res1 - exclude_mul_sum




