

def purify( email):
        
    email_parts=email.rsplit("@") #separate before and after at 
    plus_idx = email_parts[0].find("+")
    
    
    local = (email_parts[0])[:plus_idx] if plus_idx != -1 else email_parts[0]
    local =local.split(".")
    local = "".join(local) 
    
    return local + "@"+ email_parts[1]
        
    
def numUniqueEmails( emails):
    
    emails = { purify(email)  for email in emails }
    
    
    return len(emails)





def main():
   
   import itertools
   tree=[1,1,1,2,2,1,1,3,3]
   blocks = [(k, len(list(v)))for k, v in itertools.groupby(tree)]

    print (blocks)




if __name__ == '__main__' :
    main()