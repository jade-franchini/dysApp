from django.contrib import admin
from .models import Lesson, Parent, Enfant, Exercice, Phrase, Option, Recompense, Reponse, Lecture, Orthographe, LectureRapide, Memoire, MathsCalcul, MathsCompter, Resultat

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Parent)
admin.site.register(Enfant)
admin.site.register(Exercice)
admin.site.register(Phrase)
admin.site.register(Option)
admin.site.register(Reponse)
admin.site.register(Lecture)
admin.site.register(Orthographe)
admin.site.register(LectureRapide)
admin.site.register(Recompense)
admin.site.register(Memoire)
admin.site.register(MathsCompter)
admin.site.register(MathsCalcul)
admin.site.register(Resultat)
