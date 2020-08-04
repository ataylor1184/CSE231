#==============================================================================
# This is a game called Gomoku, its kind of like connect 4, except in our case
# it would be connect 5. players put pieces on a board and alternate turns.
# the first person to have 5 consecutive pieces in a row, column, or a diagnal
# wins the game.
#==============================================================================


class GoPiece(object):
    ''' creates a piece object'''
    def __init__(self,color='black'):
        '''Creates a object with one attribute, color'''
        self.color = color
        if color != 'black' and color != 'white':
            raise MyError('Wrong color.')   
    
    def __str__(self):
        '''returns black/white dot for objects with black/white attributes, respectively'''
        if self.color == 'black':
            return ' ● '
        if self.color == 'white':
            return ' ○ ' 
        elif self.color != 'white' and self.color != 'black':
          raise MyError('Wrong Color.')
    
    def get_color(self):
        ''' returns a string of the color of the object.'''
        return self.color
                   
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''Creates the 'board' object with several attributes initialized below'''
    def __init__(self,board_size=15,win_count=5,current_player='black'):
        '''sets the default attributes of the board, size = 15x15, win count = 5, current player = black
            Then it initializes the board with the attributes below
        '''
        self.__board_size = board_size
        self.win_count = win_count
        
        self.__current_player = current_player
        if current_player != 'black' and current_player != 'white':
            raise MyError('Wrong color.')
        try:
            self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
        except:
            raise ValueError
            
    def assign_piece(self,piece,row,col):
        '''Trys to place a piece on the board, raises errors if position is taken or doesnt exist'''
        try:
           row = int(row) -1
           col = int(col) -1
        except:
            raise MyError('Incorrect input.')
   
        piece = (' ● ' if piece.color == 'black' else ' ○ ')

        if row >15 or col > 15:
            raise MyError('Invalid position.')
        if self.__go_board[row][col] != ' - ':
            raise MyError('Position is occupied.')
        else: 
            self.__go_board[row][col] = piece
          
    def get_current_player(self):
        '''returns current player as a string such as 'black'''
        return self.__current_player
    
    def switch_current_player(self):
        ''' checks for current player, and returns the other player instead'''
        if self.__current_player== 'white':
            self.__current_player = 'black'    
        else:
            self.__current_player = 'white'
            
        return self.__current_player
      
        
    def __str__(self):
        
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        
        return s
        
    def current_player_is_winner(self):
        ''' Checks if the current player is winner by comparing the number of pieces in a row with the 
            win_count requirement that is initialized with the board.
            
            Checks the board horizontally. vertically and diagnally in that order.
        
        '''
       
           
        x_count = 0
        y_count = 0
        z_count = 0
        board_copy = []
        
        player_color = (' ● ' if self.__current_player == 'black' else ' ○ ')
        
        
        for row in self.__go_board:
            for col in row:
                if str(col) == str(player_color):   #iterates horizontally
                    x_count +=1                     #counts the player's pieces  
                else:
                    x_count = 0                    
                if x_count == self.win_count: 
                     return(True)                   #wins if count = win_count  
                    
        columns = 15
        rows = 15        
        for y in range(columns):
            for x in range(rows): 
                if str(self.__go_board[x][y]) == str(player_color):   #iterates vertically
                    y_count +=1                                       #counts the player's pieces  
                else:
                    y_count = 0                                     
                if y_count == self.win_count:                         #wins if count = win_count
                        return(True)
                    
                              
        for row in self.__go_board:
            board_copy.append(row)
        
                                                            #creates a copy of the current board
 
        diagnal_list = [[] for i in range(len(board_copy))]  #creates a list of the diagnals
                                                            #in the board starting at the bottom left
        for line in range(len(board_copy)): 
                                            #and adding elements along the diagnals down and
            board_copy[line].reverse()    
                                                         #to the right
            i = line
            for elem in board_copy[line]:
                if i >= len(diagnal_list):
                    diagnal_list.append([])
                diagnal_list[i].append(elem)
                i += 1
        diagnal_list.reverse()              #the diagnals are now organized in a list of lists
        for row in diagnal_list:            #horizontal traverse through them and count the points
            for col in row:
                if str(col) == str(player_color):
                    z_count +=1
                else:
                    z_count = 0   
                if z_count == self.win_count:
                        return True
                    
                    

        
        diagnal_list = [[] for i in range(len(board_copy))]  #creates a list of the diagnals
                                                            #in the board starting at the bottom right
        for line in range(len(board_copy)): 
                                            #and adding elements along the diagnals down and
            board_copy[line].reverse()    
                                                         #to the left
            i = line
            for elem in board_copy[line]:
                if i >= len(diagnal_list):
                    diagnal_list.append([])
                diagnal_list[i].append(elem)
                i += 1
        diagnal_list.reverse()              #the diagnals are now organized in a list of lists
        for row in diagnal_list:            #horizontal traverse through them and count the points
            for col in row:
                if str(col) == str(player_color):
                    z_count +=1
                else:
                    z_count = 0   
                if z_count == self.win_count:
                        return True
                    
                    
        return False         
                 
      

def main():
    row = ''
    col=''
    board = Gomoku()
    player = GoPiece('black') 
    player.color = 'black'
    
    print(board)
  
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        try: 
            try:
                 row = play_list[0]
                 col = play_list[1]
            except:
                 raise MyError("Incorrect input.")
            board.assign_piece(player,row,col)
        except MyError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                board.switch_current_player()

        
        if board.current_player_is_winner():
             board.current_player_is_winner()
             print(board)
             print("{} Wins!".format(board.get_current_player()))
             play = 'q'
        else:
            board.current_player_is_winner()
            board.switch_current_player()
            player.color = board.get_current_player()
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()
