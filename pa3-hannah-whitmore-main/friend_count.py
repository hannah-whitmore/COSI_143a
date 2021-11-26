import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)

# Implement the REDUCE function
def reducer(key, values):
    total = 0
    for v in values:
        total += v
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
