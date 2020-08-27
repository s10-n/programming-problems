matrix_structure = [[4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],
                    [4,4,4,4,4,4,4],]

#def number_matrix(n):
 #   matrix=[] # creates blank matrix
    # create an empty matrix of width 2n-1
  #  for y in range ((2*n)-1): 
   ###     matrix.append([])
      #  for x in range ((2*n)-1):
       #     matrix[y].append(n)
#    for i in range (1,n):
 #       for j in range ((n-1) - i):
            
  #      matrix[i][1]
   #     matrix[i][2]
    #    matrix[i][3]
     #   matrix[i][4]
      #  matrix[i][5]


            
    # populate the matrix with numbers
#    matrix[n-1][n-1] = 1
 #   for i in range (1,n):
  #      for y in range (2 + i):
            

###    print(matrix)



def number_matrix(n):
    countdown_set = []
    countdown = []  
    for i in range (n):
        countdown.append(n)
    for i in range (1,n):
        for j in range (i,n):
            countdown[j] = -i + n
        countdown_set.append(countdown)
#    for i in range (1,n):
#        countdown[i] = n - 1
#   for i in range (2,n):
#        countdown[i] = n - 2
#    for i in range (3,n):
#        countdown[i] = n - 3
    print(countdown_set)
    
number_matrix(10)

# create a list of n length

# [[],[],[],[]]

# populate that list with n lists of n length populated with int(n)

# [[4,4,4,4],[4,4,4,4],[4,4,4,4],[4,4,4,4]]

# for lists in range (1,(n-1)), replace the last n-i numbers with n-i

# [[4,4,4,4],[4,3,3,3],[4,3,3,3],[4,3,3,3]]
# [[4,4,4,4],[4,3,3,3],[4,3,2,2],[4,3,2,2]]
# [[4,4,4,4],[4,3,3,3],[4,3,2,2],[4,3,2,1]]

# add each list's reverse[0,-1] to the end of itself

# [[4,4,4,4,4,4,4],
# [4,3,3,3,3,3,4],
# [4,3,2,2,2,3,4],
# [4,3,2,1,2,3,4]]

# add the lists[0,-1] to the master list in reverse order

# [[4,4,4,4,4,4,4],
# [4,3,3,3,3,3,4],
# [4,3,2,2,2,3,4],
# [4,3,2,1,2,3,4],
# [4,3,2,2,2,3,4],
# [4,3,3,3,3,3,4],
# [4,4,4,4,4,4,4]]

