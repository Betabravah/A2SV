class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        for idx, box in enumerate(boxes):
            if box == '1':
                ones.append(idx)

        operations = []
        for i in range(len(boxes)):
            op = 0
            for one in ones:
                op += abs(i - one)

            operations.append(op)

        return operations
