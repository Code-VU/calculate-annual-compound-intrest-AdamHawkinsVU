def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
 x=0
 while x<3 :
    client_one_principal = float(input("Principle (amount): "))
    client_one_time = float(input("Time:               "))
    client_one_rate = float(input("Rate:               "))
    amount = client_one_principal*(pow((1+client_one_rate/100), client_one_time))
    comp_int = amount - client_one_principal
    readable_int = round(comp_int,2)
    print("Compound Interest:",readable_int)
    x=x+1
    if x<=2:
        print("---")
    

 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
