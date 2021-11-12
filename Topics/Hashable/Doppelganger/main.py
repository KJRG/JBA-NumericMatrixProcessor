from collections.abc import Hashable


# the object_list has already been defined
# write your code here
hash_occurrences = dict()
for obj in object_list:
    if isinstance(obj, Hashable):
        obj_hash = hash(obj)
        num_occurrences = hash_occurrences.get(obj_hash, 0)
        hash_occurrences[obj_hash] = num_occurrences + 1
result = sum(o for o in hash_occurrences.values() if o > 1)
print(result)
