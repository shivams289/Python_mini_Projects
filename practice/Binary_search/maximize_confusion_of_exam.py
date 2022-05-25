class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = dict()
        res = 0
        maxf = 0
        left = 0
        for right in range(len(answerKey)):
            if answerKey[right] in count:
                count[answerKey[right]] += 1

            else:
                count[answerKey[right]] = 1

            maxf = max(maxf, count[answerKey[right]])

            if (right - left + 1) - maxf <= k:
                res = max(res, right - left + 1)
            else:
                count[answerKey[left]] -= 1
                if not count[answerKey[left]]:
                    count.pop(answerKey[left])
                left += 1

        print(count)
        return res
