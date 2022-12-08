
p=120
t=3
r=2.5
n=2
f=1
while(f==1):
    #ch= int(input("Enter the Choice:"))
    #if ch== 1:  
    asi=p*(1+ (r*t))
    print("\n Simple Interest = ",asi)
    
    #elif ch== 2:  
    aci=p*((1+ r/n) ** (n*t))
    print("\n Compound Interest = ",aci)
        
    #else:
    #print("Incorrect")
    f=f-1
        
    
