from functools import reduce

def getXOR(start: int, end: int, nest_level):
    print(nest_level+"XORing:", f"{start} {end}", sep=" ")
    if (end - start) == 0:
        return 0
    if (end - start) == 1:
        return start
    if (end - start) <= 2:
        return reduce(lambda x, y: x ^ y, range(start, end))
    else:
        begin_range = (start, start // 2 * 2 + 2) # Use single slash in Python 2
        end_range = (end // 2 * 2, end) # Again, Python 2 don't have double slash operator
        return getXOR(*begin_range, nest_level+"\t") ^ getXOR(*end_range, nest_level+"\t")

"""First attempt"""
# def solution(start, length):
#     xor = 0
#     reductor = 0 # We reduce 0 on first row
#     while length > 0:
#         end = start+length # Determine end bound
#         # print("XORing:", end=" ")
#         xor ^= reduce(lambda a, b: a ^ b, range(start, end))
#         # for j in range(start, end):
#         #     # print(j, end=" ")
#         #     xor ^= j
#         # print()
#         start=end+reductor # Redfine start bound
#         length-=1 # Reduce length
#         reductor+=1 # Increase reductor
#     return xor

def solution(start, length):
    end = start+length # define end
    row_size = end-start
    lines = [(start+(length-l)*row_size, start+(length-l)*row_size+l) for l in range(length, 0, -1)]
    return reduce(lambda x, y: x ^ y, [getXOR(*line, "") for line in lines])

# print("solution(): ", solution(0, 3))
print("solution(): ", solution(16, 7))
# print("solution(): ", solution(200000, 25000))