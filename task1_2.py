fin = open("Book1.txt","r")
fin1 = open("Book2.txt","r")
fin2 = open("Book3.txt","r")
def count_the_article(task2):
  c = 0
 
  list1 = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
  for line in task2:
    word = line.strip()
    word = word.lower()

    for i in list1:
      if i == word:
        c +=1
      print(c)


count_the_article(fin)
