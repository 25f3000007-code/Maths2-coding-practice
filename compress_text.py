string = input("Input:\n")
shorten_string = ""
current_char = string[0]
current_count = 0
for i in range(0, len(string)):
    if string[i] == current_char:
        current_count += 1
    else:
        shorten_string += current_char + str(current_count)
        current_char = string[i]
        current_count = 1
shorten_string += current_char + str(current_count)

    
        


print(shorten_string)
    
    
#iterating through all the elements in the list of alphabets from left to right    

            
    

