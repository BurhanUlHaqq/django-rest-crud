from django.shortcuts import render

def books_list_view(request):
    return render(request, 'books_list.html')
