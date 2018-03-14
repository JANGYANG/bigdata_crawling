# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render
from .models import Community
from django.http import HttpResponse
import csv
# Create your views here.

def exportCsv(request):
    data = download_csv(request, Community.objects.all())
    return HttpResponse (data, content_type='text/csv')
    
def download_csv(request, queryset):
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr( obj, field.encode('utf-8')) for field in field_names])
    return response
download_csv.short_description = "Download selected as csv"