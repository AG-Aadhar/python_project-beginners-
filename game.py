# Game name is "The Perfect Guess"
import random

class Game:
    com = random.randint(1,100)
    # print(com)
    u = int(input("Guess the number: "))

    def __str__(self):

        if self.u > self.com:
            print("Enter little smaller number")
        elif self.u < self.com:
            print("Enter little larger number")

        if self.u>self.com or self.u<self.com:
            times = 1
            while self.u>self.com or self.u<self.com:
                user = int(input("Guess it again: "))

                if user > self.com:
                    print("Enter little smaller number")

                elif user < self.com:
                    print("Enter little larger number")

                elif self.u or user == self.com:
                    with open("highScore.txt","r") as f:
                        score = f.read()
                    if times+1<int(score):
                        with open("highScore.txt","w") as f:
                            update = f.write(str(times+1))
                    return f"finally you guess that in {times+1} chances"
                times+=1
        
        else:
            with open("highScore.txt","w") as f:
                update = f.write("1")
            return "You guess that in 1st chance"

g = Game() 
print(g)