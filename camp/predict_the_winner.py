class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        left, right = 0, len(nums) - 1 
        score1 = score2 = 0

        def play(left, right, score1, score2, player1):
            if left > right:
                return score1 >= score2
            else:

                if player1:
                    p1choice1 = play(left + 1, right, score1 + nums[left], score2, not player1)
                    p1choice2 = play(left, right - 1, score1 + nums[right], score2, not player1)
                    return p1choice1 or p1choice2
                else:
                    p2choice1 = play(left + 1, right, score1, score2 + nums[left], not player1)
                    p2choice2 = play(left, right - 1, score1, score2 + nums[right], not player1)
                    return p2choice1 and p2choice2
        
        return play(left, right, score1, score2, True)
