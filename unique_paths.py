def uniquePaths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Create paths as two dimensional array to represent rows and cols 
        #paths is defined as a list containing a list
        paths = [[0 for x in range(n)] for y in range(m)]
        #path at index 0 and 0 is set equal to 1 
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    continue
                paths[i][j] = paths[i -1][j] + paths[i][j-1]
                print("value at position [2][0]", paths[1][0])
        return paths[m-1][n-1]
    
result = uniquePaths(3,7)
print(result)
