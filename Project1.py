'''
Rent Calculator
User inputs Required :
1. Room Rent
2. Food Cost
3. Electricity Unit Used this Month
4. Charged Cost per unit
5. Number of people in a Room
'''
room_rent=int(input("Room rent ="))
food_cost=int(input("Food cost ="))
electricity_unit=int(input("Electricity Unit Used This month ="))
cost_per_unit=int(input("Charged per unit ="))
number_of_people=int(input("Number of people in roon ="))

Total_bill = electricity_unit * cost_per_unit
Output = (Total_bill + room_rent + food_cost) // number_of_people

print("Cost Each Person have to Pay is =",Output)