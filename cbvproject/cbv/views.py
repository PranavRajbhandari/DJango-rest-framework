from django.shortcuts import render
from rest_framework.views import APIView
# its like a decorator in function based
from rest_framework.response import Response
from .models import Course, CourseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet, ModelViewSet


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer







# viewSET (Same url pk and normal)
'''
class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
      '''  
        
    

'''
# now both at onces
class CourseListView(generics.ListCreateAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView ):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer
'''
# genericapiview----------------------------------------------------------------------
'''
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer
     '''
'''
class CourseDetailView(generics.RetrieveAPIView, generics.DestroyAPIView,generics.UpdateAPIView ):
     queryset = Course.objects.all()
     serializer_class = CourseSerializer


'''


# ........................mixins plus generic------------

'''
class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


    def get(self, request):
        return self.list(request)
    # list came from listmodelmixin

    def post(self,request):
        return self.create(request)
'''

'''
class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self,request, pk):
        return self.retrieve(request, pk)
    
    def delete(self,request, pk):
         return self.destroy(request, pk)
    
    def put(self,request, pk):
         return self.update(request, pk)


'''













# .....................................................................................................classbasedview

'''
class CourseListView(APIView):
    def get(self , request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
      
        return Response(serializer.data)
    
    def post(self, request):
        courseSerializer = CourseSerializer(data= request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)
    

class CourseDetailView(APIView):
    def get_course(self, pk):
        try: 
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
                raise Http404


    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        course = self.get_course(pk)
        courseSerializer = CourseSerializer(course, data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.error)

'''