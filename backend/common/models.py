from django.db import models
from django.utils import timezone as tz


class BaseModel(models.Model):
    """
    Common fields and methods for other models to inherit.
    """
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Override model save() method to add update data to history log.
        """
        self.created_at = tz.localtime()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
