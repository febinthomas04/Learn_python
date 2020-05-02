bots= [2425,2350,2646]
bot_ip= ["10.1.0.210","10.1.0.91","10.1.2.226"]
Var = "IP of butler %d is : %s"

Battery=0

while Battery<=100 :
    Battery=Battery+2.2
    if Battery==11.0:
        continue
    if Battery>59.7:
        break
    print(Battery)