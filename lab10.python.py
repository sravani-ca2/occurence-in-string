def removeDupWithoutOrder(str):
    
    

    
    return "".join(set(str)) 
  
 
 
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str)) 
  
 
if __name__ == "__main__": 
    str = "geeksforgeeks"
    print ("Without Order = ",removeDupWithoutOrder(str)) 
    print ("With Order = ",removeDupWithOrder(str))
