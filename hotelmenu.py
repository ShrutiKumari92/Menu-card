import menu_list
print("The delecious Restrurant ")
print("Menu card : ")

for key,value in menu_list.menu.items():
         print(f"{key.title()} Rs {value}")
total_prize=0
order=input("enter your order from the menu  : ").lower()
if order in menu_list.menu:
    total_prize+=menu_list.menu[order]
    print(f"your order {order} is added and you have to pay {total_prize}")
else:
    print("you entered wrong item please check menu ")
    

     
while True:
    anoter_item= input("do you want to try more order (Yes/No) : ").lower()
    if anoter_item=="yes" :
        for key,value in menu_list.menu.items():
         print(f"{key.title()} Rs {value}")
        
        

        order = input("enter your order from the menu again : ")
        if order in menu_list.menu:
         total_prize+=menu_list.menu[order]
         print(f"you ordered is successfull  and you have to pay {total_prize}")
        else:
            print("you entered wrong item ")
            
    elif anoter_item=="no":
        print(f"\nok, you have to final payment of your order is {total_prize}")
        print("Thank you for your orders\nvisit again🙏")
        break
    else:
        print("please enter Yes / No  :" )