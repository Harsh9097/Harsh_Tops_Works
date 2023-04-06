from rest_framework import serializers

#models.model
class Studnetserializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    subject = serializers.CharField(max_length=50)
    #city = serializers.CharField(max_length=50)
