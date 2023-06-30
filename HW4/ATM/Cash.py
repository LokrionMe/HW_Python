from datetime import datetime


class Cash(object):
    def __init__(self, balance: float):
        self.Balance = balance
        self.point = 0
        self.history = []

    def __str__(self) -> str:
        return f"Balance = {self.Balance}"

    def plus_percent(self):
        self.add_history("Percent", self.Balance * 0.03)
        self.Balance *= 1.03
        

    def plus_point(self):
        self.point += 1
        if self.point == 3:
            self.plus_percent()
            self.point = 0

    def tax(self):
        if self.Balance > 5_000_000:
            self.add_history("Tax", self.Balance * 0.1)
            self.Balance *= 0.9
            

    def get_balance(self):
        return self.Balance

    def add_history(self, operation:str, summa:float):
        self.history.append(f"{datetime.now()} {operation}: {summa}")

    def get_history(self):
        return self.history
    

