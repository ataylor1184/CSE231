quarters = 10
dimes = 10
nickels = 10
pennies = 10
price = 0
int_paid = 0


print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
price = float(price)*100
int_paid = float(int_paid) *100
while price!="q":
    price = float(price)
    
    if price < 0:
        print("Error: purchase price must be non-negative.")
    elif price > 0:
        int_paid = input("Input dollars paid (int): ")
        int_paid = int(int_paid) *100
      
        TotalChange = int_paid-price
        TotalPossibleChange = (quarters*25)+(dimes*10)+(nickels*5)+(pennies*1)
        while TotalChange < 0:
           print("Error: insufficient payment.")
           int_paid = input("Input dollars paid (int): ")
           int_paid = int(int_paid)*100
           TotalChange = int_paid-price
           
        if TotalChange == 0:
           print("No change.")
    
        elif TotalChange > 0:
            QChange =0
            DChange=0
            NChange=0
            PChange=0
            int_change_pennies=0
            if TotalChange < TotalPossibleChange:
                while quarters >= 1 and TotalChange // 25 > 0:
                    TotalChange = TotalChange-25
                    QChange +=1
                    quarters = quarters -1 
                    
                    
                while dimes >= 1 and TotalChange // 10 > 0:
                    TotalChange -=10
                    DChange +=1
                    dimes-=1
               
                while nickels >= 1 and TotalChange // 5 > 0:
                    TotalChange -=5
                    NChange +=1
                    nickels-=1
             
                while pennies >=1 and TotalChange // 1 > 0:
                    TotalChange -=1
                    PChange +=1
                    pennies -=1
                    if TotalChange % 1 >0:
                        PChange +=1
                        pennies -=1
          
                print('\nCollect change below: ')
                if (QChange) > 0:
                 print ('Quarters:', QChange)
                if (DChange) > 0: 
                 print('Dimes:', DChange)
                if (NChange) > 0 :
                 print('Nickels:',  NChange)
                if (PChange) > 0:
                 print('Pennies:', PChange)
            else:
                print("Error: ran out of coins.")
                break
            
    
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
 
    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    if str(price) =='q':
        break
    else  :
        price = float(price)*100
        price =int(price)
 
  





