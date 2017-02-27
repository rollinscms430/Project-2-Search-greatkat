#Word Ladders
#Katie Shiver

class State(object):
    
    """Represents a state in the solution
    
    Attributes:
        path: the sequence of words to get from starting word to final word"""
        
    def __init__(self, path):
        self.path = path
        
def finished(path, end_word):
    if path[len(path)-1] == end_word:
        return True
    else:
        return False
    
def solve (start_word, end_word):
    #Open the file
    print "start"
    f = open('words.txt')
        
    dictionary = {}
        
    for line in f:
        line = line.strip() #Removes whitespace
        if len(line) == len(start_word):
            for i in range(len(line)):
                word = '{}_{}'.format(line[:i], line[i + 1:])
                if word not in dictionary:
                    dictionary[word] = [line]
                else:    
                    dictionary[word].append(line) 
                 
    for word in dictionary:
        print word, dictionary[word]
            
    path = ['snakes', 'brains']
    
    if path[0] == 'snakes':
        print 'YES'
    
    print finished(path, end_word)
        
        
    
                        #letters = list(start_word)
                        #print letters[1]
                        
                        #way to increment through alphabet
                        #letter = 'a'
                        #for x in range(0,26):
                        #    print chr(ord(letter) + x)
    



if __name__ == '__main__':
        solve('snakes', 'brains')