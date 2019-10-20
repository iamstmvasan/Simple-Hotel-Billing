print("---------------------------------------------")
print("\t\tHotel Sastra Menu")
print("---------------------------------------------")
print("\t\t1-->Idly[5rs]\n\t\t2-->Dosa[30rs]\n\t\t3-->Poori[20]\n\t\t4-->Upma[25]\n\t\t5-->Vada[10]")
amount = 0
def calc(order,quantity):
    global amount
    if order==1:
        amount+= 5*quantity
    elif order==2:
        amount+= 30*quantity
    elif order==3:
        amount+= 20*quantity
    elif order==4:
        amount+= 25*quantity
    else:
        amount+= 10*quantity
    return amount
sno=1
idly=0
dosa=0
poori=0
upma=0
vada=0
l=[]
l1=[]
l2=[]
while(True):
    print("Enter your order no : ")
    order = int(input())    
    print("Quantity : ")
    quantity = int(input())
    if order==1:
        if "Idly" not in l:
            l.append("Idly")
            l1.append(5)
        idly+=quantity
       # l2.append(idly)
    elif order==2:
        if "Dosa" not in l:
            l.append("Dosa")
            l1.append(30)
        dosa+=quantity
       # l2.append(dosa)
    elif order==3:
        if "Poori" not in l:
            l.append("Poori")
            l1.append(20)
        poori+=quantity
        #l2.append(poori)
    elif order==4:
        if "Upma" not in l:
            l.append("Upma")
            l1.append(25)
        upma+=quantity
        #l2.append(pongal)
       
    elif order==5:
        if "Vada" not in l:
            l.append("Vada")
            l1.append(10)
        vada+=quantity
        
    if order>0 and order<6:
        price = calc(order,quantity)
    else:
        print("Invalid order id")
    print("Total amount : ",price)
    print("Would you like to order again[Enter to --> continue & type (end) to --> terminate]")
    ch = input()
    if ch=="end":
        break
l2=[]
for i in l:
    if i=="Idly":
        l2.append(idly)
    elif i=="Dosa":
        l2.append(dosa)
    elif i=="Poori":
        l2.append(poori)
    elif i=="Upma":
        l2.append(upma)
    elif i=="Vada":
        l2.append(vada)
print("==========================================================")
print("\t\t\tHotel Sastra")
print("==========================================================")
print("\tSno\tItem\tPrice\tQuan\tAmount")
print()
for i in range(len(l)):
    print("\t",i+1,"\t",l[i],"\t",l1[i],"\t",l2[i],"\t",l2[i]*l1[i])
print("----------------------------------------------------------")
print("\t\t\t\tPrice = ",price)
gst=price*10/100
tot=price+gst
print("\t\t\t\tGST   = ",gst)
print("----------------------------------------------------------")
print("\t\t\t\tTotal = ",tot)
print("==========================================================")
print()
print("\t\t\tThanking you")
print()
print("==========================================================")
input()
