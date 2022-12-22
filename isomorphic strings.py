"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself."""


s1 = "egg"
t1 = "add"
s2 = "foo"
t2 = "bar"
def isIsomorphic(s, t):
        mapST, mapTS = {},{} #initialising the dict

        for c1, c2 in zip(s,t): #looping both strings at the same time using zip function
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):#if one of the character already exist in dictionary and does not have the same value then return false
                return False
            #else map these character in the dictionary
            mapST[c1] = c2
            mapTS[c2] = c1
        return True #return true if no exception

def isIsomorphic2(s, t):
        d = {} #initialising the dict

        for i in range(len(s)): #looping in range of len of either string as they are of same size
            c1,c2 = s[i], t[i] #initialising the variable
            if c1 not in d: #if c1 does not exist in dict
                if c2 in d.values(): #then check if c2 already exist in dict values or nor if yes then return false
                    return False
                d[c1]=c2 #else add that char in dict
            elif d[c1] != c2: #if that char already exist in dict and does not have the same value as char 2 then return false
                return False
        return True #return true if no exception

solution1 = isIsomorphic(s1, t1)
solution2 = isIsomorphic2(s2, t2)

print(solution1)
print(solution2)