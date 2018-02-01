from rest_framework import permissions, viewsets

from voicesofyouth.project.models import Project
from voicesofyouth.user.models import MapperUser
from .serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
    Return a list of projects.

    You can use the querystring to get the translated version of the project. E.g. to get a project in portuguese
    brazilian just use: ?lang=pt-br. If the requested translation does not exists you will receive the default language. Returns list of projects that user id is associated, just use: ?auth_token=user_token

    retrieve:
    Return a specific project.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        token = self.request.query_params.get('auth_token')

        if token:
            user = MapperUser.objects.filter(auth_token=token).first()
            return user.projects.all()

        return Project.objects.all().filter(enabled=True)
