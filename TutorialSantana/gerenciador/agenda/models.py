from django.db import models

from django.contrib.auth.models import User

class ItemAgenda(models.Model):
	titulo = models.CharField(max_length=100)
	data = models.DateField()
	hora = models.TimeField()
	descricao = models.TextField()
	usuario = models.ForeignKey(User)
	participantes = models.ManyToManyField(User, related_name="item_participantes")

	def __unicode__(self):
		return u"%s - %s %s" % (self.titulo, self.data, self.hora)
