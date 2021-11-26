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
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

# Implement the REDUCE function
def reducer(order_id, records):
    records = list(records)
    order_tuples = [record for record in records if record[0]=="order"]
    line_item_tuples = [record for record in records if record[0]=="line_item"]
    join_result = []
    for r1 in order_tuples:
        for r2 in line_item_tuples:
            mr.emit((r1+r2))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
