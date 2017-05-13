from django.shortcuts import render
from .models import Post


def index(request):
    'DB에서 Post목록을 가져와서, HTML문자열을 생성/응답합니다.'
    return render(request, 'photowall/index.html', {
        'post_list': Post.objects.all(),
    })

