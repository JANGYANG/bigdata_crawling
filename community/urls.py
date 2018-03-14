import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.exportCsv, name='exportCsv'),
]