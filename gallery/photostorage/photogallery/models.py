from django.db import models
from django.core.files import File
from django.db.models.fields.files import ImageField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils import timezone


class picture(models.Model):
    class Meta:
        db_table = "picture"

    def __str__(self):
        return self.pic_title

    def pic_thumb(self):
        thumb = '<style media="screen" type="text/css">' +\
            '.center-cropped {width: 150px; height: 150px; object-fit: cover; object-position: center; border-style: solid; border-color: #AAAAAA; padding: 3px;}' +\
            '</style>' +\
            '<a href="%s"><img src="%s" class="center-cropped"/></a>' % (self.pic_image.url, self.pic_image.url)
        return thumb
    pic_thumb.short_description = 'Image'
    pic_thumb.allow_tags = True
    pic_image = ImageField(upload_to = 'static/gallery/', verbose_name='Select Image', width_field=0, height_field=0)
    pic_title = models.CharField(max_length=200, verbose_name='Title')
    pic_text = models.TextField(verbose_name='Annotation')
    pic_date = models.DateTimeField(verbose_name='Datetime')
    views = models.IntegerField(default=0)


@receiver(pre_delete, sender=picture)
def picture_del(sender, instance, **kwargs):
    instance.pic_image.delete(False)


class comment(models.Model):
    class Meta:
        db_table = "comment"
    comment_pic = models.ForeignKey(picture, null=True, blank=True)
    comment_text = models.TextField(verbose_name='Comment Text')
    comment_date = models.DateTimeField(default=timezone.now)
