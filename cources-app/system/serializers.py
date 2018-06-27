from rest_framework import serializers

from system.models import Branch, Contact, Category, Course


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'altitude', 'longtitude')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Course
        fields = ('name', 'logo', 'description', 'category', 'contacts', 'branches')
