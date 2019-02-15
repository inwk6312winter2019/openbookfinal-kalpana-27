fin = open("Book1.txt","r")
fin1 = open("Book2.txt","r")
fin2 = open("Book3.txt","r")
def sorted_words(task3):
  l = []
  for line in task3:
    word = line.strip()
    k = word.split()
    k = k.sort(key = str.lower)
    l = l.append(k)
    return l

print(sorted_words(fin))
print(sorted_words(fin1))
print(sorted_words(fin))
