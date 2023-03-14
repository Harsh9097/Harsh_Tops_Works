# 1). Write a Python program to check multiple keys exists in a dictionary ?

student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})


# Second type of example :

print("\n")
sports = {"cricket" : 1, "practice" : 2, "play" :3}

print(sports.keys() >= {"cricket", "practice"})
print(sports.keys() >= {"play", "ide"})