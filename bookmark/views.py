from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmark/bookmark_list.html', {'bookmarks': bookmarks})

def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/bookmark_form.html', {'form': form})

def bookmark_edit(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmark/bookmark_form.html', {'form': form})

def bookmark_delete(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark_list')
    return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark})

def bookmark_detail(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    return render(request, 'bookmark/bookmark_detail.html', {'bookmark': bookmark})
