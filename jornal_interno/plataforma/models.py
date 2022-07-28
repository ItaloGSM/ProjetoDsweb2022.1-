from django.db import models
from django.contrib.auth.models import User


class Colunista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Colunistas'

    def __str__(self):
        return f"Nome: {self.user.username} - CPF: {self.cpf} "    

class Edicao(models.Model):
    colunista = models.ForeignKey(Colunista, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Edições'

    def __str__(self):
            return ("{0} - {1}").format(self.id, self.texto)

class Noticia(models.Model):
    colunista = models.ForeignKey(Colunista, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Noticias'

    def __str__(self):
            return ("{0} - {1}").format(self.edicao.texto, self.texto)

class Comentario(models.Model):
    colunista = models.ForeignKey(Colunista, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comentarios'  

    def __str__(self):
            return ("{0} - {1}").format(self.noticia.texto, self.texto)   
