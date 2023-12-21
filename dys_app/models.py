from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    SCHOOL_LEVEL_CHOICES = [
        ('CP', 'cp'),
        ('CE1', 'ce1'),
        ('CE2', 'ce2'),
        ('CM1', 'cm1'),
        ('CM2', 'cm2'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    publisher = models.CharField(max_length=255)
    youtube_link = models.URLField()
    school_level = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)

    def __str__(self):
        return self.title

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.user

class Enfant(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    def __str__(self):
        return self.enfant

class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    texte = models.TextField()
    question = models.CharField(max_length=150)
    reponse = models.CharField(max_length=150)
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class Orthographe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    liste = models.TextField()
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class LectureRapide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    texte = models.TextField()
    résultat = models.SmallIntegerField()
    # quantite = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class Recompense(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.TextField()
    def __str__(self):
        return self.lecture

class Memoire(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    liste = models.TextField()
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class Orthographe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    liste = models.TextField()
    mots = models.CharField(max_length=150)
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture
# table user 
class User(models.Model):
    user_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
    surname= models.CharField(max_length=25)
    
# table reservation 
class Reservation(models.Model):
    isbn = models.ForeignKey(Title, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    indexes = [
        models.Index(fields=['isbn', 'au_id']),
    ]