from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, PublishingHouse, Friend
from django.shortcuts import redirect
from .forms import AddFriend


def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def pb_houses_books(request):
    pb_houses = PublishingHouse.objects.all()
    pb_houses_books = []
    for pb_house in pb_houses:
        books = Book.objects.filter(pb_house=pb_house).all()
        pb_house_books = {
            'pb_house': pb_house,
            'books': books,
        }
        pb_houses_books.append(pb_house_books)
    print(pb_houses_books)
    context = {'pb_houses_books': pb_houses_books}
    return render(request, 'pb_houses_books.html', context)


def friends_list(request):
    friends = Friend.objects.all()
    context = {'friends': friends}
    return render(request, 'friends_list.html', context)


def add_friend(request):
    if request.method == 'POST':
        new_friend = AddFriend(request.POST)
        new_friend.save()
        return redirect('add_friend')
    else:
        add_friend_form = AddFriend()
        context = {'form': add_friend_form}
        return render(request, 'add_friend.html', context)


def friend_info(request, id):
    person = Friend.objects.get(id=id)
    person_books = Book.objects.filter(friend_name=person).all()
    books = Book.objects.all()
    context = {
        'person': person.full_name,
        'age': person.age,
        'person_books': person_books,
        'books': books,
    }
    return render(request, 'friend_info.html', context)
