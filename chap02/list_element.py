#자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 3, 3.14, [32, 55], 'ABC']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
print(x[4][0], x[4][1])

print(x[5][0], x[5][1])