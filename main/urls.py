from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView, SupportView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('report-example/', TemplateView.as_view(template_name='report-example.html'), name='report_example'),
    path('privacy-policy/', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy_policy'),
    path('terms-conditions/', TemplateView.as_view(template_name='terms-conditions.html'), name='terms_conditions'),
    path('support/', SupportView.as_view(), name='support'),
]
