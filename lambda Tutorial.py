숫자 = [1,2,3,4,5]
승수 = [2,2,2,3,3]

# list(zip(숫자,승수))
print(list(map(lambda x: x[0] ** x[1],zip(숫자,승수))))

for i in zip(숫자, 승수):
    print(i)

for i, j in zip(숫자, 승수):
    print(i,j)

print(list(filter(lambda x : x > 100, list(map(lambda x: x[0] ** x[1],zip(숫자,승수))))))
print(sum(map(lambda x: x[0] ** x[1],zip(숫자,승수))))
