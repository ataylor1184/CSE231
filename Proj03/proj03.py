#==============================================================================
# This program repeatedly prompts the user for a word, collecting the vowels, 
# and the consonants that appear after the last vowel. The program ends after
# collecting all possible vowels or 5 different consonants
#==============================================================================

VOWELS = ['a',"e","i","o","u"]
CONS=["b","c","d","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
count =0
vow_count =0
cons_count = 0 
vow_str =""
cons_str =""
loc = 0

while vow_count<5:
    if cons_count >=5:
        break
    else:
        word = input("Input a word: ")
        for count,char in enumerate(word): #traverses the word assigning a num per letter
            if char in "aeoiu": #if char is a vowel
                loc = count #saves position of vowel in word
                if char in VOWELS:
                    vow_count += 1 #counts vowels
                    vow_str += word[count] #stores vowel
                    VOWELS = [x for x in VOWELS if x != word[count]] #removes vowel from list
           
                
        
        post_vowel_word = word[loc+1:len(word)] #slices word from last vowel to the end
        for count2, char in enumerate(post_vowel_word): #traverses each letter of word
            if char in CONS : #if letter is a consonant
                cons_count +=1 #counts consonant
                cons_str += post_vowel_word[count2] #stores consonant
                CONS = [x for x in CONS if x !=post_vowel_word[count2]] #removes consonant from list
               
        

       
          
print("\n"+"="*12)               
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants","length"))
print("{:8s}{:<7} | {:12s}{:}".format(vow_str,vow_count,cons_str,cons_count))