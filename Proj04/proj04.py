#==============================================================================
# This program is used to determine if you are laughing or not
# It does so by checking for patterns in the charectors entered
# Any combination of H followed by A or O followed by H again
# and ending in !, is considered laughing
#==============================================================================

def get_ch():
    ch= "test"
    while ch!= "":
        ch = input("Enter a character or press the Return key to finish: ")
        if len(ch)<=1 and ch.isalpha: #checks length of charector entered
            return ch #returns charector
        else:
            print("Invalid input, please try again.")

def find_state(state, ch):
    st = state     
    if ch != "": #if charector is blank, return the state
        if st ==1:
            if ch=='h': #checks if first letter is an H
                st=2
                return st #sets state to 2, to check next letter
            else :
                st = 5
                return st
        
        if st ==2:
            if ch== 'o' or ch=='a': #check if next letter is an A or O
                st =3 #moves on to third state 
                return st
            else :
                st=5
                return st
        
        if st ==3:
            if ch== 'h': #If letter is an H, next letter that is checked is
                st =2 #O or A, so back to state 2 
                return st
            elif ch =='!': 
                st = 4
            else :
                st=5
                return st
        
        if st ==4:
            if ch== '!':
                st =4
                return 4
            else :
                st =5
                return 5
    else : 
        return st
    pass

def main():
    user_input =""
    state_count = 1
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")
    string = "empty"
    while string != "":
        string = get_ch()
        user_input += string
        state_count = find_state(state_count,string) #recursively calls itself
    print("\nYou entered", user_input)
    if state_count ==4:
        print("You are laughing.")
        
    else :
        print("You are not laughing.")

main()