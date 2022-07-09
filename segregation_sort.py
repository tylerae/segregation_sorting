# 1. Name:
#      -Tyler Elms-
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


test = [31 , 72 , 10 , 32 , 18 , 95 , 25 , 50]

def i_down(test): 
    length = len(test) + 1 
    half = int(length / 2) - 1

    for i in range(0, half):
        if test[i] > test[half]:
            position_down = i
            break

    for i in range(half, length):
        if test[i] < test[half]:
            position_up = i
            break
        
    test[position_down] , test[position_up] = test[position_up] , test[position_down]

    return test


round1 = i_down(test)

    




        
