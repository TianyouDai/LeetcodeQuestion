def canConstruct(ransomNote, magazine):
    for i in ransomNote:
        if ransomNote.count(i) > magazine.count(i) or i not in magazine:
            return False
    return True
        
