from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


GENRES_CHOICES = (
    ('Action' , 'ACTION') ,
    ('Animation' , 'ANIMATION') ,
    ('Horror' , 'HORROR')
)



class Sliders(models.Model):
    name = models.CharField(_("name"), max_length=50)
    imdb_rate = models.DecimalField(_("IMDB rating "), max_digits=5, decimal_places=2)
    pg_rate = models.IntegerField(_("PG rate "), blank=True , null=True)
    time_long = models.IntegerField(_("Time long") ,  blank=True , null=True)
    description = models.TextField(_("description"))
    starring = models.CharField(_("Starring"), max_length=200)
    Genres = models.CharField(_("genres"), choices=GENRES_CHOICES ,  max_length=10)
    movie_trailor = models.URLField()
    # tags = 
    slug = models.SlugField(_("slug"), blank=True , null=True)


    class Meta:
        verbose_name = _("Sliders")
        verbose_name_plural = _("Sliderss")

    def __str__(self):
        return self.name
    
    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Sliders , self).save(*args, **kwargs)




  
