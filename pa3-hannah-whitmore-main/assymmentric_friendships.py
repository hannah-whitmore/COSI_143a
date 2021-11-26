import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    personA = record[0]
    personB = record[1]
    personBA = tuple([personB, personA])
    pair = tuple(sorted(record))
    mr.emit_intermediate(pair , personBA)

# Implement the REDUCE function
def reducer(pair, list_of_values):
    if len(list_of_values) == 1:
        mr.emit(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
