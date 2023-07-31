
idx = 0
max = 0

for i in range(0,9):
    num = int(input())
    if num >= max:
        max = num
        idx = i+1


print(max)
print(idx)
