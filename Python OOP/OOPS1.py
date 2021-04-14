class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student()
student1.name = "Harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)

student2 = Student()
student2.name = "Janet"
student2.marks = 30
did_pass = student2.check_pass_fail()
print(did_pass)
