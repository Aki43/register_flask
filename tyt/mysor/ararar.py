# aa ds gkd ee aa a ds sf y e y
# a = input().lower().split()
# b = set(a)
# for i in b:
#     print(i, a.count(i))


a = int(input())
b = [int(input()) for i in range(a)]
d = {}
for i in b:
    if i not in d:
        d[i] = f(i)
        print(d[i])
