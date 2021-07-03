
def Knapsack(W, weight, value, n):
    
    V = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                V[i][j] = 0
            elif weight[i-1] <= j:
                
                V[i][j] = max(value[i-1] + V[i-1][j-weight[i-1]], V[i-1][j])
                
            else:
                
                V[i][j] = V[i-1][j]
 
    return V[n][W]

value = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(value)
print("The maximum value of items which can be fit into the knapsack is RM"+str(Knapsack(W, weight, value, n)))