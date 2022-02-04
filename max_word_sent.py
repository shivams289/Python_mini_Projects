class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        largest = len(sentences[0].split())
        for sent in sentences:
            if len(sent.split()) > largest:
                largest = len(sent.split())
                
        return largest
    
    #2nd way 
        #return max([len(sent.split()) for sent in sentences])
        
        