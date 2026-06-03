class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings into a single string
        res = ''
        # itirate through the list
        for s in strs:
            # append the len of the s and a '#' before each string
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # decode a single string into a list of strings
        res, i = [] , 0

        # while i is in bounds, itirate char by char
        while i < len(s):
            # initate second pointer j at i to find the delimiter int
            j = i

            # whilst j != '#' we increment it
            while s[j] != '#':
                j +=1
            
            # the int length of the following string starts at i and goes to j (w/o including j)
            Length = int(s[i:j])

            # append the string after j to the result
            res.append(s[j + 1 : j + 1 + Length])

            # update i to start at the next word
            i = j + 1 + Length

        return res