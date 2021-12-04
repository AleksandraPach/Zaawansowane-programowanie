class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student("Lusia", 60)
student2 = Student("Zosia", 10)
print(student1.is_passed())
print(student2.is_passed())
