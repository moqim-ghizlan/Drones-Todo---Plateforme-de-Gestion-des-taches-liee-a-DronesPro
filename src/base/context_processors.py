from base.models import Category

def functions(request):
    return {
        'categories': Category.objects.all()
    }