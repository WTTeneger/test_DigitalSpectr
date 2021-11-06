from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserData
from .forms import form_add_date
from .serializers import CapitalSerializer


class GetUsersInfoView(APIView):
    def get(self, request):
        data_users = []
        if ('field', 'to_') in request.GET.copy():
            f = request.GET.copy().__getitem__('field')
            to_ = request.GET.copy().__getitem__('to_')

            if to_ != 'none':
                filter_ = '' if to_ == 'up' else '-'
                list_of_users = UserData.objects.order_by(filter_ + f)
            else:
                list_of_users = UserData.objects.all()
            print(list_of_users)
        elif 'search_value' in request.GET.copy():
            list_of_users = UserData.objects.filter(email__contains=request.GET.copy().__getitem__('search_value'))
        else:
            list_of_users = []
        for el in list_of_users:
            data_users.append({'email': el.email, 'phone_number': el.phone_number, 'message': el.message})
        return Response({'list_of_users': data_users})

    def post(self, request):
        print(request)


def main_page(request):
    """
    Контроллер для отображения на главной странице списка всех записей.
    """

    list_of_users = UserData.objects.all()
    context = {'list_of_users': list_of_users}
    form = form_add_date()
    return render(
        request=request,
        template_name='test/mains.html',
        context={'context': context, 'form': form}
    )


def add_page(request):
    """
    Контроллер для добавления данных
    """
    if request.method == 'POST':
        form = form_add_date(request.POST)
        if form.is_valid():
            print('request', request)
            email, phone_number, message = request.POST.get('email'), request.POST.get(
                'phone_number'), request.POST.get('message')
            data_to_db = UserData(email=email, phone_number=phone_number, message=message)
            data_to_db.save()
            # return HttpResponse("<h2>Hello, {0} {1} {2}</h2>".format(email, phone_number, message))
            return HttpResponseRedirect('/users')
    else:
        form = form_add_date()

    return render(
        request=request,
        template_name='test/add_page.html',
        context={'form': form}
    )
