from accounts.models import CustomUser
from django.db import models
import uuid


class Diary(models.Model):
    #  id = models.UUIDField(
    #      default=uuid.uuid4,
    #      primary_key=True,
    #      editable=False
    # )
    '''
    UUID sample
    ふつうのid => 1, 2, 3 uuid => sdklajfklsajfs, kfsjdklajfklsda, jfkshsfsafkj
    データべース複数になったりしてもユニークであることが保証される
    '''

    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add= True)  # auto_nowでは?

    class Meta:
        verbose_name_plural = 'app_diary'

    def __str__(self):
        return self.title

    __repr__ = __str__
    '''
    __str__, __repr__の2つをちゃんと定義しておくと,
    ターミナルから中身覗いたりとかadminから覗いたりした時にちゃんとこれが表示される
    '''