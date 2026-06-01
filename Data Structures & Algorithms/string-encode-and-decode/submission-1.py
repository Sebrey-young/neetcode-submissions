class Solution:

    def encode(self, strs: List[str]) -> str:
        # we are going to encode a list of strings into a SINGLE string
        res = ''
        # for every string in the string list
        for s in strs:
            # append the length of the string followed by a '#' char before each string
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # decode a single string (above) into a List of strings
        res, i = [], 0

        # while i is in bounds, read/itirate char by char
        while i < len(s):
            # a second pointer j is used to find the delimiter (the integer char)
            j = i
            # while j is not a '#' char we are going to keep incrementing by one
            while s[j] != '#':
                j += 1

            # the length/integer of the following string starts at i and goes to j (does not include j)
            length = int(s[i:j])

            # append the entire string following j to the result
            res.append(s[j + 1: j + 1 + length])
            
            # updates i to start at the next word
            i = j + 1 + length
        return res
