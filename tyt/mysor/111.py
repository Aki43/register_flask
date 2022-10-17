zz = 0
gg = 0
nn = 0
k = 0
with open('filik') as inf:
    for i in inf:
        stark = i.strip().split(';')
        student_average = ((int(stark[1]) + int(stark[2]) + int(stark[3])) / 3)
        print(student_average)
        zz += int(stark[1])
        k += 1
        gg += int(stark[2])
        nn += int(stark[3])
    print(zz / k, gg / k, nn / k)
with open('russia', 'w') as t:
    t.write(str(student_average) + '\n')
