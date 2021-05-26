from art import logo
import random

print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
flag = 1 if input("Do you want to play type y for yes and n for no ")=='y' else 0

def selection():
    return random.choice(cards)

def finalcompare(user,comp):
    final_winner = {
        sum(comp) == 21 or sum(user)>21 or sum(comp)>16 and sum(comp) > sum(user) and sum(comp) <=21 :f"Congratulations to the computer Sorry for your loss Computer won ",
        sum(comp) > 21 or sum(comp)>16 and sum(comp) < sum(user) and sum(user) <=21 :f"Congratulations to user you won",
        11 in comp and sum(comp) > 21:'11',
        sum(comp) < 16 : 'add',
        sum(comp) > 17 and sum(comp) == sum(user):f'Match tied ',
    }
    return final_winner.get(True,'')

def compare(user):
    winner = {
        sum(user) == 21: 'Congratulations to user you won',
        sum(user) > 21 :f"Congratulations to the computer Sorry for your loss Computer won ",
        11 in user and sum(user) >21 : '11'
    }
    return winner.get(True,'')

while(flag==1):
    user = [selection(),selection()]
    computer = [selection(),selection()]
    print(f"Your cards are {user} and current score is {sum(user)} \n Computer first card is {computer[0]} ")

    while(input("Do you want to hit type 'y' if not type 'n' ") == 'y'):
        user.append(selection())
        print(f"Your cards are {user} and current score is {sum(user)} \n Computer first card is {computer[0]} ")
        result = compare(user)
        if '11'in result:
            user[user.index(11)] = 1
        elif 'Congratulations' in result:
            flag = 0
            print(f"Computer cards are {computer} \n {result}")
            break
    
    while(flag == 1):
        mainres = finalcompare(user,computer)
        if 'add' in mainres:
            computer.append(selection())
        elif 'Congratulations' in mainres:
            flag = 0
            print(f"Computer cards are {computer} \n {mainres}")
            break
        elif '11' in mainres:
            computer[computer.index(11)] = 1
print("Good bye See you later")     
