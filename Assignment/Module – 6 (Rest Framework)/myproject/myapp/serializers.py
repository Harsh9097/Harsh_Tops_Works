from rest_framework import serializers

class Bookserializers(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    isbn = serializers.CharField(max_length=50)
    publisher = serializers.CharField(max_length=50)