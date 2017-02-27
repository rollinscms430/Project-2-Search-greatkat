import random

class State(object):
    def __init__(self, moves):
        self.moves = moves



def random_letter():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
    'r','s','t','u','v','w','x','y','z']
    return alpha[random.randrange(25)]
    
def check_word(word, dictionary):
    if word in dictionary:
        return True
    else:
        return False
        
def check_prefix(word, prefix):
    if word in prefix:
        return True
    else:
        return False
        
def hash(moves):
    sum = 0
    
    for i in range(len(moves)*len(moves)):
        row = i/len(moves)
        col = i%len(moves)
        sum += 2** i * moves[row][col]
    return sum
    
def already_visited(state, visited):
    if hash(state.moves) in visited:
        return True
    else:
        return False
        
def add_to_visited(state, visited):
    h = hash(state.moves)
    visited[h] = True


def solve(n):

    dictionary = {}
    prefixes = {}
    
    #Create dictionary of words from txt file
    f = open('words.txt')
    
    for line in f:
        line = line.strip()
        dictionary[line] = list(line)
        if line[:2] not in prefixes:
            prefixes[line[:2]] = 0
    

    #predetermined set of letters for grid
    grid = [['u', 'n', 't', 'h'], ['g', 'a', 'e', 's',], ['s', 'r', 't', 'r'], ['h', 'm', 'i', 'a']]
    
    #random set of letters for grid
    #grid = [[random_letter(self) for i in range(n)] for j in range(n)]

    state = State(moves)
    visited = {}
    words = []
    queue = []
    queue.append(state)
    
    while len(queue) > 0:
        state = queue.pop()
        
    
            

    


if __name__=='__main__':
    solve(4)    