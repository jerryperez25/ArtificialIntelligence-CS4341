def isreverse(s1, s2):
    # Your code here
    if (len(s1) == 0 and len(s2) == 0): # if both lengths are 0 then they are both equal: only thing thats 0 is empty
            return True;
    if len(s1) != len(s2): # if the lengths of 2 words are not equal then there is no way they can be reversals
        return False;
    if s1[0] != s2[-1]: # this is supposed to check the last letter of the second word against the first letter of the first
        return False; # if they are not equal then theres nopossible way they can be reversals
    else:
        return isreverse(s1[1:], s2[:-1]); #recursive call for each individual letter, it'll use from the first letter on with the first word
    # and from the last letter of the second word down to the beginning of it.

