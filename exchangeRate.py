def printHeader(case):
    print("")
    print("-------------",case, "----------------")
    print("")

def printData(s,state):
    if state == 1:
        cols = 7
    else:
        cols = 8
    for r in range(0, 4):
        for c in range(0, cols):
            print(s[r][c], end=" ")
        print()
    print(" ")

def printResult(count,str):
    if count % 2 == 0:
        print(str, "Acceptable.")
    else:
        print(str, "Error.")


case1 = 'First Case (no error) : '
case2 = 'Second Case (one error) : '
case3 = 'Third Case (two errors) : '
signal = '10001101011000'
printHeader('1.1')
s = [int(x) for x in str(signal)]
count = sum(s)
if count % 2 == 0:
    signal = signal + "0"
else:
    signal = signal + "1"
print("The final signal is : ", signal)


printHeader('1.2')
s = [int(x) for x in str(signal)]
count = sum(s)
printResult(count,case1)
if s[5] == 1:
    s[5] = 0
else:
    s[5] = 1
count = sum(s)
printResult(count,case2)
if s[11] == 1:
    s[11] = 0
else:
    s[11] = 1
count = sum(s)
printResult(count,case3)
printHeader('1.3')
# signal = input()
signal = '1100111101110101110010101001'

k = 0
s = [[0 for x in range(0, 8)] for y in range(0, 5)]
for i in range(0, 4):
    for j in range(0, 7):
        s[i][j] = signal[k]
        k = k + 1
print("Original data.")
printData(s,1)


for i in range(0, 4):
    count = 0
    for j in range(0, 7):
        if s[i][j] == '1':
            count = count + 1
    if count % 2 == 0:
        s[i][7] = '0'
    else:
        s[i][7] = '1'

for j in range(0, 8):
    count = 0
    for i in range(0, 4):
        if s[i][j] == '1':
            count = count + 1
    if count % 2 == 0:
        s[4][j] = '0'
    else:
        s[4][j] = '1'


print("New data.")
printData(s,2)

printHeader('1.4')
j = 0
count = 0
while True:
    for i in range(0, 5):
        if s[i][j] == '1':
            count = count + 1
    if count % 2 == 1:
        break
    if j == 7:
        break
    j = j + 1
printResult(count,case1)
j = 0
count = 0
if s[1][2] == '1':
    s[1][2] = '0'
else:
    s[1][2] = '1'

while True:
    for i in range(0, 5):
        if s[i][j] == '1':
            count = count + 1
    if count % 2 == 1:
        break
    if j == 7:
        break
    j = j + 1
printResult(count,case2)
if s[1][4] == '1':
    s[1][4] = '0'
else:
    s[1][4] = '1'
j = 0
count = 0
while True:
    for i in range(0, 5):
        if s[i][j] == '1':
            count = count + 1
    if count % 2 == 1:
        break
    if j == 7:
        break
    j = j + 1
printResult(count,case3)
