from rest_framework import generics, status
from rest_framework.response import Response

from system.models import Course, Contact, Branch, Category
from system.serializers import CourseSerializer


class CoursesListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        contacts = request.data.pop('contacts')
        category = request.data.pop('category')
        branches = request.data.pop('branches')

        course = Course.objects.create(**request.data)

        if category:
            category = Category.objects.get(name=category)
            course.category = category

        if contacts:
            for contact in contacts:
                c = Contact.objects.create(type=contact.get('type'), value=contact.get('value'))
                course.contacts.add(c)

        if branches:
            for branch in branches:
                b = Branch.objects.create(address=branch.get('address'),
                                          longtitude=branch.get('longtitude'),
                                          latitude=branch.get('latitude'))
                course.branches.add(b)

        course.save()
        serializer = CourseSerializer(instance=course)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
