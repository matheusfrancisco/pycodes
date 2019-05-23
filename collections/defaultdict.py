from collections import defaultdict, Counter
string = 'matheus esta na casa do jão e vai brincar'

listinha =  [1,2,34,3,2,1,1,1,1,2,3,4,5,6,7,3,3,3,2,2,1,1,1,12,3,4,4,444]
ct = Counter(string)
ct_2 = Counter(listinha)

#mostra as duas mais comuns
print(ct_2.most_common(2))

# Counter('ahah') & Counter('abc')

