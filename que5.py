#creating a telephone number pad using 2D tuples 

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ('*', 0, '#'))  

for rows in num_pad:
    for nums in rows :
        print(nums, end=" ")
    print()    