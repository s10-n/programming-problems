def same_necklace(necklace1, necklace2):
    if necklace1 == necklace2:
        return True
    elif len(necklace1) != len(necklace2):
        return False
    else:
        for i in range(len(necklace2)):
            if necklace1 == necklace2[i:] + necklace2[:i]:
                return True
        return False

print(same_necklace("nicole", "icolen"))  
print(same_necklace("nicole", "lenico"))  
print(same_necklace("nicole", "coneli")) 
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))  
print(same_necklace("abc", "cba")) 
print(same_necklace("xxyyy", "xxxyy")) 
print(same_necklace("xyxxz", "xxyxz")) 
print(same_necklace("x", "x"))  
print(same_necklace("x", "xx")) 
print(same_necklace("x", "")) 
print(same_necklace("", ""))                
