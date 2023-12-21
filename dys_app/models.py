from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE = [
        ('Parent', 'parent'),
        ('Enfant', 'enfant')
    ]

    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50, choices=ROLE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.nom


        
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

from django.db import models

# Exercices en génral (première page)
class Exercice(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()

# contient les phrases à trous (incomplète)
class Phrase(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    texte = models.TextField()

# représente les différentes options parmi lesquelles l'enfant peut choisir pour compléter une phrase. 
# Chaque option a un indicateur pour indiquer si elle est correcte ou non.
class Option(models.Model):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    texte_option = models.CharField(max_length=255)
    est_correcte = models.BooleanField(default=False)

# stocke les réponses fournies par l'enfant pour chaque phrase. 
# Il indique également si la réponse est correcte
class Reponse(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    option_selectionnee = models.ForeignKey(Option, on_delete=models.CASCADE)
    est_correcte = models.BooleanField()












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

class MathsCompter(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.TextField()
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class MathsCalcul(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture

class Resultat(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    résultat = models.SmallIntegerField()
    def __str__(self):
        return self.lecture


class Meta:
    indexes = [
        models.Index(fields=['isbn', 'au_id']),
    ]