"""
Modify the program from section 8.3 to fix the spelling error of "Oack" (should be "Ouack") and "Qack" (should be "Quack")

Here is the original program:

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print letter + suffix
"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print letter + 'u' + suffix
    else:
        print letter + suffix
