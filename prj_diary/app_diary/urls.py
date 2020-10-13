from django.urls import path

from . import views

app_name = 'app_diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
]

"""
{% url 'app_diary:diary_detail' diary.pk %}
app_diary:detail => path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail')
ARG: diary.pk
url => 'diary-detail/diary.pk/'
def index(request, pk: int):
    instance = Model.objects.get(pk)
    return render(request, 'index.html', context)
    return Response...
"""
