def chain_mult (arr):
    length = len(arr)
    max_mults = [[0 for x in range(length)] for x in range(length)]
                 #set to 0 for multiplying one matrix
    for i in range(1, length):
        max_mults[i][i] = 0
 
    for idx in range(2, length):
        for i in range(1, length-idx+1):
            j = i+idx-1
            max_mults[i][j] = 0
            for k in range(i, j):
 
                #calculate the cost - num scalar multiplications
                cost = max_mults[i][k] + max_mults[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if cost > max_mults[i][j]: #update if worse, because we want worse
                    max_mults[i][j] = cost
 
    return max_mults[1][length-1]


dimensions = [6, 4, 5, 8, 2, 7, 3]
mults = chain_mult(dimensions)
print "Mults: " + str(mults)
