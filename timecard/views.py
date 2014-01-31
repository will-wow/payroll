from .models import Employee, Holiday, Day
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.http import HttpResponse
import json


class Days(DetailView):
    model = Day

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Days, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the sections
        context['days'] = Day.objects.filter(employee=1, work_date__lte='2013-01-15')

        return context