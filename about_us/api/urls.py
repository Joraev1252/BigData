from django.urls import path
from about_us.api.views import about_us_view, our_courses_view, our_statics_view


app_name = 'about_us'

urlpatterns = [
    path('about/', about_us_view, name='about_us'),
    path('courses/', our_courses_view, name='our_courses'),
    path('statics/', our_statics_view, name='our_general_statics')
]