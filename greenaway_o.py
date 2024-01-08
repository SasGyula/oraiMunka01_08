class Film:
    def __init__(self, cim, ev):
        self.cim = cim
        self.ev = int(ev)

    def __str__(self):
        return f"A könyv címe:{self.cim}, kiadása éve: {self.ev}"
