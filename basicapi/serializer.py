from rest_framework import serializers
from basicapi.models import Book
from django.forms import ValidationError
#from dataclasses import field
'''
class BookSerilaizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    qantity = serializers.IntegerField()


    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.publish_date = data.get('publish_date', instance.publish_date)
        instance.qantity = data.get('qantity', instance.qantity)
        
        instance.save()
        return instance 

'''

class BookSerilaizer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"


    def validate_title(self, value):
        if value == "Sex":
            raise ValidationError("No book related to sex")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 200 and data["qantity"] > 200:
            raise ValidationError("to big for inventory")

        return data


    def get_description(self, data):
        return "This book is called " + data.title + " and it is " + str(data.number_of_pages) + " pages long"


