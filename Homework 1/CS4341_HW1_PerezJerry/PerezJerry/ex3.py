import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')
    # Your code here
    words = set() #this is initially empty but we will add to it once we clean up our file
    with open(fname) as targetFile:
        for line in targetFile: #for every line in our target file
            replacetheUgly = regex.sub(" ", line) #replace ugly stuff to an empty space
            replacetheUgly = replacetheUgly.lower() #bring all uppers to lower
            splitThem = replacetheUgly.split() #convert them to a list
            for splits in splitThem: #for every split word in our plit list
                words.add(splits) # add the splits to our set of words
        return words;
def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()
    wordset1 = wordset(fname1) #create a new wordset for the first file name
    wordset2 = wordset(fname2) # create another wordset for the other file name
    union = wordset1 | wordset2 #union = OR
    intersection = wordset1 & wordset2 # intersection = AND
    return len(intersection)/len(union); #formula says the cardinality or length of the intersection of both sets divided by the cardinality or length of the union of both sets


