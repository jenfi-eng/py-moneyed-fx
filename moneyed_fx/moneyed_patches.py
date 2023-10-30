from moneyed import Money

def moneyed_fx_test(self):
    return f"Moneyed FX Test: {self}, {self.amount}."

Money.moneyed_fx_test = moneyed_fx_test
