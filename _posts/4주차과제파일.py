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

## Q4.

# function: saving raw information from guest book
def raw_guest_book(guest_book):
    try:
        raw_file = open("guest_book.txt","a", encoding="UTF8")
    except:
        raw_file = open("guest_book.txt","w", encoding="UTF8")
    raw_file.write(guest_book+"\n")
    raw_file.close()
​
#main command
#input one by one until 'done'
while True:
    raw = input("Insert raw guest book's information by lines(Name,Phone no).\nWhen it is done insert 'done':")
    if raw == 'done' or raw == 'DONE':
        break
    else:
        raw_guest_book(raw)
​
# open task file
task_file = open("guest_book.txt","r",encoding="UTF8")
# show task file to user
contents=task_file.read()
print("\nBelow list is what you wrote on the file.")
print("-----Raw records of the guest book-----")
print(contents)
print("---------------------------------------")
​
# find wrong record
task_file = open("guest_book.txt","r",encoding="UTF8")
for line in task_file:
    pos = line.find(",") # find ',' position
    # seperate name and phone number
    name = line[:pos]
    phone = line[pos+1:].strip()
	# When the record matches with the conditions, skip to the next loop.
    if len(phone) == 13 and phone.find("-") != -1 and phone.startswith("010") == True:
        continue
	# If the record does not match with the conditions, print out the name of wrong recorder and the wrong phone number.
	else:
        print(f"Person who wrote wrong phone no.: {name}")
        print(f"The wrong phone no.: {phone}")
        print()

	
### Q4.py
```
def check_id(number) :
    if len(number) != 14 or number.find("-") == -1 or number[6:7]!="-": #validity check
        if (len(number) != 14 or number.find("-") == -1) : 
            print("Invaild input format! Please check the numbers (ex. 000000-0000000).")
        if ( number[6:7]!="-") : 
            print("Invaild input format! Please check the format (ex. 000000-0000000).")
        return runProcess()
    
    else :
        #Extract values
        year = str(number[:2])
        month = str(number[2:4])
        day = str(number[4:6])
        gender = str(number[7:8])
        s_gender = "None"

        flag=check_year(year,gender) #check year
        
        if flag != False :
            #Check validity
            if gender in ["1","3"] :
                s_gender = "Man"
            elif gender in ["2","4"] :
                s_gender = "Woman"
            else :
                print("Invaild input! Please check the gender number.")
                return runProcess()
            
            return year, month, day, s_gender
        else :
            exit()
            

def check_year(year,gender) :
    if(int(year) <=21 & int(year) >=0) :
        q = input("Were you born after 2000? Yes(o) No(x) : ")
        if q == "o" : #born in 2000 ~ 2021
            if gender not in ["3","4"] :
                print("Check the input! born year or gender number")
                return False
        elif q == "x" : #born in 1900 ~ 1921
            if gender not in ["1","2"] :
                print("Check the input! born year or gender number")
                return False
        else :
            print("Check the response! (o or x)")
            check_year(year,gender)
    else :
       if gender not in ["1","2"] :
                print("Check the input! born year or gender number")
                return False

def runProcess() :
    number = input("Enter your resident registration number : ")
    return check_id(number)
    
#---main---
year,month,day,gender = runProcess()
print(f"Bitrh : {year}.{month}.{day}, Gender : {gender}")
```
Q2.py
# 2021.08.10. Tuesday. 23:40.

# 시간관계상, 정답코드를 참고하였습니다만.. 머리가 굳어있는 제가 처음에 생각하기에는 어려운 논리네요 ㅠㅠ.
# 그래도 확실한건, 정답 예시 코드의 논리를 이해해두면, 도움은 될 것 같습니다!
# 제가, 만약 제대로 풀 시간이 있었다면,
# 저는, line.find해서, 문자열을 찾고, 해당 인덱스에서 길이 만큼까지의 문자열을 날리고,
# 같은 라인의 이후에서도, line.find의 결과로 -1 이 있는게 아닌지 하는 식으로 count를 단순 무식하게 했을 것 같은데요..
# 혹시 그렇게 풀면 이슈가 있을지, 생각나는게 있으면 말씀 부탁드립니다!


def count_word(text, word):
    # 문자열을 텍스트 파일로 저장
    text_save = open("text.txt", "w", encoding="UTF8")
    text_save.write(text)
    text_save.close()

    count = 0  # word를 세는 변수
    word_save = ""  # 문자의 길이만큼만 저장

    f_1 = open("text.txt")  # 텍스트 파일 읽어오기
    for line in f_1:  # 한 줄씩 불러오기
        if word in line:  # 우리가 찾는 문자가 현재 문장에 있다면
            for s in line:
                word_save = word_save + s  # 한 글자씩 word_save에 저장
                if word_save == word:  # word_save와 word를 비교해서 같으면
                    count += 1  # count +1
                if len(word_save) == len(word):  # 다음 문자 저장을 위해 1칸씩 앞으로 이동
                    word_save = word_save[1:]

    print("파일에 '" + word + "' 문자가 얼마나 있냐면은요!")
    print(str(count)+"개")  # word수 출력


if __name__ == '__main__':
    input_str = """
    울랄울랄라
    파이썬은, 신기하면서도, 이상한 언어 같아요아요.
    이번 학습을 통해,
    프로그래밍 입문자가, 파이썬으로 시작을 하는 이유에 대해서 충분히 납득이 되었고,
    프로그래밍 알고리즘 문제를 풀 때 확실히 유리한 문법들이 보이는 거 같네요.
    그렇지만, 아직도, 파이썬의 문법에서 배워야 할 게 많이 남아 있는 거 같아요.
    생각해보면, 자바는, 너무 코드가 주절주절 길어서, 가독성이 떨어진다 생각했었는데,
    파이썬은 오히려 너무 간결해서, 자바보다도 가독성이 더 떨어지는 거 같네요...
    아무튼, 새로운 언어를 배운다는 건 재밌는 것 같아요.
    열정있는 팀원분들과 함께해서 리프레쉬되고 자극도 많이 받네요!
    울랄울랄라울랄라
    """

    count_word(input_str, "울랄라")
