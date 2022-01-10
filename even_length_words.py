
s = "I am Bhavya Sree " 
s = s.split()
for w in s:
    if len(s)%2 == 0: #it prints the words only if the 's' has the even number of words in a sentence
        print(w)
'''Output I
        am
        Bhavya
        Sree '''

s = 'I am Bhavya Sree CSE'
s = s.split()
for w in s:
    if len(w)%2==0: #it prints only if the single word inside the sentence has even alphabets
        print(w)
    #else:
        #print("It don't have even alphabets in a word  ")
''' Outpt :am
        Bhavya
        Sree'''
