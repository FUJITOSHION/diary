import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
from .forms import InquiryForm, DiaryCreateForm


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"
    

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('app_diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2 #1ページに表示できるデータの数

    def get_queryset(self):
        # diaries = super().model.objects.filter(user=self.request.user).oreder_by('-created_at')
        # diaries_2nd = super().get_model().objects.filter(user=self.request.user).oreder_by('-created_at')
        diaries = self.model.objects.filter(user=self.request.user).order_by('-created_at')
        # ゲッターとは？
        return diaries


class DiaryDetailView(LoginRequiredMixin ,generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'


class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('app_diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit= False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)


    def from_invalid(self, form):
        messages.error(self.request, "日記を作成に失敗しました。")
        return super().form_invalid(form)