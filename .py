NO_OF_CHARS = 256

def max_distinct_char(str, n): 
  
    # Initialize all character's 
    # count with 0 
    count = [0] * NO_OF_CHARS 
      
    # Increase the count in array  
    # if a character is found 
    for i in range(n): 
        count[ord(str[i])] += 1
      
    max_distinct = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] != 0): 
            max_distinct += 1    
      
    return max_distinct 
  
def smallesteSubstr_maxDistictChar(str): 
  
    n = len(str)
    max_distinct = max_distinct_char(str, n) 
    minl = n     # result 
      
    # Brute force approach to 
    # find all substrings 
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = max_distinct_char(subs,  
                                                  subs_lenght) 
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 
  
if _name_ == "_main_": 
      
    str = input()
      
    l = smallesteSubstr_maxDistictChar(str); 
    print(l)