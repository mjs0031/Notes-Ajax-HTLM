from django.db import models

COLOR_TYPES = (
    ('r', 'Red'),
    ('b', 'Blue'),
    ('g', 'Green'),
    ('y', 'Yellow'),
    ('p', 'Purple'),
    ('o', 'Orange'),
)

class Blocks(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=1, choices=COLOR_TYPES)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    width = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __unicode__(self):
        return '%s\t%s' % (self.name, self.color)
    
    class Meta:
        ordering = ['name', 'color']
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
