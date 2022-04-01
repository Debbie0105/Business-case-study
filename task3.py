def simDetector(a, b):
   a = a.lower()
   b = b.lower()

   words_a = a.split()
   words_b = b.split()
  
   words_Common = []
   words_Uncommon = []

   for w in words_a:
       if w in words_b:
           words_Common.append(w);
       else:
           words_Uncommon.append(w);

   for w in words_b:
       if w not in words_a:
           words_Uncommon.append(w);

   sa = set(words_Common)
   sb = set(words_Uncommon)


   return 100 * len(sa)/(len(sa) + len(sb))

print("Enter the first submission : ")
a = input();
print("Enter the second submission : ")
b = input();

print("The similarity score between the two is : %.2f%%" % simDetector(a, b))