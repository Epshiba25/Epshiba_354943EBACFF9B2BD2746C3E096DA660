class Student:
  def __init__(self, name, rollno, cgpa):
      self.name = name
      self.rollno = rollno
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

if __name__ == "__main__":
  stu1 = [Student("anu", 101, 5), Student("aruna", 102, 7), Student("anju", 103, 8)]
  sorted_stu1 = sort_students(stu1)
  print("sort_students(list 1):")
  for student in sorted_stu1:
      print(f"{student.name}_rollno:{student.rollno}, cgpa:{student.cgpa}")
