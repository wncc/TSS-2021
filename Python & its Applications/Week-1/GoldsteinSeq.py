#Point the conciseness and compactness with which you can define functions in Python!

n = int(input('What would you want n to be?'))
m = int(input('What would you want m to be?'))

getInBase = (lambda m,n: m if m==0 else ((m%n) + (n+1)*(getInBase(m//n,n))))
GoodStein = lambda m,n: m if n==1 else getInBase(GoodStein(m,n-1),n)

print(GoodStein(m,n))
