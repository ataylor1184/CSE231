#from proj11 import GoPiece, Gomoku,MyError
listt = [[ 'x', 'b', 'c', 'd', 'x', 'f', 'g', 'h','i'    ],
         [ 'j', 'x', 'l', 'x', 'n', 'o', 'p', 'q','r'    ],
         [ 's',' t', 'x', 'v', 'w', 'x', 'y', 'z',  1    ],
         [  2  , 'x'  , 4  , 'x'  , 6  , 7  , 8  , 9 ,'a1'   ],
         ['x','a3','a4','a5','a6','a7','a8','a9','a10'] ]

for row in listt:
    for col in row:
        #print (col)   #horizontal traverse
        pass
        
columns = 9
rows = 5        
for y in range(columns):
    for x in range(rows):                      #verticle traverse
        #print (listt[x][y])
        pass
   

        
def diagonal(l):
    count = 0 
    L = l[:]
    return_list = [[] for i in range(len(L))]
    for line in range(len(L)):
        #L[line].reverse()
        i = line
        for elem in L[line]:
            if i >= len(return_list):
                return_list.append([])
            return_list[i].append(elem)
            i += 1
    return_list.reverse()                   #diagnal traverse (starting bot left, traverse left to bot right)
    for row in return_list:
        for value in row:
            print('value',value)
            if str(value) == 'x':
                count +=1
                print('count',count)
                if count == 5:
                    print('bingo')
            else:
                count = 0   
            
    return return_list

print(diagonal(listt))

