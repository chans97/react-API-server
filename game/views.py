from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


from .models import GameUser,Repl
from .serializers import PostListSerializer,PostDetailSerializer,ReplSerializer


class PostListView(generics.ListCreateAPIView):

    name = "board-list-create"
    serializer_class = PostListSerializer 
    pagination_class = PageNumberPagination

    def get_queryset(self):

        queryset = GameUser.objects.all().order_by('-id')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.set_filters( self.get_queryset(), request ) 
        """ paginate_queryset 내장 함수에 queryset 객채를 전달한다.
         이때 paginator라는 페이징 클래스를 인스턴스화한 속성에 size_query_
         param을 "page_size"를 적용한다. 이는 한번에 보여줄 게시물의 갯수를 어
         떤 파라미터를 통해 전달하는지 설정하는 속성이다. """ 
         
        self.paginator.page_size_query_param = "page_size" 
        page = self.paginate_queryset(queryset) 
        
        """ page 객체가 존재한다면 get_paginated_respon
        se 내장함수를 이용해 응답한다. 200 Success로 응답한다. """ 
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def set_filters(self, queryset, request):
        type = request.query_params.get('type', None)
        description = request.query_params.get('description', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        if description is not None:
            queryset = queryset.filter(description__contains=description)
        return queryset




class ReplViewSet(generics.ListCreateAPIView):
    queryset = Repl.objects.all()
    serializer_class = ReplSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = GameUser.objects.all()
    serializer_class = PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserByLevelView(generics.ListAPIView):
    serializer_class = PostDetailSerializer
    
    def get_queryset(self):
        return GameUser.objects.filter(id=self.kwargs['id'])