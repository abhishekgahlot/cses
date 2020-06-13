dna = input()

last = 0
tmp = ''

for i in range(len(dna)-1):
    if dna[i] == dna[i+1]:
        tmp += dna[i]
    else:
        last = max(last, len(tmp + dna[i]))
        tmp = ''

if tmp != '':
    last = max(last, len(tmp)+1)

if len(dna) == 1:
    print(1)
else:
    print(last)
