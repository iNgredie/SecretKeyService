import uuid
from django.db import models


class Secret(models.Model):

    LIFETIME_CHOICES = [
        (604800, "7 days"),
        (259200, "3 days"),
        (86400, "1 day"),
        (43200, "12 hours"),
        (14400, "4 hours"),
        (3600, "1 hour"),
        (1800, "30 minutes"),
        (300, "5 minutes"),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=8)
    content = models.BinaryField()
    salt = models.BinaryField(null=True, blank=True)
    has_custom_passphrase = models.BooleanField(default=False)
    lifetime = models.IntegerField(choices=LIFETIME_CHOICES)

    def __str__(self):
        return str(self.pk)


