from rest_framework.serializers import ModelSerializer
from base.models import Todo, User



class Todo_serialized(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class User_serialized(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

