class Solution:
    """
    My brute force approach
    """
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t) :
            return False
        else:
            letters_set= {}
            
            for i in range(len(s)):
                if s[i] in letters_set:
                    letters_set[s[i]] +=1
                else:
                    letters_set[s[i]] = 1
                    
            print (letters_set)         
            letters_set2= {}
            
            for i in range(len(t)):
                if t[i] in letters_set2:
                    letters_set2[t[i]] +=1
                else:
                    letters_set2[t[i]] = 1
            
            print (letters_set2)    
                    
            
            for key ,value  in letters_set2.items() :
                
                
                if key in letters_set and  value == letters_set[key]:
                    pass
                else:
          
                    return False
                


            return True

        
        
        # Optimized Solution 
        
        class Solution:
            """
            Optimal Solution 
            """
            def isAnagram(self, s: str, t: str) -> bool:
                if len(s)==len(t):
                    for char in set(s):  # Beutiful way to cast string into set 
                        if s.count(char)!=t.count(char): # nice way count number of char in str
                            return False
                    return True
                else:
                    return False
                
        
        