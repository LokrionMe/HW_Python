def fibbo(n:int)->int:
    n_one = 0
    n_two = 1
    for _ in range(n):
        yield n_one
        n_one, n_two = n_two, n_two + n_one

for i , sum in enumerate(fibbo(10),start=1):
    print(f'{i} = {sum}')
