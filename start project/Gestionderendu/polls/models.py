
import datetime

from django.db import models

class Eleve(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=200, default = "")


class Event(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField(max_length=200, default = "")
    Date = models.DateTimeField(auto_now_add=False, null = True)
    
    
class Cour(models.Model):
    def __str__(self):
        return self.Cours
    Cours = models.CharField(max_length=200)
    Année = models.DateField(auto_now_add=False)
    Eleves = models.ManyToManyField(Eleve, related_name = "Cour")


class Projet(models.Model):
    def __str__(self):
        return self.Name_of_student
        return self.Title_of_the_project
    Name_of_student = models.CharField(max_length=200)
    Title_of_the_project = models.CharField(max_length=200, default = "")
    Coeficients = models.CharField(max_length=200)
    Deadline = models.DateTimeField(auto_now_add=False )



class Prof(models.Model):
    def __str__(self):
        return self.Name_of_the_prof
    Name_of_the_prof = models.CharField(max_length=200)

    


