from django.db import models

# Create your models here.
class TeamsRequest(models.Model):
    page = models.IntegerField()
    team = models.CharField(primary_key=True,blank=True,max_length=100)
    class Meta:
        verbose_name_plural = "Equipos"
        ordering = ['team']
    def _str_(self):
            #return '{}:{}'.format(self.imagenRequest.id,self.id)
        return self.team
    
    
class PlayersRequest(models.Model):
    page = models.IntegerField()
    totalPages = models.IntegerField()
    totalResults = models.IntegerField()
    commonName= models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    nation = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True) # club
    #team = models.ManyToManyField(TeamsRequest)
    team = models.ForeignKey(TeamsRequest, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "juagadores"
        ordering = ['commonName']
    def _str_(self):
            #return '{}:{}'.format(self.imagenRequest.id,self.id)
        return self.commonName