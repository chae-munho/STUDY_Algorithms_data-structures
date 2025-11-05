# *개를 n개를 출력하되 w개마다 줄바꿈하기 2

print("*")
n = int(input("몇 개를 출력할까요? : "))
w = int(input("몇 개마다 줄바꿈할까요? : " ))

for _ in range(n // w):
    print("*" * w)
rest = n % w
if rest: #if문 판단 1번
    print("*" * rest)