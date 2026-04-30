import random


def game():
    print("you are playing game!!")
    score = random.randint(1,90)
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if hiscore != "" :
            hiscore = int(hiscore)
        else:
            hiscore == 0

    print(f"your score: {score}")
    if (score > hiscore):
       with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score
    


game()      

        
