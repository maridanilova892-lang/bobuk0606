# put your python code here
print("Welcome! enter a secret code to access log in to your account")
password="Python1989"
попытки=3
счет=1
while True:
    a=input()
    if a!=password:
        попытки-=1
        if попытки>0:
            
            print("Wrong answer! You have", попытки ,"attempts left")
            счет+=1
        else:
            print("You've run out of attempts! try again in a few hours")
    if a==password:
        print("You have  logged into your account in", счет, "attempts")
        break


