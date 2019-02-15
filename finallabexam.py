fin = open("Book1.txt","r")
fin1 = open("Book2.txt","r")
fin2 = open("Book3.txt","r")
def unique_words(task1):

  list1 = []
  for line in task1:
    word = line.strip() 
    word = word.split()
    list1.append(word)

    if word not in list1:
      list1.append(word)
    return list1


print(unique_words(fin))
print(unique_words(fin1))
print(unique_words(fin2)) 

