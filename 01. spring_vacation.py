days = int(input())
budget = float(input())
people = int(input())
price_fuel_for_kilometer = float(input())
food_expenses = float(input())
room_price = float(input())
food_and_accommodation = (days*people*room_price) + (days*food_expenses*people)
print(food_and_accommodation)

for day in range(days):
    distance = int(input())
    food_and_accommodation += distance * price_fuel_for_kilometer
    if day % 3 == 0:
        food_and_accommodation += food_and_accommodation * 0.4    
    if day % 5 == 0:
        food_and_accommodation += food_and_accommodation * 0.4    
    if day % 7 == 0:
        small_budget = food_and_accommodation / people     

    print(f"{food_and_accommodation:.2f}")
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
