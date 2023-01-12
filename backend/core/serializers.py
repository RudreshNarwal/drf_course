from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


class ContactSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    message = CharField(source="description", required=True)
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'email',
            'message'
        )
        

# Model fields are used within the database i.e while creating the schema, visible to the developer only.
# while Serializer fields are used to when exposing the api to the client, visible to client also.
