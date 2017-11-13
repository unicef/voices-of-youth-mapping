from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from voicesofyouth.project.models import Project
from voicesofyouth.user.forms import MapperFilterForm
from voicesofyouth.user.models import AdminUser
from voicesofyouth.user.models import MapperUser


class AdminView(TemplateView):
    template_name = 'user/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admins'] = AdminUser.objects.all()
        return context


class MapperView(TemplateView):
    template_name = 'user/mapper.html'
    form_class = MapperFilterForm

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'filter_form': form}
        delete = request.POST.get('deleteMappers')

        if delete:
            try:
                MapperUser.objects.filter(id__in=delete.split(',')).delete()
            except Exception:
                return HttpResponse(status=500)
            return HttpResponse("Users deleted!")

        if form.is_valid():
            cleaned_data = form.cleaned_data
            project = cleaned_data['project']
            theme = cleaned_data['theme']
            search = cleaned_data['search']

            if project and theme and project != theme.project:
                qs = []
            elif theme:
                qs = theme.mappers_group.user_set.all()
            elif project:
                groups_ids = project.themes.values_list('mappers_group__id')
                qs = MapperUser.objects.filter(groups__id__in=groups_ids)
            else:
                qs = MapperUser.objects.all()

            if not isinstance(qs, list) and search:
                qs = qs.filter(Q(username__icontains=search) |
                               Q(first_name__icontains=search) |
                               Q(last_name__icontains=search))
            context['mappers'] = qs

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mappers'] = MapperUser.objects.all()
        context['projects'] = Project.objects.filter()
        context['filter_form'] = MapperFilterForm()
        return context
