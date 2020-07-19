from django.db import models

class College(models.Model):
    college_name = models.CharField(max_length=150)
    college_short = models.CharField(max_length=10)

class Department(models.Model):
    department_name = models.CharField(max_length=150)
    department_short = models.CharField(max_length=10)

class Courses(models.Model):
    course_name = models.CharField(max_length=150)
    course_name1 = models.CharField(max_length=10)

class Students(models.Model):
    M = 'MALE'
    F =  'FEMALE'
    SEX = (
        (M, 'Male'),
        (F, 'Female'),
    )

    REG = 'REGULAR'
    IREG = 'IRREBULAR'
    OS = 'OVER STAYING'
    OTHERS = 'OTHERS'
    STATUS = (
        (REG, 'Regular'),
        (IREG, 'Irregualr'),
        (OS, 'Over Staying'),
        (OTHERS, 'Others')
    )

    student_no  = models.CharField(max_length=11)
    qr_code = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    name_ext    = models.CharField(max_length=3, default="")
    gender      = models.CharField(max_length=10, choices=SEX)
    status      = models.CharField(max_length=15, choices=STATUS)
    course      = models.ForeignKey(Courses, related_name='student_course', on_delete=models.CASCADE)

class Prospectus(models.Model):
    prospectus_name = models.CharField(max_length=250)
    prospectus_note = models.CharField(max_length=250)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='procourses')

class Levels(models.Model):
    FIRST = '1ST SEMESTER'
    SECOND = '2ND SEMESTER'
    SUMMER = 'SUMMER'
    SEMESTER = (
        (FIRST, "1st Sem"),
        (SECOND, "2nd Sem"),
        (SUMMER, "Summer")
    )
    level_no = models.IntegerField()
    level_name = models.CharField(max_length=50)
    level_semester = models.CharField(max_length=50, choices=SEMESTER)
    level_note = models.CharField(max_length=250)

class Subjects(models.Model):
    subject_no = models.CharField(max_length=50)
    descriptive_title = models.CharField(max_length=250)
    lecture = models.FloatField()
    laboratory = models.FloatField()
    credit = models.FloatField()
    pre1 = models.CharField(max_length=50)
    pre2 = models.CharField(max_length=50)
    pre3 = models.CharField(max_length=50)

class ProSubects(models.Model):
    subject = models.ForeignKey(Subjects, related_name="prosubjects", on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, related_name="prolevels", on_delete=models.CASCADE)
