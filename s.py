import matplotlib.pyplot as plt

n = int(input())
y = []

while n != 1:
    y.append(n)

    if n%2 == 0:
        n /= 2
    else:
        n = n*3 + 1

y.append(1)

plt.plot(y, 'o-')
plt.grid(True)
plt.show()