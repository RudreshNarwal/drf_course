from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel
)
from utils.model_abstracts import UuidModel


class Contact(
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
    UuidModel
):
    class Meta:
        verbose_name_plural = "Contacts"

    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f'{self.title}'

# Model fields are used within the database i.e while creating the schema, visible to the developer only.
# while Serializer fields are used to when exposing the api to the client, visible to client also.