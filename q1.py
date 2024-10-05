import random

# start

num_list: list[int] = [i for i in range(95, 106)]
print(num_list)

even_num: list[int] = [i for i in range(10, 20 + 2, 2)]
print(even_num)

rand_tr_fa: list[int] = [random.randint(0, 1) for _ in range(5)]
print(rand_tr_fa)

rand_1_100: list[int] = [random.randint(1, 100) for _ in range(10)]
print(rand_1_100)

above_50: list[int] = [number for number in rand_1_100 if number > 50]
print(above_50)

# Bonus1:
# rand_1_100_2: list[int] = [random.randint(1,100) for _ in range(10) if _ > 50]
# print(rand_1_100_2)

# Bonus2:
# sentence: str = input('hello python masters')
# let_user: str = input('enter a letter:')
# trail: list[str] = [letter for letter in sentence if letter != ' ' and letter != let_user]
# print(trail)

list_10: list[int] = [random.randint(10, 99) for _ in range(10)]
print(list_10)
Ahadot: list[int] = [number for number in list_10 if number % 10 == 0]
print(list_10)

# stop
