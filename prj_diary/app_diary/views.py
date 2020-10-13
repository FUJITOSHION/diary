import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary


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

    def get_queryset(self):
        # たぶん, リンターが読めてないだけで実態はある(ダメだったらしたのcodeを使用する。)
        diaries = super().model.objects.filter(user=self.request.user).oreder_by('-created_at')
        # ゲッター使う気がするどっちもためしてみて
        # でんわかかってきてたOKまたあとできく
        # 直接弄るとまずいからみたいな感じ, getmodelないねー
        # diaries_2nd = super().get_model().objects.filter(user=self.request.user).oreder_by('-created_at')
        # diaries = Diary.objects.filter(user = self.request.user).oreder_by('-created_at')
        # ゲッターとは？
        return diaries