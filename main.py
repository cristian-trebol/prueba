print('Hola')
from tqdm import tqdm

my_list = [1, 2, 3]


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def divisiom(num1, num2):
    return num1 % num2

print(suma(1, 2))

for x in tqdm(range(10000000)):
    suma(x, x)
