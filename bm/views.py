from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated():
        return redirect('bookmarks_index')
    
    return render(request, 'index.html')