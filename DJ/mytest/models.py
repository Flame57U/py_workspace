from django.db import models
from collections import namedtuple

from django.db import connection

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="名称")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "草稿"
        PUBLISHED = "published", "已发布"

    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(blank=True, verbose_name="内容")
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="状态",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="分类",
    )
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    is_top = models.BooleanField(default=False, verbose_name="置顶")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

def fun_raw_sql_query(**kwargs):
    song = kwargs.get('song')
    if song:
        result = Music.objects.raw('SELECT * FROM music WHERE song = %s', [song])
    else:
        result = Music.objects.raw('SELECT * FROM music')
    return result


def namedtuplefetchall(cursor):
    # Return all rows from a cursor as a namedtuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def fun_sql_cursor_update(**kwargs):
    song = kwargs.get('song')
    pk = kwargs.get('pk')

    '''
    Note that if you want to include literal percent signs in the query, 
    you have to double them in the case you are passing parameters:
    '''
    with connection.cursor() as cursor:
        cursor.execute("UPDATE music SET song = %s WHERE id = %s", [song, pk])
        cursor.execute("SELECT * FROM music WHERE id = %s", [pk])
        # result = cursor.fetchone()
        result = namedtuplefetchall(cursor)
    result = [
        {
            'id': r.id,
            'song': r.song,
            'singer': r.singer,
            'last_modify_date': r.last_modify_date,
            'created': r.created,
        }
        for r in result
    ]

    return result

class Share(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "share"