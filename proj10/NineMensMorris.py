

import NMM #This is necessary for the project


#==============================================================================
# A simple game, sort of like tick tack toe and checkers with a larger board
# 
# 
# 
# 
# 
# 
# 
# 
# 
#==============================================================================


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
def get_mills(board,player):
    """
    returns the mills by a list of tuples, found same way as count_mills function
    """
    mill_test = 0 
    mill_count= 0     #same as the count mills function but it returns the points
    mill_points= []
    
    for tup in board.MILLS:
        for point in tup:
            if board.points[point] == player:
                mill_test += 1 
                if mill_test == 3:
                    mill_count +=1
                    mill_test = 0 
                    mill_points.append(tup)
                    
        mill_test = 0 
    return(mill_points)
    
        
def count_mills(board, player):
    """
        add your function header here.
    """
    mill_test = 0 
    mill_count= 0
    mill_points= []
    
    for tup in board.MILLS:
        for point in tup:
            if board.points[point] == player:
                mill_test += 1 
                if mill_test == 3:
                    mill_count +=1
                    mill_test = 0 
                    mill_points.append(tup)
                    
        mill_test = 0 
    return(mill_count)
                
            
def place_piece_and_remove_opponents(board, player, destination):
    """
        Adds the player's piece to the board, or removes opponents piece when 
        a mill is formed
    """
    if destination == 'q' or destination =='r' or destination =='h':
        pass
    else:
        if destination not in board.points:
            raise RuntimeError("Invalid command: Not a valid point")
        else:
            if board.points[destination] != 'O' and board.points[destination] != 'X':
                    board.assign_piece(player,destination)
            else:
                    raise RuntimeError("Invalid command: Destination point already taken")

     
def move_piece(board, player, origin, destination):
    """
        attempts to move a piece to another position in phase 2
    """
    booling = False    
    while booling == False:
        #    try:
                if origin in placed(board,player) and destination in board.points and board.points[origin] == player:
                        if destination in board.ADJACENCY[origin] and board.points[destination] == ' ':
                            booling = True
                            place_piece_and_remove_opponents(board,player,destination)
                            if origin in placed(board,player):
                                board.clear_place(origin)
                            
                        else:
                             raise RuntimeError("Invalid command: Destination is not adjacent")
                else:
                    raise RuntimeError("Invalid command: Origin point does not belong to player")
         #   except:
          #      raise RuntimeError("\nInvalid command: Not a valid point")             
                break
    
def points_not_in_mills(board, player):
    """
        returns a set of points placed on the board, that are not in a mill
    """
    mill_test = 0
    points_not_in_mills_set = set()
    placed_set = set()  
    placed_set = placed(board,player)  #set of every placed point by player
    final_set = set()
    
    for tup in board.MILLS:
        for point in tup:
                points_not_in_mills_set.add(point)  #Adds every point to a set
            
    for tup in board.MILLS:                      #Checks for a mill of current player
        for point in tup:
            if board.points[point] == player:
                mill_test += 1 
                if mill_test == 3:
                    for point in tup:   
                        try: #removes sets from the the points
                            points_not_in_mills_set.remove(point) #set contains all points not in mills
                        except:
                            #error occurs when player does not have any points outside of mills
                            pass  
                    mill_test = 0 
        mill_test = 0 
        
    for point in placed_set:     #for every placed point
        if point in points_not_in_mills_set:   #if the point is not in a mill
            final_set.add(point)                #put it into set)
    return(final_set)


def placed(board,player):
    """
        returns a set of points occupied by the current player
    """
    placed_set = set() 
    for tup in board.MILLS:
        for point in tup:
            if board.points[point] != ' ' and board.points[point] == player:
                placed_set.add(point)         
    return(placed_set)

    
def remove_piece(board, player):
    """
        removes a piece by calling clear_place, loops again if point is invalid
    """
    booling = False
    not_mill_set = set()  
    player = get_other_player(player)                                       
    not_mill_set =  points_not_in_mills(board, player)
 
    while booling == False:
        command = input("Remove a piece at :> ").strip().lower()
        try: 
            if command in not_mill_set:
                board.clear_place(command)
                booling = True
            else:
                print("Invalid command: Point is in a mill")   
                print("Try again.")         

        except:
                print('Invalid command: Point does not belong to player')
                
    

           
def is_winner(board, player):
    """
        checks if player has won by counting the number of enemy pieces
        if the enemy has 2 or less, returns true
    """
    player2 = get_other_player(player) #finds 'opponent' player
    opponent_count = 0     
    for point in placed(board,player2):
        opponent_count +=1  
    return True if opponent_count <=2 else False
    


   
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"
    
def main():
    
    while True:
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        temp_mills_before = 0
        temp_mills_after = 1
        points_in_mills_before = set()
        points_in_mills_after = set()
        
        placed_count = 0 
        # PHASE 1
         
        print(player + "'s turn!")   
        command = input("Place a piece at :> ").strip().lower()
        placed_count +=1 
        place_piece_and_remove_opponents(board,player,command)
        
        print()
        print(board)
                  
#====================================================== first run ^ =======================#
#=======================================================Phase 1============================#
        
        count_mills(board,player)
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count < 18:
            player = get_other_player(player)
            print(player + "'s turn!")   
      
            try:
                temp_mills_before = count_mills(board, player)
                command = input("Place a piece at :> ").strip().lower()
                place_piece_and_remove_opponents(board, player, command)
                temp_mills_after = count_mills(board, player)
                if temp_mills_before != temp_mills_after:
                    print("A mill was formed!")
                    print(board)
                    points_not_in_mills(board, player)
                    remove_piece(board,player)

                placed_count += 1
                placed(board,player)

            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                command = input("Place a piece at :> ").strip().lower()
            if command == 'q':
                return
            if command =='h': 
                print(MENU)
               # command = input("Place a piece at :> ").strip().lower()
                try:
                    temp_mills_before = count_mills(board, player)
                    command = input("Place a piece at :> ").strip().lower()
                    place_piece_and_remove_opponents(board, player, command)
                    temp_mills_after = count_mills(board, player)
                    if temp_mills_before != temp_mills_after:
                        print("A mill was formed!")
                        print(board)
                        points_not_in_mills(board, player)
                        remove_piece(board,player)

                    placed_count += 1
                    placed(board,player)

                except RuntimeError as error_message:
                    print("{:s}\nTry again.".format(str(error_message)))
       
            if command =='r':
                for point in board.points:
                    board.clear_place(point)
                player = "X"
                print(RULES)
                print(MENU)
                print(board)
                
                placed_count = 0 
       
         
                print(player + "'s turn!")   
                command = input("Place a piece at :> ").strip().lower()
                placed_count +=1 
                place_piece_and_remove_opponents(board,player,command)
                print(board)
       
               # main()
                continue
            print(board)

   
#========================================Phase 2============================================# 
        player = get_other_player(player)
        print(player + "'s turn!")            
        print("**** Begin Phase 2: Move pieces by specifying two points")
        
        if command == 'r':   
            continue 
        command = input("Move a piece (source,destination) :> ").strip().lower()    
        while command != 'q' and placed_count >= 18:
            command = command.split(' ')
            try:  
                try:
                    origin = command[0]
                    destination = command[1]
                except:
                     #   print('\nInvalid number of points')
                    raise RuntimeError("\nInvalid number of points")
              
                temp_mills_before = count_mills(board, player)
                points_in_mills_before = get_mills(board, player) #keeping track of mill information, before move
                try:
                    move_piece(board,player,origin,destination)
                except:
                    raise RuntimeError("Invalid command: Not a valid point")
                
                temp_mills_after = count_mills(board, player)
                points_in_mills_after = get_mills(board, player) # keeping track of mill information, after move
               
                if temp_mills_before < temp_mills_after:
                    print("\nA mill was formed!")      
                    print(board)
                    remove_piece(board,player)
                elif points_in_mills_before != points_in_mills_after and temp_mills_before == temp_mills_after and temp_mills_after !=0:
                    print("\nA mill was formed!")            #for that special case where your mill count remains the same
                    print(board)                           #but a mill was formed the same time one was broken, happens in test 1 
                    remove_piece(board,player)
                #print('is_winner?',is_winner(board,player))
                if is_winner(board,player) == True:
                    print(BANNER)
                    return
                player = get_other_player(player)
            
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))   
                      
            print(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            if command == 'q':
                return
            if command =='h':
                print(MENU)
            if command =='r':
                main()

        #If we ever quit we need to return
    if command == 'q':
            return
   

if __name__ == "__main__":
    main()
