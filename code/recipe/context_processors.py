from .models import Keyword, Shopping


def all_tags(request):
    tags = Keyword.objects.all()
    return {'tags': tags}


def url_parse(request):
    result_str = ''
    for item in request.GET.getlist('filters'):
        result_str += f'&filters={item}'
    return {'filters': result_str}
