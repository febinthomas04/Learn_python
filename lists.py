bots= [2425,2350,2646]
bot_ip= ["10.1.0.210","10.1.0.91","10.1.2.226"]
Var = "IP of butler %d is : %s"
bot_ip.append("192.168.9.90")
del bot_ip[3]
Fin = Var%(bots[0],bot_ip[0])
check = len(bot_ip)
print Fin
print bot_ip