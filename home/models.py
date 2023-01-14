from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name=models.CharField(max_length=200, null=True,blank=True)
    department_description=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return self.dept_name
    


class Doctors(models.Model):
    doc_name=models.CharField(max_length=200, null=True,blank=True)
    doc_spec=models.CharField(max_length=200, null=True,blank=True)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors',null=True, blank=True)
    def __str__(self):
        return self.doc_name




class Booking(models.Model):
    p_name=models.CharField(max_length=200, null=True,blank=True)
    p_phone=models.CharField(max_length=200, null=True,blank=True)
    p_email=models.EmailField(null=True,blank=True)
    doc_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

