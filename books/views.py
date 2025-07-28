from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import TeluguBook, HindiBook, EnglishBook, FrenchBook, KannadaBook

# ----------------- HOME -----------------
def Home(request):
    return render(request, "index.html")


# ----------------- LOGIN -----------------
def Login(request):
    if request.method == 'POST':
        un = request.POST.get('Username')
        pw = request.POST.get('password')

        user = authenticate(username=un, password=pw)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful! Welcome 😊")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "login.html")


# ----------------- REGISTER -----------------
def Register(request):
    if request.method == 'POST':
        fn = request.POST.get('Fullname')
        em = request.POST.get('Email')
        un = request.POST.get('Username')
        pw = request.POST.get('password')
        cpw = request.POST.get('cpassword')

        if pw != cpw:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=un).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=em).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        user = User.objects.create_user(username=un, email=em, password=pw, first_name=fn)
        user.save()
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')

    return render(request, "register.html")


# ----------------- PAGES -----------------
def List(request):
    return render(request, "list.html")

def Stories(request):
    return render(request, "stories.html")


# ----------------- TELUGU -----------------
def Telugu(request):
    books = TeluguBook.objects.all()
    return render(request, 'telugu.html', {'books': books})

def telugu_book_detail(request, book_id):
    book = get_object_or_404(TeluguBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})


# ----------------- HINDI -----------------
def Hindi(request):
    books = HindiBook.objects.all()
    return render(request, 'hindi.html', {'books': books})

def hindi_book_detail(request, book_id):
    book = get_object_or_404(HindiBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})


# ----------------- ENGLISH -----------------
def English(request):
    books = EnglishBook.objects.all()
    return render(request, 'english.html', {'books': books})

def english_book_detail(request, book_id):
    book = get_object_or_404(EnglishBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})


# ----------------- FRENCH -----------------
def French(request):
    books = FrenchBook.objects.all()
    return render(request, 'french.html', {'books': books})

def french_book_detail(request, book_id):
    book = get_object_or_404(FrenchBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})


# ----------------- KANNADA -----------------
def Kannada(request):
    books = KannadaBook.objects.all()
    return render(request, 'kannada.html', {'books': books})

def kannada_book_detail(request, book_id):
    book = get_object_or_404(KannadaBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})
