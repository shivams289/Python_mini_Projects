import heapq as hq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dic = dict()
        for word in words:
            if word in dic:
                dic[word] += 1

            else:
                dic[word] = 1

        return hq.nsmallest(
            k, dic, key=lambda word: (~dic[word], word)
        )  # sort in descending order of word frequencies
