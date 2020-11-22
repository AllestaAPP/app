import math
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


def check_age(value):
    f, i = math.modf(value)
    if not (f == 0.0 or f == 0.5) or value > 8:
        raise ValidationError('0.5 刻み、8 以下で入力してください(0, 0.5, 1, 1.5...)')


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'テスト'),
    )

    NAME_CHOICES = (
        ('作業者1', '作業者1'),
        ('作業者2', '作業者2'),
        ('作業者3', '作業者3'),
        ('作業者4', '作業者4'),
        ('作業者5', '作業者5'),
        ('作業者6', '作業者6'),
        ('作業者7', '作業者7'),
        ('作業者8', '作業者8'),
        ('作業者9', '作業者9'),
        ('作業者10', '作業者10'),
        ('作業者11', '作業者11'),
        ('作業者12', '作業者12'),
        ('作業者13', '作業者13'),
        ('作業者14', '作業者14'),
        ('作業者15', '作業者15'),
        ('作業者16', '作業者16'),
        ('作業者17', '作業者17'),
        ('作業者18', '作業者18'),
        ('作業者19', '作業者19'),
        ('作業者20', '作業者20'),
        ('作業者21', '作業者21'),
        ('作業者22', '作業者22'),
        ('作業者23', '作業者23'),
        ('作業者24', '作業者24'),
        ('作業者25', '作業者25'),
        ('作業者26', '作業者26'),
        ('作業者27', '作業者27'),
        ('作業者28', '作業者28'),
        ('作業者29', '作業者29'),
        ('作業者30', '作業者30'),
    )

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric are allowed.')



    name = models.CharField(
        verbose_name='名前',
        choices=NAME_CHOICES,
        max_length=20,
    )

    takuhaikenpin = models.IntegerField(
        verbose_name='宅配検品(@400)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                  validators.MaxValueValidator(300)]
    )

    sonotakenpin = models.IntegerField(
        verbose_name='その他検品(@200)',
        # blank=True,
        null=True,
        default=0,
        validators = [validators.MinValueValidator(0),
                  validators.MaxValueValidator(999)]
    )

    nyuukosyouhinka = models.IntegerField(
        verbose_name='入庫商品化(@200)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(999)]
    )

    shiiresyouhinka = models.IntegerField(
        verbose_name='仕入商品化(@100)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                  validators.MaxValueValidator(5000)]
    )

    cleaning = models.IntegerField(
        verbose_name='クリーニング(@50)',
        # blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                  validators.MaxValueValidator(5000)]
    )

    dataerase = models.IntegerField(
        verbose_name='データイレース(@50)',
        # blank=True,
        null=True,
        default=0,
        validators = [validators.MinValueValidator(0),
                  validators.MaxValueValidator(999)]
    )

    shiirePC = models.IntegerField(
        verbose_name='仕入PC(@1000)',
        # blank=True,
        null=True,
        default=0,
        validators = [validators.MinValueValidator(0),
                  validators.MaxValueValidator(999)]
    )

    tsutaya = models.DecimalField(
        verbose_name='TSUTAYA関連(h)※0.5h刻みで入力',
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[check_age]
    )

    takuhaikaikon = models.DecimalField(
        verbose_name='宅配開梱(h)※0.5h刻みで入力',
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[check_age]
    )

    picking = models.DecimalField(
        verbose_name='搬出・ピッキング(h)※0.5h刻みで入力',
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[check_age]
    )

    datanyuuryoku = models.DecimalField(
        verbose_name='データ入力・画像登録(h)※0.5h刻みで入力',
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[check_age]
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        # auto_now_add=True
        default=timezone.now
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
