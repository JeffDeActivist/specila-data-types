d1 = {"name": "JeffDeActivist",
      "age": 18}
print(d1)
d1.pop("age")
print(d1)
d1.clear()
print(d1)
print(" length is", len(d1))
print("keys are", d1.keys())
print("values are", d1.values())
print("items are", d1.items())
print("age is", d1.get("age"))
# print("default is", d1.setdefault("default", "Empty"))
d1["course"] = "MCS"  # adding a value to a dict
d1["age"] = 18.8  # change value in a dict

print(d1["age"])  # to search a vlaue using the index
print(d1.get("school", "TTU"))  # returns the default TTU since no key called "schhol" exists
for key, value in d1.items():
    print(key, "is", value)
from collections import defaultdict
d1 = defaultdict(lambda: "Key does not exist")
print(d1["keyErrorTry"])  # will return the defaultdict value set
d2 = {"grade": "B+"}
from collections import ChainMap
d1 = ChainMap(d1, d2)  # to merge dictionaries
print(d1)
print(sorted(d1.items()))  # sorts the items
from lists import l1
print(sorted(l1))
""" creating an ordered dict"""
from collections import OrderedDict
d3 = OrderedDict()
d3[1] = "name"
d3[2] = "age"
d3[3] = "level of education"
d3[4] = "Current job",
print(d3.items())
print("My name is", d1["name"].upper(), "and am", d1["age"], "years old")

