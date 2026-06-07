class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashing = {}
        for s in strs:
            key = self.generate_key(s)
            if key in hashing:
                hashing[key].append(s)
            else:
                hashing[key] = [s]
        output = []
        # for i, v in hashing.items():
        #     output.append(v)
        # return output
        return list(hashing.values())
        
    
    def generate_key(self,string):
            return tuple(sorted(string))

        