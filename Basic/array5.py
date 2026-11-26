class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(index, remaining, path):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            if index == len(candidates):
                return

            # Take current number (reuse allowed)
            path.append(candidates[index])
            backtrack(index, remaining - candidates[index], path)
            path.pop()

            # Skip current number
            backtrack(index + 1, remaining, path)

        backtrack(0, target, [])
        return result