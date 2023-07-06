a = ['ivan', 'petr', 'abdul']
b = [10000, 20000, 30000]
c = ['9.25%', '11%', '0.5%']

d = {i: j * float(k.replace('%',''))/100 for i, j, k in zip(a,b,c) }

print(d)
