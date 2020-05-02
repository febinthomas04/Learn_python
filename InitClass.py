class rect:
    def __init__(self,Bot_id,Bot_ip,Bot_fw):
        self.Bot_fw = Bot_fw
        self.Bot_id = Bot_id
        self.Bot_ip = Bot_ip

    def Bot_f(self):
        var = print(self.Bot_fw + "is the Bot Firmware")
        return var