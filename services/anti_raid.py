
from collections import deque
import time

joins = deque()

def raid_detected():
    now = time.time()
    while joins and now - joins[0] > 10:
        joins.popleft()

    joins.append(now)

    return len(joins) > 10  # 10 joins in 10 sec = raid
