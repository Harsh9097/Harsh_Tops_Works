print("Welcome To KALYAN JWELLERS ")

Name=input("Enter Your Name:")
Gender= input("Enter Gender:")
age=int(input("Enter Age:"))
product=input("Enter product:-")
Gram=int(input("Enter product Gram:-"))
Gold_price=int(input("Enter current gold price :"))

print("Name : ",Name)
print("Gender :",Gender )
print("Age :" ,age)
print("product : ",product)
print("Gram : " ,Gram )
print("Gold Price :" ,Gold_price)

total_rate= Gold_price * Gram
print("Total Gold Rate :",total_rate)

M_charges=int(input("Enter Making Charges :")) 
print("Making charges :" ,M_charges)


total_M_chage= total_rate + (M_charges * Gram)
print("Total Making Charges :",total_M_chage)

total_amt=total_rate + total_M_chage
print("Total Amount :",total_amt)

discount=""
if Gender=="male":
    if age>65:
        if total_amt>200000:
            print("Discount 20%")
            discount=int(total_amt)*20/100
        elif total_amt>300000:
            print("Discount 30%")
            discount=int(total_amt)*30/100
        elif total_amt>500000:
            print("Discount 35%")
            discount=int(total_amt)*35/100
        else:
            print("No discount")

    else: 
        if age<65:
            if total_amt>200000:
                print("Discout 10%")
                discount=(total_amt)*10/100
            elif total_amt>300000:
                print("Discount 20%")
                discount=(total_amt)*20/100
            elif total_amt>500000:
                print("Discount 25%")
                discount=(total_amt)*25/100
            else:
                print("No Discont")
                    
            
if Gender=="Female":
    if age>65:
        if total_amt>200000:
            print("Discount 25%")
            discount=(total_amt)*25/100

        elif total_amt>300000:
                print("Discount 35%")
                discount=(total_amt)*35/100

        elif total_amt>500000:
                print("Discount 40%")
                discount=(total_amt)*40/100
        else:
            print("No Discount")
    else:
        if age<65:
            if total_amt>200000:
                print("Discount 15%")
                discount=(total_amt)*15/100
            elif total_amt>300000:
             print("Discount 25%")        
             discount=(total_amt)*25/100
            elif total_amt>500000:
                print("Discount 30%")
                discount=(total_amt)*30/100
            else:
                print("No Discount")

dis_amount=(total_amt-total_M_chage)-discount
print("Discount Amount :",dis_amount)

net_amt=total_amt-dis_amount
print("Total Net Amount :",net_amt)




