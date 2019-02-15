fin=open("Book1.txt")
fin1=open("Book2.txt")
fin2=open("Book3.txt")

for line in fin:
  word = line.strip()
  word = word.split()
for line in fin1:
  word1 = line.strip()
  word1 = word1.split()
for line in fin2:
  word3 = line.strip()
  word3 = word3.split()
d = {}
for i in word:
  if i in word1 or word3:
    print(i)

