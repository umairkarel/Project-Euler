from itertools import permutations
from itertools import islice
temp = (islice(permutations('0123456789'), 999999, None))
print("".join(str(x) for x in next(temp)))