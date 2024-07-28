from rest_framework import viewsets, parsers, permissions

from .. import  serializer, models
from ...base.permissions import IsAuthor


class UserView(viewsets.ModelViewSet):
    """Просмотр редактирования данных пользователя"""
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializer.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()

class AuthorView(viewsets.ReadOnlyModelViewSet):
    """Список авторов"""
    queryset = models.AuthUser.objects.all()
    serializer_class = serializer.AuthorSerializer

class SocialLinkView(viewsets.ModelViewSet):
    """CRUD ссылок соц.сетей пользователя"""
    serializer_class = serializer.SocialLinkSerializer
    permissions_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)