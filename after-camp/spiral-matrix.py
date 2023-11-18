class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        order = []
        while left < right and top < bottom:
            for col in range(left, right):
                order.append(matrix[top][col])
            top += 1
            for row in range(top, bottom):
                order.append(matrix[row][right-1])
            right -= 1

            if left >= right or top >= bottom:
                break

            for col in range(right-1, left-1, -1):
                order.append(matrix[bottom-1][col])
            bottom -= 1
            for row in range(bottom-1, top-1, -1):
                order.append(matrix[row][left])
            left += 1
        return order



















        # order = []
        # dir = 'E'
        # while left != right != bleft != bright:
        #     if dir == 'E':
        #         temp = left
        #         while temp != right:
        #             order.append(matrix[temp[0]][temp[1]])
        #             temp[1] += 1
        #         left[0] += 1
        #         right[0] += 1
        #         dir = 'S'
        #     elif dir == 'S':
        #         temp = right
        #         while temp != bright:
        #             order.append(matrix[temp[0]][temp[1]])
        #             temp[0] += 1
        #         right[1] -= 1
        #         bright[1] -= 1
        #         dir = 'W'
        #     elif dir == 'W':
        #         temp = bright
        #         while temp != bleft:
        #             order.append(matrix[temp[0]][temp[1]])
        #             temp[1] -= 1
        #         bright[0] -= 1
        #         bleft[0] -= 1
        #         dir = 'N'
        #     else:
        #         temp = bleft
        #         while bleft != left:
        #             order.append(matrix[temp[0][temp[1]]])
        #             temp[0] -= 1
        #         bleft[1] += 1
        #         left[1] += 1
        #         dir = 'E'
        # return order


