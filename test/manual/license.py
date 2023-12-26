from time import time

from ThamesThrive.service.license import License, VALIDATOR

s = time()
print(License.has_service(VALIDATOR))
print(time() - s)
