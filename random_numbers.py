import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = False

    for random_number in my_randoms:
        if number == random_number:
            the_numbers_match = True

            break
    if the_numbers_match:
        print(f"{number} is in the random list")

    else:
        print(f"{number} is not in the random list")
