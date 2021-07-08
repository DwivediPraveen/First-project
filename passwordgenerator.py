import random
passlen =int(input("Number of digit password- " ))

s= "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*><?"
p = "".join(random.sample(s, passlen))

print("your password is: "+ p)