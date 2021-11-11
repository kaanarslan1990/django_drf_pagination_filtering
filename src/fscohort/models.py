from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=30)

    def __str__ (self):
        # return f'{self.first_name} {self.last_name}'
        return self.title

    # def student_count(self):
    #     return self.student_set.all().count()

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    
    
    def __str__ (self):
        # return f'{self.first_name} {self.last_name}'
        return self.first_name
    
    
    
