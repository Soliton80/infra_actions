from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!! \n'
                        'Сделаю в следующий раз цветную раскладку')


def second_page(request):
    return HttpResponse('А это вторая страница!')
