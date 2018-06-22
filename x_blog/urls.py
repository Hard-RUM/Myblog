from django.conf.urls import url
from .views import index, photos, blog, mail, short_codes, single, archives,categories,BlogView

app_name = 'x_blog'

urlpatterns = [
    # 设计首页的url
    url(r'^index/$', index, name='index'),

    url(r'^single/(?P<pk>\d+)/$', single, name='single'),

    url(r'^photos/$', photos, name='photos'),

    url(r'^blog/', blog, name='blog'),

    url(r'^short-codes/$', short_codes, name='short_codes'),

    url(r'^mail/$', mail, name='mail'),

    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[1-9]|1[0-2])/$', archives, name='archives'),

    url(r'^categories/(?P<pk>\d+)/$', categories, name='categories'),
]
