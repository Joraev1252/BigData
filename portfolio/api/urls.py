from django.urls import path
from portfolio.api.views import portfolio_view, contact_us_view, any_problems_view, asked_questions_view, our_team_view, partners_view, partners_logo_view


app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', portfolio_view, name='portfolio'),
    path('any_problems/', any_problems_view, name='any_problems'),
    path('contact_us/', contact_us_view, name='contact_us'),
    path('asked_questions/', asked_questions_view, name='asked_questions'),
    path('our_team/', our_team_view, name='our_team'),


    path('partners/', partners_view, name='partners'),
    path('partners_logo/', partners_logo_view, name='partners_logo'),
]