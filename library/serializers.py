from .models import Author,Book,Category
from rest_framework import serializers
class AuthorSerializer(serializers.ModelSerializer):
         class Meta:
              model = Author
              fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
         class Meta:
              model = Category
              fields ='__all__'

class BookSerializer(serializers.ModelSerializer):
         class Meta:
              model = Book
              fields ='__all__'