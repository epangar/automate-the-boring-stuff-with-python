def sum(a,b):
    return a + b


for i in range (0, 10):
    for j in range(0,10):
        print ('%d + %d = %d' % (i, j, sum(i,j)) )