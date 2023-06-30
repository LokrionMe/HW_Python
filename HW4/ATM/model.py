from Cash import Cash


def addition_balance(summa, wallet: Cash):
    wallet.Balance += summa
    if summa > 0:
        wallet.add_history("Addition", summa)
    else:
        wallet.add_history("Removing", summa)
