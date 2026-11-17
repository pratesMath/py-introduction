# importing a built-in module
from math import sqrt

sqrt = sqrt(25)

print(sqrt)

# importing a module
import module_b as module_b
from module_b import double

message = module_b.greeting("Alice")
print(message)

result = double(5)
print(result)