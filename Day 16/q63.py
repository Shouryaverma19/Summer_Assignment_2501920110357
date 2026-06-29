size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    arr.append(int(input(f"Enter element {i}: ")))

target_sum = int(input("Enter target sum: "))
seen_elements = []
pair_found = False

for num in arr:
    complement = target_sum - num
    if complement in seen_elements:
        print(f"Pair found: ({complement}, {num})")
        pair_found = True
        break
    seen_elements.append(num)

if not pair_found:
    print("No pair exists with the given sum.")