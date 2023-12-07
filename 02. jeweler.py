white_gold = input().split(" ")
yellow_gold = input().split(" ")
earrings = 0
left_gold = 0
for i in range(len(white_gold)):
    a = int(white_gold[i])
    b = int(yellow_gold[i])
    sum = a + b
    if sum < 10:
        left_gold += sum
    elif sum > 10:
        sum -= 2
        if sum % 10 == 0:
            earrings += 1
            if sum > 10:
                sum -= 2
                if sum % 10 == 0:
                    earrings += 1
            else:
                left_gold += sum
    else:
        earrings +=1            
                
if left_gold > 10:
    left_sum = left_gold // 2
    earrings += left_sum
    
if earrings >= 7:       
    print(f"Great success, you created {earrings} earrings.") 
else:
    new_sum = 7 - earrings
    print(f"Keep trying, you need {new_sum} more earrings.")
                                        
print(white_gold)
print(yellow_gold)

# Input 1

# 2 7 8 5 1 6 1 7 5
# 8 3 2 7 9 4 9 2 3


# Input 2

# 5 3 2 2 4
# 5 5 8 2 6