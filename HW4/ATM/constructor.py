from Cash import Cash
import model
from Viewer import Viewer

printer = Viewer
wallet = Cash(0)


def menu():
    while True:
        printer("Choose operation:\n1.Addition\n2.Removing\n3.Exit\n")
        pos = input("Enter from 1 to 3:")
        if pos == "1":
            wallet.tax()
            printer("Input summa: ")
            plus = input()
            if plus.isdigit() and int(plus) % 50 == 0:
                model.addition_balance(int(plus), wallet)
                wallet.plus_point()
            else:
                printer("Wrong input, try again")
            printer(wallet)
        elif pos == "2":
            wallet.tax()
            printer("Input summa: ")
            minus = input()
            if minus.isdigit() and int(minus) % 50 == 0 and int(minus) < wallet.get_balance():
                percent = int(minus)*0.015
                model.addition_balance(-int(minus), wallet)
                if percent < 30:
                    model.addition_balance(-30, wallet)
                elif percent > 600:
                    model.addition_balance(-600, wallet)
                else:
                    model.addition_balance(-percent, wallet)
                wallet.plus_point()
            else:
                printer("Wrong input, try again")
            printer(wallet)
        elif pos == "3":
            for i in wallet.get_history():
                printer(i)
            printer("Goodbye")
            break
        else:
            printer("Wrong input, try again")
