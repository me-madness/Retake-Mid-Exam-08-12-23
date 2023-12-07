days = int(input())
budget = float(input())
people = int(input())
price_fuel_for_kilometer = float(input())
food_expenses = float(input())
room_price = float(input())

if people > 10:
    discount = (days*people*room_price) * 0.25
    food_and_accommodation = (days*people*room_price) + (days*food_expenses*people) - discount
else:    
    food_and_accommodation = (days*people*room_price) + (days*food_expenses*people)

for day in range(days):
    current_day = day + 1 
    distance = int(input())
    food_and_accommodation += distance * price_fuel_for_kilometer
    if current_day % 3 == 0:
        food_and_accommodation += food_and_accommodation * 0.4    
    if current_day % 5 == 0:
        food_and_accommodation += food_and_accommodation * 0.4    
    if current_day % 7 == 0:
        food_and_accommodation -= food_and_accommodation / people     


if budget >= food_and_accommodation:
    sum = budget - food_and_accommodation
    print(f"You have reached the destination. You have {sum:.2f}$ budget left.") 
else:
    sum = food_and_accommodation - budget
    print(f"Not enough money to continue the trip. You need {sum:.2f}$ more.")
    
    
    
    
# Input 1

# 7
# 12000
# 5
# 1.5
# 10
# 20
# 512
# 318
# 202
# 154
# 222
# 108
# 123


# Input 2

# 10
# 20500
# 11
# 1.2
# 8
# 13
# 100
# 150
# 500
# 400
# 600
# 130
# 300
# 350
# 200
# 300
