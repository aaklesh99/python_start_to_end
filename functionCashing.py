import time
from functools import lru_cache

# @lru_cache(maxsize=3)
# def delay(n):
#     time.sleep(n)
#     return n
#
# if __name__=='__main__':
#     print("Loading...")
#     delay(3)
#     print("Hello Akki")
#     delay(3)
#     print(("How are you?"))

# def handle(n):
#     lru_cache(maxsize=n)
n = int(input())
@lru_cache(maxsize=n)
def delay(b):
    time.sleep(b)
    return b




if __name__ == '__main__':
    print("Loading...")
    delay(3)
    print("Hello Akki")
    delay(3)
    print(("How are you?"))


