n=int(input("enter seconds: "))

h=n//3600
n=n%3600
m=n//60
n=n%60

print("number of hours: ",h)
print("number of minutes: ",m)
print("number of seconds: ",n)

