from django.db import models
from jsonfield import JSONField

class CatanBoard(models.Model):
    seed = models.IntegerField(primary_key=True)
    resource_tiles_order = JSONField()
    probabilities_order = JSONField()
    pips_order = JSONField()

    def get_seed(self):
        return self.seed
    
    def get_tiles_order(self):
        return self.resource_tiles_order
    
    def get_probabilities_order(self):
        return self.probabilities_order
    
    def get_pips_order(self):
        return self.pips_order
    
    def get_all(self):
        return {
        "seed": self.seed,
        "resource_tiles_order": self.resource_tiles_order,
        "probabilities_order": self.probabilities_order,
        "pips_order": self.pips_order
    }

    def __str__(self):
        return str(self.get_all())
        