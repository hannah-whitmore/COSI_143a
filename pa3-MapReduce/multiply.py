import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    matrix=record[0]
    row=record[1]
    col=record[2]
    value=record[3]
    mr.emit_intermediate(1,(matrix,row,col,value))


# Implement the REDUCE function
def reducer(key, list_of_values):
    matrix_a=[]
    for element in list_of_values:
        if element[0]=="a":
            matrix_a.append(element)
    matrix_b=[]
    for element in list_of_values:
        if element[0]=="b":
            matrix_b.append(element)

    ## size of final matrix
    result_rows = max(x[1] for x in matrix_a)+1
    result_cols = max(x[2] for x in matrix_b)+1

    ## add data
    for i in range(result_rows):
        for j in range(result_cols):
            product=0
            for k in range(result_cols):
                for l in range(len(matrix_a)):
                    for m in range(len(matrix_b)):
                        if matrix_a[l][1]==i and matrix_a[l][2]==k and matrix_b[m][1]==k and matrix_b[m][2]==j:
                            product += matrix_a[l][3]*matrix_b[m][3]
            mr.emit((i,j,product))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
