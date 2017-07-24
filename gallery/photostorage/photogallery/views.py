from django.shortcuts import render, redirect
from django.utils import timezone
from .models import picture, comment
from .forms import AddForm, AddComment
from hitcount.views import HitCountDetailView
from django.db.models import F


class PictureCountHitDetailView(HitCountDetailView):
    model = picture
    count_hit = False


def gallery_home(request):
    image_list = picture.objects.order_by('-pic_date')[:12]
    return render(request, 'picture_list.html', {'pictures': image_list})


def gallery_popular(request):
    image_list = picture.objects.order_by('-views')[:12]
    return render(request, 'popular.html', {'pictures': image_list})


def allphoto(request):
    image_list = picture.objects.order_by('pic_date')
    return render(request, 'allphoto.html', {'pictures': image_list})


def pic_detail(request, pk):
    pic = picture.objects.get(pk=pk)
    pic.views = F('views') + 1
    pic.save()
    pic.refresh_from_db()
    comm = comment.objects.filter(comment_pic=pk)
    if request.POST:
        form_comment = AddComment(request.POST)
        if form_comment.is_valid():
            comm = form_comment.save(commit=False)
            comm.comment_pic = pic
            comm.comment_date = timezone.now()
            comm.save()
            return redirect('pic_detail', pk=pic.pk)
    else:
        form_comment = AddComment(auto_id=False)
    return render(request, 'pic_detail.html', {'pic': pic, 'comments': comm, 'form_comment': form_comment})


def pic_upload(request):
    if request.POST:
        form_upload = AddForm(request.POST, request.FILES)
        if form_upload.is_valid():
            picture = form_upload.save(commit=False)
            picture.pic_date = timezone.now()
            picture.save()
            return redirect('pic_detail', pk=picture.pk)
    else:
        form_upload = AddForm()
    return render(request, 'pic_upload.html', {'form_upload': form_upload})
