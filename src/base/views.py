from imaplib import _Authenticator
from django.shortcuts import render, redirect
from .models import Todo, User, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout



@login_required(login_url='/login')
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})



@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        cat = Category.objects.filter(id=request.POST['category_id']).first()
        todo = Todo.objects.create(title=title, description=description, created_by = request.user)
        if cat:
            todo.category = cat
            todo.save()
        return redirect('todos_category', slug=cat.slug)
    return redirect('index')



@login_required(login_url='/login')
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('index')



@login_required(login_url='/login')
def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        cat_id = request.POST['category_id']
        todo.title = title
        todo.description = description
        cat = Category.objects.filter(id=cat_id).first()
        if cat:
            todo.category = cat
        todo.save()
        return redirect('index')
    return redirect('index')



@login_required(login_url='/login')
def complete(request, id):
    todo = Todo.objects.get(id=id)
    todo.set_completed()
    return redirect('index')



@login_required(login_url='/login')
def pending(request, id):
    todo = Todo.objects.get(id=id)
    todo.set_incomplete()
    todo.save()
    return redirect('index')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        if user and user.check_password(password):
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
        else:
            return render(request, 'auth/login.html', {'error': 'Incorrect Email or password', "email": email})
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('login_view')



@login_required(login_url='/login')
def new_category(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            category = Category.objects.filter(name=name).first()
            if not category:
                category = Category.objects.create(name=name)
                return redirect('todos_category', slug=category.slug)
        except:
            return redirect('index')
    return redirect('index')

@login_required(login_url='/login')
def delete_category(request):
    if request.method == 'POST':
        try:
            id = request.POST['category_id']
            category = Category.objects.get(id=id)
            category.delete()
            return redirect('index')
        except:
            return redirect('index')
    return redirect('index')

@login_required(login_url='/login')
def todos_category(request, slug):
    category = Category.objects.filter(slug=slug).first()
    if not category:
        return redirect('index')

    todos = Todo.objects.filter(category__slug=slug).all()
    return render(request, 'todo/list.html', {'todos': todos, 'category':category })