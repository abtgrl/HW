import functools

# task 1

students_list = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 19, "grades": [75, 82, 79, 88]},
    {"name": "Emily", "age": 20, "grades": [90, 92, 87, 89]},
    {"name": "Frank", "age": 22, "grades": [84, 79, 91, 88]},
    {"name": "Grace", "age": 21, "grades": [91, 85, 90, 86]},
    {"name": "Henry", "age": 19, "grades": [87, 88, 91, 92]},
    {"name": "Ivy", "age": 20, "grades": [82, 88, 90, 86]},
    {"name": "Jack", "age": 22, "grades": [90, 91, 89, 87]},
    {"name": "Katie", "age": 21, "grades": [85, 84, 92, 91]},
    {"name": "Liam", "age": 19, "grades": [88, 87, 83, 91]},
    {"name": "Mia", "age": 20, "grades": [93, 88, 90, 89]},
    {"name": "Noah", "age": 22, "grades": [86, 89, 91, 87]},
    {"name": "Olivia", "age": 21, "grades": [90, 92, 88, 87]},
    {"name": "Parker", "age": 23, "grades": [89, 91, 85, 88]},
    {"name": "Quinn", "age": 20, "grades": [87, 90, 92, 84]},
    {"name": "Ryan", "age": 22, "grades": [94, 88, 95, 92]},
    {"name": "Sophia", "age": 21, "grades": [88, 87, 89, 91]},
    {"name": "Thomas", "age": 19, "grades": [90, 92, 88, 89]},
]


def filter_students(students, age=None, grade=None):
    if not age and not grade:
        return 0
    if age:
        return list(filter(lambda student: student["age"] == age, students))
    else:
        return list(filter(lambda student: (all(student_grade > grade for student_grade in student["grades"])), students))


def student_average(student):
    grades = student["grades"]
    average_grade = sum(grades) / len(grades)
    return {"name": student["name"], "age": student["age"], "average_grade": average_grade}


def student_average_list(students):
    return list(map(student_average, students))


def overall_average(students):

    all_grades = functools.reduce(lambda x, student: x + sum(student["grades"]), students, 0)
    return functools.reduce(lambda x, student: x + student["average_grade"], student_average_list(students), 0) \
           / len(students) if len(students) > 0 else 0


def top_students(students):
    max_average = max(students, key=lambda student: sum(student["grades"]) / len(student["grades"]))
    return [student for student in students if sum(student["grades"]) / len(student["grades"])
            == sum(max_average["grades"]) / len(max_average["grades"])]


print("TASK 1\n")
print("Students who are 20 years old:", filter_students(students_list, age=20))
print("Students with certain grades: ", filter_students(students_list, grade=85))
print("Average score of each student: ", student_average_list(students_list))
print("Overall average score: ", overall_average(students_list))
print("Students with maximum score: ", top_students(students_list))

# task 2

users_list = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [350, 610, 80, 290]},
    {"name": "Charlie", "expenses": [120, 460, 270, 220]},
    {"name": "David", "expenses": [190, 340, 65, 80]},
    {"name": "Emily", "expenses": [510, 355, 75, 110]},
    {"name": "Frank", "expenses": [240, 465, 85, 200]},
    {"name": "Grace", "expenses": [130, 62, 178, 215]},
    {"name": "Sophia", "expenses": [395, 245, 70, 285]},
    {"name": "Ivy", "expenses": [105, 52, 673, 395]},
    {"name": "Jack", "expenses": [145, 368, 88, 205]},
    {"name": "Katie", "expenses": [425, 358, 177, 95]},
    {"name": "Liam", "expenses": [115, 453, 72, 200]},
    {"name": "Mia", "expenses": [135, 162, 380, 110]},
    {"name": "Noah", "expenses": [125, 557, 276, 190]},
    {"name": "Olivia", "expenses": [615, 55, 174, 205]},
    {"name": "Parker", "expenses": [130, 363, 82, 95]},
    {"name": "Quinn", "expenses": [220, 258, 176, 200]},
    {"name": "Ryan", "expenses": [140, 465, 85, 120]},
    {"name": "Sophia", "expenses": [75, 60, 378, 295]},
    {"name": "Thomas", "expenses": [110, 350, 73, 210]}
]


def filter_users(users, name=None, expense=None):
    if not name and not expense:
        return 0
    elif name:
        return list(filter(lambda user: user["name"] == name, users))
    else:
        return list(filter(lambda user: (all(user_expense > expense for user_expense in user["expenses"])), users))


def user_sum(user):
    expenses = user["expenses"]
    return {"name": user["name"], "total_sum": sum(expenses)}


def user_sum_list(users):
    return list(map(user_sum, users))


def total_sum(users, name=None, expense=None):
    if not name and not expense:
        return 0
    elif name:
        filtered = filter_users(users, name=name)
    else:
        filtered = filter_users(users, expense=expense)
    return functools.reduce(lambda x, user: x + sum(user["expenses"]), filtered, 0)


print("\nTASK 2\n")
print("Filtered by name: ", filter_users(users_list, name="Sophia"))
print("Total expenses of each user: ", user_sum_list(users_list))
print("Total expenses of all filtered users: ", total_sum(users_list, name="Sophia"))

# task 3

orders_list = [
    {"order_id": 1, "customer_id": 101, "amount": 150},
    {"order_id": 2, "customer_id": 102, "amount": 200},
    {"order_id": 3, "customer_id": 101, "amount": 75},
    {"order_id": 4, "customer_id": 103, "amount": 100},
    {"order_id": 5, "customer_id": 101, "amount": 50},
    {"order_id": 6, "customer_id": 104, "amount": 120},
    {"order_id": 7, "customer_id": 102, "amount": 80},
    {"order_id": 8, "customer_id": 103, "amount": 90},
    {"order_id": 9, "customer_id": 104, "amount": 60},
    {"order_id": 10, "customer_id": 101, "amount": 110},
    {"order_id": 11, "customer_id": 102, "amount": 70},
    {"order_id": 12, "customer_id": 103, "amount": 85},
    {"order_id": 13, "customer_id": 101, "amount": 95},
    {"order_id": 14, "customer_id": 104, "amount": 130},
    {"order_id": 15, "customer_id": 103, "amount": 55},
    {"order_id": 16, "customer_id": 102, "amount": 65},
    {"order_id": 17, "customer_id": 101, "amount": 120},
    {"order_id": 18, "customer_id": 104, "amount": 75},
    {"order_id": 19, "customer_id": 103, "amount": 110},
    {"order_id": 20, "customer_id": 102, "amount": 150}
]


def filter_by_customer(orders, customer_id):
    return list(filter(lambda order: order["customer_id"] == customer_id, orders))


def customer_sum(orders, customer_id):
    return sum(order["amount"] for order in filter_by_customer(orders, customer_id))


def average_customer_sum(orders, customer_id):
    return customer_sum(orders, customer_id) / len(filter_by_customer(orders, customer_id))


print("\nTASK 3\n")
print("Orders of a specific customer: ", filter_by_customer(orders_list, 101))
print("Sum of all customer orders: ", customer_sum(orders_list, 101))
print("Average amount of customer orders: ", average_customer_sum(orders_list, 101))
