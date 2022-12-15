# How TO Draw In Atm Using For Python
# 1. Bank name
# 2.pin number
# 3.conditions
# deposite with drall ,balance enqurey,exit()


print("******* Wel Come to state bank of india********")
pin=4300
chances=3

total_amount=70000

while chances != 0:
    n1=int(input("enter your pin number:"))
    if n1 != pin:
        chances -=1
        print("wrong pin number")
        print(f"your chance is {chances} number of letf")

    else:
        print("you click 1: balance enqure,2:deposite,3:withdrall,4:exit")

        n2=int(input("Click your option:"))
        if n2==1:
            print(f"your balcence is {total_amount}")
        elif n2==2:
            dep=int(input("enter your amount:"))
            total_amount +=dep
            print(f"your deposite amount is RS.{dep}")
            print(f"your total balance is RS.{total_amount}")


        elif n2==3:
            withd=int(input("enter your amount:"))
            total_amount -=withd
            print(f"your withdrall amount is RS.{withd}")
            print(f"your total balance is RS.{total_amount}")

        elif n2==4:
            n3=input("click your option exit yes or no:")
            if n3=='yes':
                print("**********Thank for visiting*************")
                break

            else:
                continue


else:
    print("Sorry your attempts is over after 24hours back restart")                







