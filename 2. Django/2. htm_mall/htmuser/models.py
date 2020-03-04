from django.db import models

# Create your models here.


class HTMuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')
    level = models.CharField(max_length=8, verbose_name='등급',
                             choices=(('admin', 'admin'), ('user', 'user')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'HTMmall_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
