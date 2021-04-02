from .models import Category

def Menu_Categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context