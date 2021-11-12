from collections.abc import Hashable


# create your dictionary here
objects_dict = {o: hash(o) for o in objects if isinstance(o, Hashable)}
