from django.shortcuts import get_object_or_404,redirect,render
from notice.models import Notice
import pandas as pd
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from spider import spider

def home(request):
    notices = Notice.objects.all()
    context = {}
    context['notices'] = notices
    return render(request, 'home.html', context)


def bidding(request):
    if request.GET.get('key') == 'update':
        spider.spider()
        data = []
        b = pd.read_csv('./static/bidding.csv', encoding='utf-8')
        for i in range(len(b)):
            data.append(b.iloc[i])

        paginator = Paginator(data, 8)
        try:
            page_number = request.GET.get('page', '1')
            page = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage, InvalidPage):
            # 如果出现上述异常，默认展示第1页
            page = paginator.page(1)

        return render(request, 'bidding.html', {'page': page})
    else:
        data = []
        b = pd.read_csv('./static/bidding.csv', encoding='utf-8')
        for i in range(len(b)):
            data.append(b.iloc[i])

        paginator = Paginator(data, 8)
        try:
            page_number = request.GET.get('page', '1')
            page = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage, InvalidPage):
            # 如果出现上述异常，默认展示第1页
            page = paginator.page(1)

        return render(request, 'bidding.html', {'page': page})

