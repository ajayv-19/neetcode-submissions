class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        s2_dict = {}
        window_size = len(s1)
        l = 0
        r = 0
        while r < len(s2):
            s2_dict[s2[r]] = s2_dict.get(s2[r],0) +1
            if r-l+1 > window_size:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l+=1
            if s2_dict == s1_dict:
                return True
            r+=1
        return False




        
        """

        the s1 should be always samller or equal than s2

        approac 1. 
        get all perutation of the s1 and store in list.
        slide strouh the s2 of size s1 and see the particular substring in list

        approacah 2
        store s1 words list in a dict
        slide trough the s2 of size s1 and keep track of the elemnet in dict (every move drop left and update right)
        see the both dict are equal or not



        " 

        In the approach add in the strings - when count comparision use dictionary"
        """