from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User     #usamos el modelo usuario q trae django
# Create your models here.

class Post(models.Model):
    STATUS_CHOICE = (   #tupla con dos elementos
        ('draft', 'Draft'),     #borrador
        ('published', 'Published'),     #publicado
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   #Relaciona tablas con ForeignKey.  // CASCADE -> borrar registros relacionados en todas las tablas
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:     #inner class, contiene metainformación. Cuando haga consultas use campo publish, con el - le definimos el orden descendiente
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

