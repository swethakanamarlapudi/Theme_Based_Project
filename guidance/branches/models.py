from django.db import models

class Departments(models.Model):
  department_name=models.CharField(max_length=400)
  deptartment_information=models.CharField(max_length=5000)
  department_coresubject=models.CharField(max_length=1000)
  department_logo=models.CharField(max_length=1000)


  def __str__(self):
   return self.department_name + ' - ' +self.department_coresubject

class companies(models.Model):
  departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
  company_name=models.CharField(max_length=2000)
  company_turnover=models.CharField(max_length=300)
  is_favorite = models.BooleanField(default=False)


  def __str__(self):
   return self.company_name 

class college(models.Model):
  departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
  college_name= models.CharField(max_length=300)
  college_intake=models.CharField(max_length=300)
  college_logo=models.CharField(max_length=1000)







