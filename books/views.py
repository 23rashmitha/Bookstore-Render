from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import (
    TeluguBook, HindiBook, EnglishBook, FrenchBook, KannadaBook,
    MechanicalBook, CivilBook, CseBook, EceBook, EeeBook, ChemicalBook,
    AnatomyBook, PhysiologyBook, BiochemistryBook, PharmacologyBook, MicrobiologyBook, PathologyBook,
    JeePhysicsBook, JeeChemistryBook, JeeMathBook, JeeMockBook
)

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

def engineering(request):
    return render(request, 'engineering.html')

def Medical(request):
    return render(request, 'medical.html')

def Jee(request):
    return render(request, 'jee.html')


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

# ----------------- ENGINEERING BRANCHES -----------------
def Mechanical(request):
    books = MechanicalBook.objects.all()
    return render(request, 'mechanical.html', {'books': books})

def mechanical_book_detail(request, book_id):
    book = get_object_or_404(MechanicalBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Civil(request):
    books = CivilBook.objects.all()
    return render(request, 'civil.html', {'books': books})

def civil_book_detail(request, book_id):
    book = get_object_or_404(CivilBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Cse(request):
    books = CseBook.objects.all()
    return render(request, 'cse.html', {'books': books})

def cse_book_detail(request, book_id):
    book = get_object_or_404(CseBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Ece(request):
    books = EceBook.objects.all()
    return render(request, 'ece.html', {'books': books})

def ece_book_detail(request, book_id):
    book = get_object_or_404(EceBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Eee(request):
    books = EeeBook.objects.all()
    return render(request, 'eee.html', {'books': books})

def eee_book_detail(request, book_id):
    book = get_object_or_404(EeeBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Chemical(request):
    books = ChemicalBook.objects.all()
    return render(request, 'chemical.html', {'books': books})

def chemical_book_detail(request, book_id):
    book = get_object_or_404(ChemicalBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

# ----------------- MEDICAL BRANCHES -----------------
def Anatomy(request):
    books = AnatomyBook.objects.all()
    return render(request, 'anatomy.html', {'books': books})

def anatomy_book_detail(request, book_id):
    book = get_object_or_404(AnatomyBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Physiology(request):
    books = PhysiologyBook.objects.all()
    return render(request, 'physiology.html', {'books': books})

def physiology_book_detail(request, book_id):
    book = get_object_or_404(PhysiologyBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Biochemistry(request):
    books = BiochemistryBook.objects.all()
    return render(request, 'biochemistry.html', {'books': books})

def biochemistry_book_detail(request, book_id):
    book = get_object_or_404(BiochemistryBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Pharmacology(request):
    books = PharmacologyBook.objects.all()
    return render(request, 'pharmacology.html', {'books': books})

def pharmacology_book_detail(request, book_id):
    book = get_object_or_404(PharmacologyBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def Microbiology(request):
    books = MicrobiologyBook.objects.all()
    return render(request, 'microbiology.html', {'books': books})

def microbiology_book_detail(request, book_id):
    book = get_object_or_404(MicrobiologyBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})
# ----------------- PATHOLOGY -----------------
def Pathology(request):
    books = PathologyBook.objects.all()
    return render(request, 'pathology.html', {'books': books})

def pathology_book_detail(request, book_id):
    book = get_object_or_404(PathologyBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})



def JeePhysics(request):
    books = JeePhysicsBook.objects.all()
    return render(request, 'jee_physics.html', {'books': books})

def jee_physics_book_detail(request, book_id):
    book = get_object_or_404(JeePhysicsBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def JeeChemistry(request):
    books = JeeChemistryBook.objects.all()
    return render(request, 'jee_chemistry.html', {'books': books})

def jee_chemistry_book_detail(request, book_id):
    book = get_object_or_404(JeeChemistryBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def JeeMath(request):
    books = JeeMathBook.objects.all()
    return render(request, 'jee_math.html', {'books': books})

def jee_math_book_detail(request, book_id):
    book = get_object_or_404(JeeMathBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})

def JeeMock(request):
    books = JeeMockBook.objects.all()
    return render(request, 'jee_mock.html', {'books': books})

def jee_mock_book_detail(request, book_id):
    book = get_object_or_404(JeeMockBook, id=book_id)
    return render(request, 'view_book.html', {'book': book})


