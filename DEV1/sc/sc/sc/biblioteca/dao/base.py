from django.db import models


class BaseManager(models.Model):
    class Meta:
        app_label = 'bibilioteca' ## Dizer que esse base é de bibilioteca e não de outro app