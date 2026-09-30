# LIST

#1

def high_low(marks=[78,92,65,88,92,71,55,88]):
    if not marks:
        return None, None
    high = max(marks)
    low = min(marks)
    return high, low

#2
def marks_avg(marks=[78,92,65,88,92,71,55,88]):
    if not marks:
        return None
    avg = sum(marks) / len(marks)
    return avg

#3
def count_marks_above_80(marks=[78,92,65,88,92,71,55,88]):
    if not marks:
        return 0
    count = sum(1 for mark in marks if mark > 80)
    return count

#4
def remove_duplicates(marks=[78,92,65,88,92,71,55,88]):
    if not marks:
        return []
    unique_marks = list(set(marks))
    return unique_marks

#5
def sort_marks_desc(marks=[78,92,65,88,92,71,55,88]):
    if not marks:
        return []
    sorted_marks = sorted(marks, reverse=True)
    return sorted_marks


# TUPLE

#1
def display_product_name(product=("Laptop", 55000, "Dell")):
    name, price, brand = product
    return f"Product Name: {name}"

#2
def display_product_price(product=("Laptop", 55000, "Dell")):
    name, price, brand = product
    return f"Product Price: {price}"

#3 
def display_product_brand(product=("Laptop", 55000, "Dell")):
    name, price, brand = product
    return f"Product Brand: {brand}"

#4
def try_changing_price(product=("Laptop", 55000, "Dell"), new_price=60000):
    product[1] = new_price  # This will raise an error because tuples are immutable



# SETS

#1
def common_skills(team1={"Python", "SQL", "Excel", "Java"}, team2={"Python", "JavaScript", "SQL", "HTML"}):
    common = team1.intersection(team2)
    return common

#2 
def skill_either_team(team1={"Python", "SQL", "Excel", "Java"}, team2={"Python", "JavaScript", "SQL", "HTML"}):
    either = team1.union(team2)
    return either

#3 
def skill_by_team1_not_team2(team1={"Python", "SQL", "Excel", "Java"}, team2={"Python", "JavaScript", "SQL", "HTML"}):
    only_team1 = team1.difference(team2)
    return only_team1  

#4 
def skill_by_team2_not_team1(team1={"Python", "SQL", "Excel", "Java"}, team2={"Python", "JavaScript", "SQL", "HTML"}):
    only_team2 = team2.difference(team1)
    return only_team2



# DICTIONARY

#1 
def display_all_names(marks={"Aman":85, "Riya":92, "Karan":78, "Neha":95}):
    names = list(marks.keys())
    return names

#2 
def display_all_marks(marks={"Aman":85, "Riya":92, "Karan":78, "Neha":95}):
    marks_list = list(marks.values())
    return marks_list

#3 
def student_with_highest_marks(marks={"Aman":85, "Riya":92, "Karan":78, "Neha":95}):
    if not marks:
        return None
    highest_student = max(marks, key=marks.get)
    return highest_student, marks[highest_student]

#4
def add_new_student(marks={"Aman":85, "Riya":92, "Karan":78, "Neha":95}, name="Vikas", score=88):
    marks[name] = score
    return marks

#5 
def update_student_score(marks={"Aman":85, "Riya":92, "Karan":78, "Neha":95}, name="Karan", new_score=82):
    if name in marks:
        marks[name] = new_score
    return marks



# ARRAY 1 
import numpy as _n_

#1 
def calculate_total_bill(prices=_n_.array([120,250,80,450,150,75])):
    total_bill = _n_.sum(prices)
    return total_bill

#2 
def most_expensive_item(prices=_n_.array([120,250,80,450,150,75])):
    max_price = _n_.max(prices)
    return max_price

#3
def cheapest_item(prices=_n_.array([120,250,80,450,150,75])):
    min_price = _n_.min(prices)
    return min_price

#4 
def count_items_above_threshold(prices=_n_.array([120,250,80,450,150,75]), threshold=200):
    count = len(prices[prices > threshold])
    return count

#5 
def apply_10_percent_discount_on_1000_plus(prices=_n_.array([120,250,80,450,150,75])):
    total_bill = _n_.sum(prices)
    if total_bill>1000:
        discounted_price = total_bill*0.9
    else:
        discounted_price = total_bill
    return discounted_price



# ARRAY 2 

#1 
def count_even(numbers=_n_.array([12, 7, 25, 18, 30, 41, 56, 63, 72, 89])):
    even_count = _n_.sum(numbers % 2 == 0)
    return even_count

#2 
def count_odd(numbers=_n_.array([12, 7, 25, 18, 30, 41, 56, 63, 72, 89])):
    odd_count = _n_.sum(numbers % 2 != 0)
    return odd_count

#3
def display_all_even(numbers=_n_.array([12, 7, 25, 18, 30, 41, 56, 63, 72, 89])):
    even_numbers = numbers[numbers % 2 == 0]
    return even_numbers 

#4 
def display_all_odd(numbers=_n_.array([12, 7, 25, 18, 30, 41, 56, 63, 72, 89])):
    odd_numbers = numbers[numbers % 2 != 0]
    return odd_numbers

#5 
def sum_of_even(numbers=_n_.array([12, 7, 25, 18, 30, 41, 56, 63, 72, 89])):
    even_sum = _n_.sum(numbers[numbers % 2 == 0])
    return even_sum









# RUNS(run all functions here)
print("LIST FUNCTIONS")
print("1. Highest and Lowest Marks:", high_low())
print("2. Average Marks:", marks_avg())
print("3. Count of Marks Above 80:", count_marks_above_80())
print("4. Remove Duplicates:", remove_duplicates())
print("5. Sort Marks Descending:", sort_marks_desc())

print("SET FUNCTIONS")
print("1. Common Skills:", common_skills())
print("2. Skills in Either Team:", skill_either_team())
print("3. Skills in Team 1 but not in Team 2:", skill_by_team1_not_team2())
print("4. Skills in Team 2 but not in Team 1:", skill_by_team2_not_team1())

print("DICTIONARY FUNCTIONS")
print("1. All Names:", display_all_names())
print("2. All Marks:", display_all_marks())
print("3. Student with Highest Marks:", student_with_highest_marks())
print("4. Add New Student:", add_new_student())
print("5. Update Student Score:", update_student_score())

print("ARRAY 1 FUNCTIONS")
print("1. Total Bill:", calculate_total_bill())
print("2. Most Expensive Item:", most_expensive_item())
print("3. Cheapest Item:", cheapest_item())
print("4. Count of Items Above Threshold:", count_items_above_threshold())
print("5. Apply 10% Discount on Items Over 1000:", apply_10_percent_discount_on_1000_plus())

print("ARRAY 2 FUNCTIONS")
print("1. Count of Even Numbers:", count_even())
print("2. Count of Odd Numbers:", count_odd())
print("3. All Even Numbers:", display_all_even())
print("4. All Odd Numbers:", display_all_odd())
print("5. Sum of Even Numbers:", sum_of_even())


print("TUPLE FUNCTIONS")
print("1. Display Product Name:", display_product_name())
print("2. Display Product Price:", display_product_price())
print("3. Display Product Brand:", display_product_brand())
print("4. Try Changing Product Price:", try_changing_price())