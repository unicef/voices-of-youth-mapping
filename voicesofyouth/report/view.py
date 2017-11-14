from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

from voicesofyouth.theme.models import Theme
from voicesofyouth.voyadmin.utils import get_paginator
from voicesofyouth.report.models import Report
from voicesofyouth.report.models import REPORT_STATUS_PENDING
from voicesofyouth.report.models import REPORT_STATUS_APPROVED
from voicesofyouth.report.models import REPORT_STATUS_REJECTED
from voicesofyouth.report.forms import ReportFilterForm
from voicesofyouth.report.forms import ReportForm


class ReportListView(TemplateView):
    template_name = 'report/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme_id = kwargs['theme']

        context['theme'] = get_object_or_404(Theme, pk=theme_id)

        data = {
            'theme': theme_id,
            'tag': self.request.GET.get('tag'),
            'search': self.request.GET.get('search'),
            'status': self.request.GET.get('status')
        }

        form = ReportFilterForm(data=data, theme=context['theme'])
        context['filter_form'] = form

        if form.is_valid():
            cleaned_data = form.cleaned_data
            page = self.request.GET.get('page')

            qs_filter = {}
            if cleaned_data['theme'] is not None:
                qs_filter['theme'] = cleaned_data['theme']

            if cleaned_data['tag'] is not None:
                qs_filter['tags'] = cleaned_data['tag']

            if cleaned_data['status'] is not '':
                qs_filter['status'] = int(cleaned_data['status'])

            if cleaned_data['search'] is not None:
                qs_filter['name__icontains'] = cleaned_data['search']

            context['reports'] = get_paginator(Report.objects.filter(**qs_filter), page)

        return context


class ReportView(TemplateView):
    template_name = 'report/view.html'

    def post(self, request, *args, **kwargs):
        report_id = request.POST.get('report')
        message = request.POST.get('message')

        if report_id and message:
            try:
                report = get_object_or_404(Report, pk=report_id)
                report.status = REPORT_STATUS_REJECTED
                report.save()

                messages.success(request, _('Report rejected'))
                return redirect(reverse('voy-admin:reports:index', kwargs={'theme': report.theme.id}))
            except Exception:
                return HttpResponse(status=500)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report_id = kwargs['report']

        context['report'] = get_object_or_404(Report, pk=report_id)
        context['theme'] = context['report'].theme

        return context


class ReportApproveView(TemplateView):
    def get(self, request, *args, **kwargs):
        report_id = kwargs['report']
        if report_id:
            report = get_object_or_404(Report, pk=report_id)
            report.status = REPORT_STATUS_APPROVED
            report.save()

            messages.success(request, _('Report approved'))
        return redirect(request.META.get('HTTP_REFERER'))


class AddReportView(TemplateView):
    template_name = 'report/add.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = ReportForm(data=request.POST)

        print(form.data)
        print(request.POST.getlist('tags'))
        print(request.POST.get('location'))
        print(form.errors)

        context['selected_tags'] = request.POST.getlist('tags')

        if request.POST.get('location') == '':
            messages.error(request, _('Set a location'))

        if form.is_valid():
            print(form.cleaned_data.get('title'))
            print('AAA')
        else:
            print('BBB')
            messages.error(request, form.non_field_errors())

        return super(AddReportView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_form'] = ReportForm(data=self.request.POST) if self.request.method == 'POST' else ReportForm()
        return context


class PendingReportView(TemplateView):
    template_name = 'report/pending.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        context['reports'] = get_paginator(Report.objects.filter(status=REPORT_STATUS_PENDING), page)

        return context
