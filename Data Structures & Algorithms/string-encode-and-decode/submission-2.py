class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings into a single string
        res = ''

        # itirate through the string list
        for s in strs:
            # append the len of s followed by a '#' before each string
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        # decode a single string into a list of strings
        res, i = [], 0

        # while i is in bounds, read/itirate char by char
        while i < len(s):
            # second pointer j used to find the delimiter(int)
            j=i

            # while j != '#' we are going to keep incrementing by one
            while s[j] != '#':
                j += 1

            # the integer of the following string that starts at i and goes to j (but does not include j) is the length
            Length = int(s[i:j])

            # append the entire string that comes after j to the result
            res.append(s[j + 1 : j + 1 + Length])

            # update i to start at the next word
            i = j + 1 + Length
        return res