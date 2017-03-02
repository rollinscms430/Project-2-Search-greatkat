#Boggle
#Katie Shiver
#Worked with DC

from copy import deepcopy
import random

#Global variables
d = {}
prefix_dict = {}

board = [['u','n', 't', 'h'] ,
         ['g', 'a', 'e', 's'],
         ['s', 'r', 't', 'r'],
         ['h', 'm', 'i', 'a']]
#Possible random generated board code below

class State(object):
    
    """
        Represents the current state of the board
        
    """
    
    def __init__(self, position, sequence):
        
        self.position = position
        self.sequence = sequence
        
        
    def add_position(self, position):
        
        new_position = deepcopy(self.position)
        new_position.append(position)
            
        new_sequence = deepcopy(self.sequence)
        new_sequence += board[position[0]][position[1]]
        
        return State(new_position, new_sequence)
        
#******************        

#Create dictionary
def init_dict(file):
    f = open(file)
    for word in f:
        word = word.strip()
        d.setdefault(word, [])
        
#Create prefix dictinary
def init_prefix(d):
    
    for word in d:
        prefix = ""
        for i in range(len(word)):
            prefix += word[i]
            if prefix not in prefix_dict:
                prefix_dict[prefix] = True
                
#Generates children
def gen_children(state):
    
    current_position = state.position[len(state.position) - 1]
    
    for i in range(max(0, current_position[0] - 1), min(len(board) - 1, current_position[0] + 2)):
        for j in range(max(0, current_position[1] - 1), min(len(board[i]) - 1, current_position[1] + 2)):
            
            position = (i, j)
            if position != current_position:
                new_state = state.add_position(position)
            
                recursive_search(new_state)

#Searches for the word and prints it
def recursive_search(state):
    
    if state.sequence in d:
        print state.sequence
        
    if state.sequence in prefix_dict:
        gen_children(state)

#Main solve
def solve(board):
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            init_position = [(i, j)]
            
            init_sequence = board[i][j]
            
            state = State(init_position, init_sequence)
            
            recursive_search(state)


if __name__ == '__main__':
    
    init_dict('words.txt')
    init_prefix(d)
    
    solve(board)








#def create_board(n):
    #predetermined set of letters for grid
    #board = [['u', 'n', 't', 'h'], ['g', 'a', 'e', 's',], ['s', 'r', 't', 'r'], ['h', 'm', 'i', 'a']]
    
    #random set of letters for grid
    #board = [[random_letter() for i in range(board_size)] for j in range(board_size)]

#def random_letter():
    #alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
    #'r','s','t','u','v','w','x','y','z']
    #return alpha[random.randrange(25)]
