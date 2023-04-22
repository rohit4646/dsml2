import os 

print("Welcome to secret auction program")
bid_list=[]
condition= False

def bid_log(person,amount):
    bid_detail={}
    bid_detail['name']=person
    bid_detail['bid']=amount
    bid_list.append(bid_detail) 

def winner_check(listx):
    highest=0
    # bidder=''
    for items in listx:
        for x in items:
            current= items['bid']
            if current >= highest:
                highest= current
                bidder= items['name']
            
    print(f"The highest bid is {highest} by {bidder}")


while not condition:
    name= input("What is your name?: ")
    bid=int(input("Place your bid: "))
    bid_log(name,bid)
    next_log=input("More Entry? Type y or n: ")
    if next_log=='n':
        condition = True
    else:
        os.system('cls')

winner_check(bid_list)


