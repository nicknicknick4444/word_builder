import random

def choose_len():
    num=input("How many letters? (Up to 15): ")
    if num.isdigit():
        if int(num) < 2 or int(num)> 15:
            return choose_len()
        else:
            return int(num)
    else:
        return choose_len()

def who_goes():
    return random.choice(["you","comp"])

def your_go(go,total_len,listo):
    choicey=input("Choose a letter: ")
    if len(choicey) < 1 or len(choicey) > 1:
        return your_go(go,total_len,listo)
    if choicey.isalpha():
        go+=1
        prev=choicey
        listo.append(choicey)
        return go, prev
    else:
        return your_go(go,total_len,listo)
     
def comp_go(go,prev,alph,listo):
    choicey=""
    prev=""
    go+=1
    if go==1:
        choicey=random.choice(alph)
        prev=choicey
        listo.append(choicey)
    elif go>1 and prev=="s":
        choicey=random.choice(["h",random.choice(alph)])
        prev=choicey
        listo.append(choicey)
    elif go>1 and prev !="s":
        choicey=random.choice(alph)
        listo.append(choicey)
    prev=choicey
    return go, prev
        
def play(listo,prev,total_len,go,turn):
    alph=["a","b","c","d","e","f","g","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    vo=["a","e","i","o","u"]
    cons=[i for i in alph if i not in vo]
    if turn=="you":
        print("\nYour Turn:")
        go, prev = your_go(go,total_len,listo)
        turn="comp"
        return go,prev,turn
    if turn=="comp":
        go, prev = comp_go(go,prev,alph,listo)
        print("\nComputer's Turn:")
        turn="you"
        return go, prev,turn

def done(listo):
    return "".join(listo).title()

def go_again():
    again=input("\nGo again? (y/n): ")
    if again=="y":
        print("\nStarting new game...\n")
        return main()
    else:
        print("Bye!")

def main():
    listo=[]
    turn=who_goes()
    total_len=choose_len()
    go=0
    if go==0:
        prev=""
    while go<total_len:
        go, prev,turn=play(listo,prev,total_len,go,turn)
        print(listo)
    print("\nYour word is: {}".format(done(listo)))
    go_again()

if __name__ == "__main__":
    main()
