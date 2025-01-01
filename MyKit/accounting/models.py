from django.db import models
from django.utils import timezone


# Currency模型 存储不同货币信息
class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    icon = models.CharField(max_length=100, verbose_name='Font 图标')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = '货币'
        verbose_name_plural = '货币'


# Account 模型用于存储用户账户信息
class Account(models.Model):
    name = models.CharField(max_length=100, verbose_name='账户名称')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='金额')
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, default=1,
                                 verbose_name='货币')  # default=1 Currency模型中人民币id为1
    icon = models.CharField(max_length=100, null=True, verbose_name='图标')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='创建日期')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_date']
        verbose_name = '账户'
        verbose_name_plural = '账户'


# Category 模型用于存储交易类别的信息。
class Category(models.Model):
    CATEGORY_TYPES = (
        ("expense", "支出"),
        ("income", "收入"),
        ("save", "优惠"),
    )
    name = models.CharField(max_length=100, verbose_name='类别名称')
    icon = models.CharField(max_length=100, verbose_name='图标')
    category_type = models.CharField(choices=CATEGORY_TYPES, default=CATEGORY_TYPES[0][1], max_length=100,
                                     verbose_name='类别类型')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '类别'
        verbose_name_plural = '类别'


# SubCategory 模型用于存储子类别信息，每个子类别属于一个父类别
class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='子类别名称')
    icon = models.CharField(max_length=100, verbose_name='图标')
    parent = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='父类别')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = '子类别'
        verbose_name_plural = '子类别'


# HistoryRecord 模型用于存储交易历史记录
class HistoryRecord(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, default=None, verbose_name='账户')
    time_of_occurrence = models.DateTimeField(default=timezone.now, verbose_name='发生时间')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='类别')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='子类别')
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, default=None, verbose_name='货币')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='金额')
    comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='备注')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='创建日期')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        ordering = ['-time_of_occurrence']
        verbose_name = '交易记录'
        verbose_name_plural = '交易记录'


class TransferRecord(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='outgoing_transfers')
    to_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='incoming_transfers')
    time_of_occurrence = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, default=1)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=500, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time_of_occurrence']
