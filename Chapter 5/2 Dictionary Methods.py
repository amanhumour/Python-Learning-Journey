marks = {
    "Aman": 70,
    "Abhishek": 60,
    "Abhishek R": 80
}

print(marks.keys())
print(marks.items())
print(marks.values())
marks.update({"Aman": 75, "Ansh": 0})
print(marks)

print(marks.get("Aman2")) #prints none

print(marks["Aman2"]) #returns a error