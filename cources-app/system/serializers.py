import time

from rest_framework import serializers

from system.models import Branch, Contact, Category, Course


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longtitude')


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
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Course
        fields = ('name', 'logo', 'description', 'category', 'contacts', 'branches')

    def create(self, validated_data):
        t = time.time()
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        category = validated_data.pop('category')
        category = Category.objects.get(name=category.get('name'))
        course = Course.objects.create(**validated_data)
        course.category = category
        for contact in contacts:
            c = Contact.objects.create(**contact)
            course.contacts.add(c)
        for branch in branches:
            b = Branch.objects.create(**branch)
            course.branches.add(b)
        e = time.time() - t
        print("serializer_time: ", e)
        return course
