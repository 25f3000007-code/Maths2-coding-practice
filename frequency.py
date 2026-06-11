1
dataset = input("Enter Number:\n").split(" ")
int_list = []
for element in dataset:
    element = int(element)
    int_list.append(element)
print(int_list)

seen = []
frequency_dictionary = {}
for N in int_list:
    if N in seen:
        continue
    seen.append(N)
    count = 0
    for i in int_list:
        if i == N:
            count = count+1
    print(N, count)
    frequency_dictionary[N] = count
    
print(frequency_dictionary)        
   
def mode(frequency_dictionary):
    max_freq = max(frequency_dictionary.values())
    modes = [k for k, v in frequency_dictionary.items() if v == max_freq]
    return(modes, max_freq)    
print(mode(frequency_dictionary))
