import random


def find_neighbors(value, row, column):

    # βρίσκω τα στοιχεία αριστερα δεξια πανω κατω
    # αν υπάρχουν, και η τιμή τους είναι μικρότερη, τα αποθηκεύω τοπικά σε μια λίστα με tuples (τιμή , γραμμή, στήλη) την οποία επιστρέφω    

    neighbors = []

    # αριστερά
    if column > 0 and matrix[row][column-1] > value:
        neighbors.append((matrix[row][column-1], row, column-1))

    # δεξιά
    if column < len(matrix[0])-1 and matrix[row][column+1] > value:
        neighbors.append((matrix[row][column+1], row, column+1))

    # πάνω
    if row > 0 and matrix[row-1][column] > value:
        neighbors.append((matrix[row-1][column], row-1, column))

    # κάτω
    if row < len(matrix)-1 and matrix[row+1][column] > value:
        neighbors.append((matrix[row+1][column], row+1, column))

    return neighbors



def find_longest_path(value, row, column):
  
    # βρισκω τους γείτονες
    neighbors = find_neighbors(value, row, column)
    
    # αν δεν εχω γείτονες, τελειώνει το path εδώ
    if not neighbors:
        return 0
    
    # για κάθε γείτονα, βρίσκω το μήκος του μεγαλύτερου path αναδρομικά και επιστρέφω το μεγαλύτερο από αυτά
    longest_path = 0

    for nvalue, nrow, ncolumn in neighbors:
        path_from_neighbor = 1 
        path_from_neighbor += find_longest_path(nvalue, nrow, ncolumn)
        longest_path = max(longest_path, path_from_neighbor)

    return longest_path



#######################
#### MAIN PROGRAM #####
#######################

m = random.randint(2, 9)
n = random.randint(2, 9)

matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]

print(f"Μέγεθος: {m}x{n}")
for row in matrix:
    print(row)

paths = [] # περιέχει τα longest paths που ξεκινούν από κάθε στοιχείο του πίνακα

for row in range(0,m):
    for column in range(0,n):

        element_paths = find_longest_path(matrix[row][column],row,column)
        paths.append(element_paths)

        
max_path_length = max(paths)
print("Μήκος μεγαλύτερου μονοπατιού:", max_path_length)

