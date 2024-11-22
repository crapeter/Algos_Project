#Proposing a dynamic programming solution

"""In order to obtain the maximum enjoyment points while keeping up with the weight constraint of 20,
we can use the idea of 0/1 knapsack. 0/1 knapsack simply means the objects we choose are 
indivisible, we either choose it or we don't. We create a 0/1 knapsack table and start filling it based on certain 
criteria.
The dimension of the knapsack matrix will be N X W, where N is the number of objects we have, 
and W is the maximum weight capacity. HOWEVER, I have created a (N + 1) X (W + 1) because I want to address
each object number as it's corresponding index. For example, object 1 will have index 1, not index 0. So to address
this, both the values and weights array start with a 0. In addition, the entire first row of the knapsack matrix
is filled with 0's.

KNAPSACK TABLE FILLING CRITERIA
----> We will be creating a nested for loop where the outer loop iterator is 'i', and the inner loop iterator is 'w'.
So, if i == 0 or w == 0, then we set knapsack[i][w] to 0. This way, the entire first row and the first element of the 
second row is set to 0.
----> Then comes the main condition. If the value of iterator 'w' (current) is greater than weights[i], then we find
the maximum between knapsack[i-1][w] and knapsack[i-1][w-weights[i]] + values[i]. Here,
weights[i]: The weight associated with the current object we are dealing with.
knapsack[i-1][w]: This is the value we have obtained in the row right above the current value, or in other words,
the maximum value we obtained considering the previous objects while satisfying the weight capacity.
values[i]: The value (enjoyment points) associated with the current object (experience).
----> Finally, the last condition (else) is just if the value of iterator 'w' is lesser than weights[i]. In this 
case we just have set the current value to the value that is just above it from the previous row. This is because
we have we don't have enough capacity / weight at the moment to fill the 'knapsack' with any other object.

TIME COMPLEXITY: O(N * W)
SPACE COMPLEXITY: O(N * W)
These would likely approximate to O(n^2), which means it runs in quadratic time.
"""

#   CODE IMPLEMENTATION

# Initializing Experience weights and values
weights = [0,8,7,6,5,4] # Including a dummy 0 to match 1-based indexing
values = [0,1500,1600,1700,1800,3000] # Including a dummy 0 to match 1-based indexing
weight_capacity = 20 # The maximum weight the "knapsack" can hold

n = len(weights) # The length of the weights array / list

# Initialize the DP knapsack table
# (n+1) x (weight_capacity+1) for clarity and 1-based indexing

# Initializing the 2D knapsack table. 
# Initially, it's filled with 0's.
knapsack = [[0] * (weight_capacity + 1) for x in range(n)] 

def maximizeExperience():
    # Creating loops to fill up the DP knapsack table
    for i in range(n): # Looping through the experiences (objects)
        for w in range(weight_capacity + 1): # Looping through all the possible weights
            if weights[i] <= w:
                # Here we decide whether we want to include the current item or not
                knapsack[i][w] = max(knapsack[i-1][w], knapsack[i-1][w-weights[i]] + values[i])
            else:
                # This condition occurs when we don't have enough capacity to include the current item
                knapsack[i][w] = knapsack[i-1][w]

    max_enjoyment = knapsack[n-1][weight_capacity] # This gives us the maximum enjoyable points
    selected_experiences = [] # This array will contain the experiences that lead to the maximum enjoyable points

    for i in range(n-1, 0, -1): # 'Backtracking' or looping backwards to obtain the experiences that we included
        """If this condition passes, it means that we actually included this object. That's why knapsack[i][w]
        is NOT EQUAL to knapsack[i-1][w], i.e. the value directly above our current value."""
        if knapsack[i][w] != knapsack[i-1][w]:
            selected_experiences.append(i)
            w -= weights[i]
        else:
            continue
    
    return max_enjoyment, selected_experiences # Returning our values of interest

max_enjoyment, experiences = maximizeExperience()

print("The maximum number of enjoyment points within the weight limit : {}".format(max_enjoyment))

for i in range(len(experiences) - 1, -1, -1):
    print("Experience {} (Weight: {}, Value: {}) was selected!"
    .format(experiences[i], weights[experiences[i]], values[experiences[i]]))
