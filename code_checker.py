# put your python code here
print("Welcome! enter a secret code to access log in to your account")
password="Python1989"
attempts=3
count=1
while True:
    a=input()
    if a!=password:
        attempts-=1
        if attempts>0:
            
            print("Wrong answer! You have", attempts ,"attempts left")
            count+=1
        else:
            print("You've run out of attempts! try again in a few hours")
    if a==password:
        print("You have  logged into your account in", count, "attempts")
        break


