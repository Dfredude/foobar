

# def solution(start, length):
#     xor = 0

#     i = start
#     step = 0
#     print("Starting...")
#     while length > 0:
#         end = i+length
#         for j in range(i, end):
#             print(j)
#             xor ^= j
#             print("XOR: ", xor)
#         i = end+step
#         length-=1
#         step+=1
#     return xor

def solution(start, length):
    xor = 0
    print("  i","Input", "operator", "XOR", sep=' | ')
    print("--------------------------------")
    i = 0
    for j in range(start, start+length):
        prev = xor
        xor ^= j
        i+=1
        print(f"{i:3} | {prev:^5} | {j:^8} | {xor:^5}")
    return xor


print(solution(17, 20))