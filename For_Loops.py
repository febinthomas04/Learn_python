bots= [2425,2350,2646]
bot_ip= ["10.1.0.210","10.1.0.91","10.1.2.226"]
Var = "IP of butler %d is : %s"

# Using for loop with variable size:

for var in bots:
    print("Available Butlers are:" ,var)


# Using for loop in a given range:

for x in range(0,10,2):
    if x==4:
        print("The Number is 4")
        continue
    print(x)
