from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from whimsy.views import views

# RESTful stuffs
from tastypie.api import Api
from whimsy.api import JobResource, TaskResource, CompanyResource, SkillResource
from django.conf.urls import include

v1_api = Api(api_name='v1')
v1_api.register(JobResource())
v1_api.register(TaskResource())
v1_api.register(CompanyResource())
v1_api.register(SkillResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^interactive$', views.interactive, name='interactive'),
    url(r'^standard$', views.standard, name='standard'),
    url(r'^$', views.home, name='home'),
    url(r'^wakemydyno\.txt$', TemplateView.as_view(template_name='wakemydyno.txt', content_type='text/plain')),
)
