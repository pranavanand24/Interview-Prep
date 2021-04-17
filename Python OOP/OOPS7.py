class Person:
    "This is a Person Class"
    age = 10

    def greet(self):
        print("Hello")


# Output: 10

print(Person.age)

# Output: < function Person.greet>

print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)