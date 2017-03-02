#Word Ladder
#Katie Shiver
#Worked with DC


from copy import deepcopy

queue = []
d = {}
visited = {}

start = 'snakes'
goal = 'brains'


class State(object):

    """Represents the state of the ladder
       Attributes:  
        ladder:  represents the current list of moves
    """
    
    def __init__(self, ladder):
        self.ladder = ladder
        
    #Adds word to the ladder
    def add_word(self, word):
        new_ladder = deepcopy(self.ladder)
        new_ladder.append(word)
        
        return State(new_ladder)
        
#*******************************    

#Build dictionaru
def init_dict(file):
    f = open(file)
    for word in f:
        word = word.strip()
        if len(word) == len(start):
            d.setdefault(word, [])

#Check if goal state found
def finished(state):   
    if state.ladder[len(state.ladder) - 1 ] == goal:
        return True
    
    return False

#Expand the children nodes
def expand_node(state):
    start = state.ladder[len(state.ladder) - 1]
    
    for word in d:
        if word != start:
            if len(word) == len(start):
                for i in range(len(start)):
                    slice_word = start[:i] + start[i+1:]
                    slice_cn = word[:i] + word[i+1:] 
                    
                    if slice_word == slice_cn:
                        if word not in visited:
                            visited[word] = 1
                            new_state = state.add_word(word)
                            queue.append(new_state)
            
#Main solve            
def solve(word):
    
    ladder = [word]
    init_state = State(ladder)
    queue.append(init_state)
    
    while len(queue) > 0:
        
        current_state = queue.pop(0)
        
        if finished(current_state):
            print current_state.ladder
        
        expand_node(current_state)
        
        
        
if __name__ == '__main__':
    init_dict('words.txt')
    solve(start)
