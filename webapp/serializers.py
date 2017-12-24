from rest_framework import serializers
from . models import users

class usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
       # fields = ('firstname','lastname')
        fields = ('firstname','lastname','email_id','password')


