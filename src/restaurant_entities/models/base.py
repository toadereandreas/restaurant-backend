from django.db import models
import uuid


class GlobalID(models.Model):
    gid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        verbose_name="Global ID",
        help_text="Unique global identifier",
        db_index=True
    )

    class Meta:
        abstract = True

    @classmethod
    def get_pk(cls, gid):
        return cls.objects.values_list('pk', flat=True).get(gid=gid)
