from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(primary_key=True,max_length=5)
    course = models.CharField(max_length=20)
    class Meta:
        db_table = 'course'

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    byu_id = models.CharField(max_length=30)
    byu_name = models.CharField(max_length=100)
    international = models.BooleanField()
    class Meta:
        db_table = 'employee'

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    payrate = models.DecimalField(max_digits=10, decimal_places=2)
    last_increase_date = models.DateField()
    pay_increase = models.DecimalField(max_digits=10, decimal_places=2)
    increase_input_date = models.DateField()
    class Meta:
        db_table = 'payment'

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.RESTRICT)
    semester = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    course = models.ForeignKey(Course,db_column='course_code', to_field='course_code', on_delete=models.RESTRICT)
    position_type = models.CharField(max_length=50)
    hire_date = models.DateField()
    year_in_program = models.CharField(max_length=20)
    pay_grad_tuition = models.BooleanField()
    name_change_complete = models.BooleanField()
    notes = models.CharField(max_length=500)
    terminated = models.BooleanField()
    termination_date = models.DateField()
    qualtrics = models.BooleanField()
    submitted = models.BooleanField()
    submitted_date = models.DateField()
    authorized = models.BooleanField()
    supervisor = models.CharField(max_length=50)
    authorization_to_work_email_sent_date = models.DateField()
    expected_hours_per_week = models.IntegerField()
    class Meta:
        db_table = 'job'