#!/usr/bin/env python3
import time

def find_primes_sundaram(upper_bound):
    nums,mid_bound,cur_val = list(range(3, upper_bound+1, 2)),int((upper_bound) / 2),4

    for x in range(3, upper_bound+1, 2):
        for y in range(cur_val, mid_bound, x):
            nums[y-1] = 0
        cur_val += 2*(x+1)

        if cur_val > mid_bound:
            nums.append(2)
            return [x for x in nums if x != 0]

start_time = time.time()    
print(sum(find_primes_sundaram(2000000)))
print(time.time() - start_time)


