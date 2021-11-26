import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    key = record[1]
    mr.emit_intermediate(key, record)


# Implement the REDUCE function
def reducer(key, list_of_values):
    FirstList = list_of_values[0]
    RestOfResults = list_of_values[1:]
    for i in RestOfResults:
        mr.emit(FirstList + i)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
