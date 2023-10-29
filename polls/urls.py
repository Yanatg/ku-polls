from django.urls import path
from polls.views.index_view import IndexView
from polls.views.details import DetailView, vote
from polls.views.results import ResultsView

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
