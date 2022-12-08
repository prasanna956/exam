
p=120
t=3
r=2.5
n=2
f=True
while(f==True):
    ch= int(input("Enter the Choice:"))
    if ch== 1:  
       asi=p*(1+ (r*t))
       print("\n Simple Interest = ",asi)
       f=False
    elif ch== 2:  
        aci=p*((1+ r/n) ** (n*t))
        print("\n Compound Interest = ",aci)
        f=False
    else:
        print("Incorrect")
        f=False
    
