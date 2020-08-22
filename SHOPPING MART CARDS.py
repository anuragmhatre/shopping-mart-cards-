from calculate import *
product_chances=0
replace_product=1
a=100000
b=10000
eggs=5
breads=30
grains=100

print("!!!!!! welcome to dmart !!!!!!!")
print("    what would you like to buy:  \n")

while product_chances <10:
    print('press 1 to buy sofa set?  \n')
    print('press 2 to buy electronics?  \n')
    print('press 3 to buy food items?  \n')
    print('press 4 to replace items? \n')
    option=int(input('what will you buy? :  '))
    if option==1:
        print("sofa prize = 10000")
        print(input("press Y to buy:\t"))
        product_chances += 1
        total=sub(a,b)
        print("10000rs is debited from your bank ."
              "balance = ",total)
        break
    elif option==2:
        print('Do you want to sell any  electonics : ')
        print(input('Y, N: '))
        sell=(int(input("for what prize is mobile : ")))
        to_get=add(a,sell)
        print(sell,"rs amount is credited to your bank ."
                   
              "balance is = ",to_get)
        break
    elif option==3:
        print("grains")
        print("breads")
        print("eggs")
        print(input("what you want: "))
        quantity=int(input("how much do you want: "))
        quantity=multi(quantity,eggs)
        print("total amount = ",quantity)
        bal=a-quantity
        print(quantity,"rs is debited from your bank .Balance = ",bal)
        break
    elif option==4:
        print(input("what you want to replace= "))
        print("OK WILL SOON REPLACED YOUR THINGS")
        break





