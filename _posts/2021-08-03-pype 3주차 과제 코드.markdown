---
layout: post
title:  "pype 3주차 과제 코드"
date:   2021-08-03 14:20:59 +0900
author: Namnani
categories: pype, python, boost-course
tags: pype, python, boost-course
---
---

# Q1. 구구단, 홀수번째 출력, 값이 50이하인 것만 출력.
```python
def checkInput(number) : #check validity
    while True:
        try :
            inumber = int(number)
            break
        except :
            print("Invaild input! Please check it (1~9)")
            number = input("Which order do you want to calculate the multiplication table? ")
            return checkInput(number)

    if inumber > 9 or inumber < 1:
        print("Invaild Input! Please check it (1~9)")
        number = input("Which order do you want to calculate the multiplication table? ")
        return checkInput(number)
    else:
        return inumber #return int

def calMult(number) :
    print("Order : "+str(number))
    a = 1 #increase order
    i = 1 #index for odd n
    result = number * 1 #initialization
    while result<=50 and a <= 9: #print the results below the 50
        print(f"{number}X{a}={result}") #print
        a = 2*i + 1 # odd number
        result = number * a
        i=i+1

#---main---
number = input("Which order do you want to calculate the multiplication table? ")
calMult(checkInput(number))
```

# Q2. 가위바위보 업그레이드 버전.(함수 버전, 게임을 몇판 진행할지 입력, 다르 입력 시 재입력, 게임종료 후 총 전적 출력)
```python
import random  # import to use random function

def checkInput():
    while True:
        print("------Please enter the input as 0(rock), 1(scissors), 2(paper)------")
        human = input("Rock Scissors Paper! : ")
        try:  # check that input can be convert to int type
            ihuman = int(human)
            if ihuman >= 3:
                print("Invalid Input!! Please check it")
                print("You should insert 0(rock), 1(scissors), 2(paper) only. Try again")
                continue
        except:  # if input can not be convert to int type, convert the input manually.
            if (human == "rock"):
                ihuman = 0
            elif (human == "scissors"):
                ihuman = 1
            elif (human == "paper"):
                ihuman = 2
            else:
                print("Invalid Input!! Please check it")
                print("You should insert 0(rock), 1(scissors), 2(paper) only. Try again")
                continue
        break
    return ihuman  # return the input that type of int


# play the game
def doGame(human):
    computer = random.randint(0, 2)
    if (human == computer):  # case : draw
        printStatus(human, computer)  # print the status
        print('Round',i,'result: Draw!')
        result = 'draw'
        return result
    # Calculate the levicivita since the game is based on the permutation
    # Rock(0) -> Scissors(1) -> Papaer(2) -> Rock(0) ->....
    levicivita = lambda i, j, k: (i - j) * (j - k) * (k - i) / 2
    other = [0, 1, 2]  # remain component of levicivita calcaulation
    other.remove(int(human))
    other.remove(int(computer))
    levi = levicivita(human, computer, other[0])

    if (levi == 1):  # case : win
        printStatus(human, computer)  # print the status
        print('Round',i,'result: You win!')
        result = 'win'
        return result

    elif (levi == -1):  # case : loose
        printStatus(human, computer)  # print the status
        print('Round',i,'result: You lose!')
        result = 'lose'
        return result


# print the status
def printStatus(human, com):
    a = 0  # for Indexing
    for tmpinput in [str(human), str(com)]:
        if (tmpinput == "0"):
            soutput = "rock"
        elif (tmpinput == "1"):
            soutput = "scissors"
        else:
            soutput = "paper"
        if (a == 0):
            print(f"You : {soutput}")
            a = a + 1  # for indexing
        else:
            print(f"Computer : {soutput}")


# -----------------------------------main--------------------------------------
print("------------------------ROCK SCISSORS PAPER ------------------------")

#input numbers for turns of game
while True:
    try:
        games = int(input("How many times do you want play?:"))
    except:
        print("Only numbers are allowed. Please try again.")
        continue
    break
if games == 0:
    print("Oh, you don't want to play game? Ok, bye")
    quit()
#execute the games
w=0
d=0
l=0
for i in range(1,games+1):
    print('-----Round',i, '!-----')
    score = doGame(checkInput())
    if score == 'draw':
        d = d + 1
    elif score == 'win':
        w = w + 1
    else:
        l = l + 1
# total score after game ends
print("-----------------------------Total score----------------------------")
print('My record:',w,'win',d,'draw',l,'lose')
print("Com's record:",l,'win',d,'draw',w,'lose')
```

# Q3. 2개의 숫자를 입력받아, 그 사이 짝수만 출력. (중앙값이 짝수가 아닐 시는 출력 X)
```python
print('짝수의 개수를 확인하고픈 범위를 알려주세요!')
n=int(input('확인하고 싶은 범위의 첫 번재 수 입력해주세요: '))
m=int(input('확인하고 싶은 범위의 마지막 수 입력해주세요: '))
b=0
numbers=[h for h in range(n,m+1)]
count = len(numbers)
if count % 2 == 0: # 짝수인 경우,
    mid = ( numbers[int(count/2-1)] + numbers[int(count/2)] ) / 2
else: # 홀수인 경우.
    mid = numbers[int(count/2)]
for h in numbers:
    if h%2==0:
        if h == mid:
            print('알려주신 범위 내에는',h,'라는 짝수이자 중앙값이 있네요')
        else:
            print('알려주신 범위 내에는',h,'라는 짝수가 있네요')
        b=b+1
print('Done!')
print('총',b,'개의 짝수가 있습니다')
```

# Q4. 2개의 숫자를 입력받아, 그 사이 소수가 몇개인지 출력하는 함수.
```python
def count_prime_number(n, m):
    prime_count = 0;

    # n보다 m이 크거나 같도록 switching.
    if n > m:
        temp = n
        n = m
        m = temp

    while n <= m:
        prime_case_variable = 0 # 밑에 while문을 돌고 나왔을 때, 이 값이 2라면, 소수인 것!
        currentValue = 1

        while currentValue <= n:
            if prime_case_variable == 2: # while문을 돌고 있는데, 이 값이 2라는 건, 이미 소수가 아니라는 것 임.
                break
            if n % currentValue == 0: # 나누어 진다는 소리임.
                prime_case_variable = prime_case_variable + 1

            currentValue = currentValue + 1 # 다음 반복문을 위한, variable setting.

        if currentValue > n: # break를 안타고, while문을 다 돌았으면(소수라면), currentValue 값이 n보다 무조건 크다.
            if prime_case_variable == 2: # while문을 돌고 나왔는데, 이 값이 2라면, 소수인 걸로 n을 소수로 count 해줘도 됨!
                prime_count = prime_count + 1

        n = n + 1 # 다음 반복문을 돌기 위한, variable setting.

    return prime_count

if __name__ == "__main__":
    while True:
        try:
            # 입력
            n = int(input("첫 번째 수 입력 : "))
            m = int(input("두 번째 수 입력 : "))
            break
        except:
            print("아마 int형이 아닌 값을 입력하셨을 겁니다.\n다시 입력해주세요.")

    count = count_prime_number(n, m)

    # 출력
    print("소수개수 :", count)

```
