import random

# for n in range(20):
#     print(n)
#     if n == 4:
#         print('\033[93m exit')
#         break
# else:
#     print('END')
# for i in range(1, 10):
#     print('\n')
#     for k in range(1,10):
#         print(f"{i}*{k}={i*k}", end=' ')
print('\u2591'*40)
print('\u2591'*4,'Guess the number from 0 to 4',  ',\u2591 '*4)
print('\u2591'*40, end='\n'*2)
attempts = 4
rating = 0

for i in range(1, attempts + 1):
    print('Step:', i, end='')
    random_number = random.randint(1, 4)
    number = int(input(' Input number:'))

    if random_number == number:
       rating+= 1
       print('true')
    else:
       print('false')


