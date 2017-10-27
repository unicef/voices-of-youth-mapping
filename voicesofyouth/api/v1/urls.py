from django.conf.urls import include
from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from voicesofyouth.api.v1.report.views import ReportCommentsViewSet
from voicesofyouth.api.v1.report.views import ReportsViewSet
from voicesofyouth.api.v1.tag.views import TagsViewSet
from .project.views import ProjectsViewSet
from .theme.views import ThemesViewSet
from .views import UsersEndPoint

router = DefaultRouter()
router.register(r'projects', ProjectsViewSet, base_name='projects')
router.register(r'themes', ThemesViewSet, base_name='themes')
router.register(r'tags', TagsViewSet, base_name='tags')
router.register(r'user', UsersEndPoint, base_name='user')
router.register(r'reports', ReportsViewSet, base_name='reports')
router.register(r'report-comments', ReportCommentsViewSet, base_name='report-comments')

urlpatterns = [
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='Voices of Youth API')),
    url(r'', include(router.urls)),
    # url(r'^comments/$', CommentsEndPoint.as_view()),
]
