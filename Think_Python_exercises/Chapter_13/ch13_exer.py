import string 

# normalize all words in a text by stripping out punctuation and whitespace
def text_normalizer(f):
    
    # get the number of lines in the file for later use
    fin = open(f)        
    lines = fin.readlines()
    num_lines = len(lines)
    #print num_lines
    fin.close()
    
    
    fin = open(f)
    
    # empty list that will soon hold entire text as one list of words
    single_list = []
    
    # iterate through each line in the file
    for i in range(num_lines):        
        
        line = fin.readline()

        
        # punctuation-strip exception for "--" (em dash)
        if line.__contains__("--"):
            line = line.replace("--", " ")
            
        # replace hyphens with spaces
        if line.__contains__("-"):
            line = line.replace("-", " ")
        
        # strip all remaining punctuation     
        for char in line:
            if char in string.punctuation:
                line = line.replace(char, "")

        
        line = line.lower()

        words = line.split()

        if words != []:
            single_list += words

    # print single_list
    
    # return a single normalized list that contains words in the text
    return single_list


# takes a file and returns the number of words in it.
def wordcounter(f):
    # print len(text_normalizer(f))
    return len(text_normalizer(f))

# takes a file, prints the no. of different words in
# the file, and returns a dict showing word frequency
def word_histogram(f):
    text = text_normalizer(f)
    d = {}
    
    for word in text:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
        
    # print d
    return d
    
# prints the top 20 most frequent words in a file, 
# followed by the no. of times each one appears
def top_twenty(f):
    # generate a histogram dictionary from the file
    d = word_histogram(f)

    # convert dictionary into a sorted (ascending) list
    # of tuples, where k = frequency and v = word
    lst_tup = sorted([(v, k) for k, v in d.iteritems()])
    
    i = -1
    
    # print last 20 (i.e. most frequent) items, formatted
    for num in range(20):
        print lst_tup[i][1] + ": " + str(lst_tup[i][0])
        i -= 1
        
# takes a file (f), compares it to a word list
# and returns all the words in f that do not
# appear in the word list
def word_compare(f, wordlist):
    # generate dictionary of words (with words as keys)
    # to avoid word repetition
    d = word_histogram(f)
    
    # convert to list of words only
    d_to_lst = d.keys()
    
    # open word list
    # (precondition: each line of file contains one word)
    fin = open(wordlist, 'r')
    words = fin.readlines()
    
    # get rid of whitespace
    newlist = []    
    for line in words:
        word = line.strip()
        newlist += [word]
    
    print set(d_to_lst) - set(newlist)
    return set(d_to_lst) - set(newlist)


# text_normalizer("candp.txt")
# wordcounter("candp.txt")
# word_histogram("candp.txt")
# top_twenty("candp.txt")
word_compare("candp.txt", "words.txt")




 




