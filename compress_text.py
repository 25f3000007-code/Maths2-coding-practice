string = input("Input:\n")
sorted_string = sorted(string)


compressed_text = ""
seen = []

for i in sorted_string:
    if i in seen:
        continue
    seen.append(i)
    count = 0
    for z in sorted_string:
        if i == z:
            count += 1
    compressed_text += i + str(count)
    
    

print(compressed_text)