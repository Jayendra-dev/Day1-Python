# calculate simple interest and total amount by taking input from user;
p=float(input("enter principal here:"))
r=float(input("enter rate here:"))
t=float(input("enter time:"))
si=p*r*t/100
totalamt=p+si
print("your si  is:",si)
print("your total amount is:",totalamt)
print("CONSISTENCY>INTENSITY")