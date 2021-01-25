con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vow = ['a', 'e', 'i', 'o', 'u']
var = input()
for letter in var:
    #if letter.isalpha() != True: #and (letter not in vow and letter not in con) :
      #print('vowel') or print('consonant')
    if letter.isalpha() == True and ' ' in letter:
      if letter in con:
        print('consonant')
      elif letter in vow:
        print('vowel')
      else:
        break
    #elif letter in vow
      #break
    #print('vowel') or print('consonant')
