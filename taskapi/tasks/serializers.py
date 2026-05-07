from rest_framework import serializers
from .models import Task, Category
 
class TaskSummarySerializer(serializers.ModelSerializer):
     class Meta:
         model = Task
         fields = ['id', 'title', 'completed']
 
class CategorySerializer(serializers.ModelSerializer):
     tasks = TaskSummarySerializer(many=True, read_only=True)
     
     class Meta:
         model = Category
         fields = ['id', 'name', 'tasks']
 
class CategoryMiniSerializer(serializers.ModelSerializer):
     class Meta:
         model = Category
         fields = ['id', 'name']
 
class TaskSerializer(serializers.ModelSerializer):
     category = serializers.PrimaryKeyRelatedField(
         queryset=Category.objects.all(),
         allow_null=True,
         required=False
     )
     category_detail = CategoryMiniSerializer(source='category', read_only=True)
     
     class Meta:
         model = Task
         fields = ['id', 'title', 'description', 'category', 'category_detail', 'completed', 'created_at', 'updated_at']
