class RBI:
    def InterestRate(self):
        print("RBI rate is10%")
    
class SBI(RBI):
    def InterestRate(self):
        print("SBI Interest rate is 9.5%")

class PNB(RBI):
    def InterestRate(self):
        print("PNBInterest rate is 9%")

class IDBI(RBI):
    def InterestRate(self):
        print("IDBI Interest rate is 11%")

objidbi=IDBI()
objpnb=PNB()
objsbi=SBI()
objrbi=RBI()
objidbi.InterestRate()
objsbi.InterestRate()
objrbi.InterestRate()
objpnb.InterestRate()


