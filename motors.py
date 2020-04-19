from utime import sleep

class Motors:
    def __init__(self, rA, rB, lA, lB):
        self.motorRA = rA
        self.motorRB = rB
        self.motorLA = lA
        self.motorLB = lB

    def forward(self):
        sleep(0.1)
        self.motorRA.on()
        self.motorRB.off()
        self.motorLA.on()
        self.motorLB.off()

    def backward(self):
        sleep(0.1)
        self.motorRA.off()
        self.motorRB.on()
        self.motorLA.off()
        self.motorLB.on()

    def right(self):
        sleep(0.1)
        self.motorRA.on()
        self.motorRB.off()
        self.motorLA.off()
        self.motorLB.on()

    def left(self):
        sleep(0.1)
        self.motorRA.off()
        self.motorRB.on()
        self.motorLA.on()
        self.motorLB.off()

    def stop(self):
        sleep(0.1)
        self.motorRA.off()
        self.motorRB.off()
        self.motorLA.off()
        self.motorLB.off()
    