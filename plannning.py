#open the file
import numpy as np
with open("module12quizF23.txt", "r") as m:
    my_array = np.array([])
    print(my_array)
    for x, line in enumerate(m):
       my_array = np.append(my_array, int(line))
    my_array = my_array.reshape(100,100)
    sum = 0
    for i in range(5):
        sum += my_array[i,86]
        
    print(np.mean(my_array[5]))
    print(sum)
   


