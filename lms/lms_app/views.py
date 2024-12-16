from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import BookForm , CategoryForm
# Create your views here.


def index(request) : 
    
    if request.method == 'POST' :
        add_book = BookForm(request.POST , request.FILES)
        add_category = CategoryForm(request.POST)
        if add_book.is_valid() :
            add_book.save()
        elif add_category.is_valid() :
            add_category.save()
    
    content = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form' : BookForm(),
        'form1' : CategoryForm(),
        'all' : Book.objects.filter(active = True).count(),
        'so' : Book.objects.filter(status = "sold").count(),
        're' : Book.objects.filter(status = "rental").count(),
        'av' : Book.objects.filter(status = "availble").count(),
    }
    if request.method == "POST" :
        add_category = CategoryForm(request.POST)
        if add_category.is_valid() :
            add_category.save()
    return render(request,'pages/index.html' , content)

def books(request) :

    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET : 
        title = request.GET['search_name']
        if title :
            search = search.filter(title__icontains = title)
    if request.method == "POST" :
        add_category = CategoryForm(request.POST)
        if add_category.is_valid() :
            add_category.save()
    content = {
        'form1' : CategoryForm(),
        'category' : Category.objects.all(),
        'books' : search
    }
    return render(request,'pages/books.html',content)

def update(request , id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES , instance=book_id)
        if book_save.is_valid() : 
            book_save.save()
            return redirect("/")
    #سينفذ هذا الشرط بالاول عند الضغط على تعديل واستدعاء صفحةالابديت
    else : 
        book_save = BookForm(instance=book_id)

    context = {
        'form2' : book_save
    }        
    return render(request , 'pages/update.html' , context)
    
    
def delete(request , id) :
    book_delete = get_object_or_404(Book , id = id)
    if request.method == 'POST' :
        book_delete.delete()
        return redirect("/")
    return render(request , 'pages/delete.html' )