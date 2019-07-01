import random
outcomes = ['rock','paper','scissors']

for n in range(20):
    print(random.choice(outcomes))

def game():
    print(random.choice(outcomes))
m=1
while m!=0:
    m = int(input())
    print("press 1 play game 0 to exit")
    if m==1:
        game()
    else:
        exit()