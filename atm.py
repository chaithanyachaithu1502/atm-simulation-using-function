balance=10000
def check_balance():
    print("avaliable balance is",balance)
def deposit():
    global balance
    amount=int(input())
    if amount>0:
        balance+=amount
        print("deposit successful")
    else:
        print("invalid")
def withdraw():
    global balance
    amount=int(input())
    if amount<=0:
        print("invalid balance")
    elif amount>balance:
        print("insufficient amount")
    else:
        balance-=amount
        print("withdraw successful")
while True:
    print("\n1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    a=int(input())
    if a==1:
        check_balance()
    elif a==2:
        deposit()
    elif a==3:
        withdraw()
    elif a==4:
        print("thank you!")
        break
    else:
        print(")





