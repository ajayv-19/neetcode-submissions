class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s))+"#"+s
        print(string) 
        return string
    def decode(self, s: str) -> List[str]:
        output_strs = []
        n = ""
        i=0
        while i < len(s):
            if s[i] == "#":
                ind = int(n)
                output_strs.append(s[i+1: i+1+ind])
                i = i+1+ind
                n=""
            else:
                n = n+s[i]
                i=i+1
            print(n,"n")
        return output_strs



        
