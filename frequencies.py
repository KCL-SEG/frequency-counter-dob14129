"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    keyList = []
    keyFreqs = []
    frequencies = {}

    for item in items:
        found = False
        for i in range(0, len(keyList)):
            if str(item) == str(keyList[i]):
                keyFreqs[i] = keyFreqs[i] + 1
                found = True
        if found == False:
            keyList.append(str(item))
            keyFreqs.append(1)

    for i in range(0, len(keyList)):
        frequencies[str(keyList[i])] = str(keyFreqs[i])

    return frequencies
