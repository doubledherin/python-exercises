"""
Exercise 10.13

Two words "interlock" if taking alternating letters from each forms a new
word. 

For example, "shoe" and "cold" interlock to form "schooled." 
1. Write a program that finds all pairs of words that interlock. Hint: don't enumerate all pairs!

2. Can you find any words that are three-way interlocked; that is, every third letter forms a word, 
starting from the first, second or third?
"""

def bisect(t, v):
    found = False
    start = 0
    stop = len(t)-1
    while start<=stop and not found:
        midpoint = (start+stop)//2
        if t[midpoint] == v:
            found = True
        elif t[midpoint] < v:
            start = midpoint + 1
        else:
            stop = midpoint - 1
    if found:
        return midpoint
        
def interlock_search_2(t):
    for item in t:
        odds, evens = "", ""
        for i in range(len(item)):
            if i % 2 != 0:
                odds += item[i]
            else:
                evens += item[i]
        if bisect(t, odds) and bisect(t, evens):
                print item, evens, odds

def interlock_search_3(t):
    for item in t:
        if len(item) < 3:
            continue    
        zeros, ones, twos = "", "", ""
        for i in range(0,len(item),3):
            zeros += item[i]
        for j in range(1,len(item),3):
            ones += item[j]
        for k in range(2,len(item),3):
            twos += item[k]
        if bisect(t, zeros) and bisect(t, ones) and bisect(t, twos):
            print item, zeros, ones, twos

t=[]
fin = open("words.txt")
for line in fin:
    word = line.strip()
    t.append(word)

#interlock_search_2(t)
interlock_search_3(t)

    
    


    