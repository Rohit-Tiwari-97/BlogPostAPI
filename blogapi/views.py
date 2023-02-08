from blogapi.models import BlogModel
from blogapi.serializers import BlogSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework import permissions



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['post']
    serializer_class = BlogSerializer



class BlogPostsViewSet(viewsets.ModelViewSet):
    '''To update or Delete post we can use Id in url
    For Example - "http://127.0.0.1:8000/blogs/1"   
    '''
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','head','put','patch','delete','options']
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author','date_created']




    

    
      