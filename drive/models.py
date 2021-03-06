
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
import uuid


class User(AbstractUser):
    apodo = models.CharField(max_length=30)
    carpeta_raiz = models.CharField(max_length=250, null=True)
    descripcion = models.TextField(blank = True)
    fecha_nacimiento = models.DateField(null = True, blank = True)
    class Meta:
        unique_together = ['email']
    avatar = models.FileField(upload_to='avatars/',blank=True, null= True)
    
    

#En la variable padres, la gracia es que cada carpeta tiene un padre, y los hijos no es necesario entregarlos
#   ya que con esta implementacion, en la parte de related_name nos permite acceder a los hijos, ejemplo:
#   con miCarpeta.sub_carpeta.all() entregara un queryset, esto en los templates se escribe como {{ miCarpeta.sub_carpeta.all }}
class Carpeta(models.Model):
    class Meta:
        unique_together = ['id','usuario']
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length = 250)
    fecha_creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    padre = models.ForeignKey('self', blank = True, null = True, default=None, on_delete=models.CASCADE)

class Archivo(models.Model):
    class Meta:
        unique_together = ['nombre', 'formato', 'usuario', 'carpeta'] 
    
    nombre = models.CharField(max_length = 250)
    formato = models.CharField(max_length = 250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/', blank=False, null=True)
    fecha_upload = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    carpeta = models.ForeignKey(Carpeta, blank=False, null=True, on_delete=models.CASCADE)
    tags = TaggableManager()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name #name to be shown when called



class Task(models.Model): #drive able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general", on_delete=models.SET_DEFAULT) # a foreignkey
    owner = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"] #ordering by the created field

    def __str__(self):
        return self.title #name to be shown when called