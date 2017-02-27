#Anagrams
#Katie Shiver

#Open the file
f = open('words.txt')

dictionary = {}

for line in f:
    line = line.strip()
    alpha_line = ''.join(sorted(line))
    
    if alpha_line not in dictionary:
        dictionary[alpha_line] = [line]
    else:    
        dictionary[alpha_line].append(line)
        
for word in dictionary:
    print dictionary[word]
    
    
    