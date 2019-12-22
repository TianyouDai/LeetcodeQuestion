class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        sum_loc = 0

        for i in range(len(A)):
            if (A[i] % 2 == 0):
                sum_loc += A[i]

        for i in range(len(queries)):
            val = queries[i][0]
            idx = queries[i][1]

            if A[idx] % 2 == 0:
                sum_loc -= A[queries[i][1]]

            A[idx] += val

            if A[idx] % 2 == 0:
                sum_loc += A[idx]

            output.append(sum_loc)

        return output
                
