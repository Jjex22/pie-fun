# -*- coding: utf-8 -*-
from random import randint

##-------------------------- ===Global Variables===-------------------------##

size = 10                          # The size of the playboard
cornerstone = "_| "                # Symbol displayed in topleft corner
play_board = {cornerstone : []}    # Play area with each row a list
board_index = []                   # Row numbers
ship_list = {}                     # Ship components 

player1 = {}
player2 = {}                        # Play area for two player game
gues_board1 = {}
guess_board2 = {}

##-------------------------------===FUNCTIONS===----------------------------##

def boardgenerator(lgth):
    '''creates grid full of blank ocean.

    lgth must be an integer greater than 1
    '''
    for each in range(1,lgth+1):
        play_board[cornerstone].append("%s " %(str(each)))
        play_board[str(each)] = ["~" for item in range(lgth)]
        board_index.append(str(each))

def printboard(play_board):
    '''prints the play area. 

    takes type dictionary as input
    '''
    from os import system, name
    
    system('clear' if name != 'nt' else 'clr')
    print cornerstone + " ".join(play_board[cornerstone])
    for entry in board_index:
        print entry + "  " + "  ".join(play_board[entry])

def shipgenerator(snum):
    '''populates ship_list.
    
    must recieve a positive integer
    '''
    count = 0
    for boats in range(snum):
        ship_list[count]= ["◀ "]
        for segments in range(count):
           ship_list[count].append("◼ ")
        ship_list[count].append("▶ ")
        count += 1
    return ship_list

def randomPoint():
    '''returns a random co-ordinate within the play area'''
    """row = str(randint(1,len(board_index)))
    col = randint(0,len(board_index)-1)
    """
    location = play_board[str(randint(1,len(board_index)))]
        [randint(0,len(board_index)-1)]
    return location

def userShipPlot(snum,play_board):
    '''takes in an integer greater than zero
    takes the user's own board dictionary.
    prompts user to select a location for the bow
    and to set vertical/horizontal orientation.
    checks to see if plotting is valid then
    updates playboard 
    '''
    current_ship = 'Ship Selected: ' +  " ".join(ship_list[snum])
    layer1 = play_board.copy()
    while True:
        print current_ship
        orientation = userInput(
            'Do you want to place your ship horizontally (h),'\
            'or vertically (v)? ',
            'hv',
            1,
            'Invalid Input! \n' + current_ship
            ) 
        row = userInput('Which number row do you want the ship bow on? \n',
                str(range(1,(len(size)+1))),1,
                'Invalid Input! \n' + current_ship
                )
        col = userInput('Which number column do you want the ship bow on? \n',
                str(range(1,(len(size)+1))),1,
                'Invalid Input! \n' + current_ship
                )
        if shipPlot(row, col,play_board,snum,orientation):
            pass
            
            
def shipPlot(row,col,play_board,shipLgth,orientation):
    '''takes in the co-ordintes of the ship as a 
    positive integer. expects int to be in range 
    of board.
    checks if placing shipLgth in play_board is legal
    if legal, updates playboard and returns True.
    if not, returns False, without modifying the play_board.'''
    layer1 = play_board.copy()
    if orientation == 'h':
        for each in range(row-1,(row+snum+1)):
            try:
                if layer1[row][each] == '~':
                    layer1[row][each] = ship_list[snum][each]
                else: 
                    return False
            except:
                return False
    if orientation == 'v':
        for each in range(col-1,(col+snum+1)):
            if layer1[each][col] == '~':
                layer1[each][col] = (
                                    '▲' if each == 0 else 
                                    '▼' if each == (col+snum) else 
                                    ship_list[snum][each]
                                    )
            else:
                return False
            

print longString
def computerShipPlot():
    pass

    
def userInput(Q,A,L,E):
    '''asks user queestion Q
    checks if user input in  A
    checks if user input of length L
    if not prints message E and loops'''
    while True:
        answer = raw_input(Q)
        answer =str(answer).lower()
        if answer in A and len(answer) == L:
            return answer
        print E


##---------------------------------===GAME!===------------------------------##

shipgenerator(5)
for each in range(5):
    print "".join(ship_list[each])
boardgenerator(10)
printboard(play_board)
randomPoint()

##-----------------------------===TESTING CODE===---------------------------##
## ▲▼▶◀◼☆★   os.system('clear')
print cornerstone 
print play_board
print board_index
print ship_list