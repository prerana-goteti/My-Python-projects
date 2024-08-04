i = 1
s = 0
nn = s + i
while nn <= 1000:
    print(nn)
    print("Numbers", i , "through", s)
    print(i)
    print(s)
    print(nn)
    i = s
    s  = nn
    nn = i + s
print("The squence is completed!")