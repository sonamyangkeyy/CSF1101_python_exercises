name = "Sonam yangki"
age  = 21
height = 155
is_student = True
person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)

person_info["blue"]
print(person_info)

try:
    print(person_info["53"])
except KeyError as e:
          print(f"Error: {e}")