from rest_framework import serializers

from blog.models import Postblog


class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = Postblog
        fields =["date","blog"]