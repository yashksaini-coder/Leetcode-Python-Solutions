X, Y, Z, N = 5,1,2,3
lis = [[x,y,z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x+y+z != N]
print(lis)


