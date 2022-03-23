from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms  import Postform

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = Postform(request.POST)
      # IF the form is valid
        if form.is_valid( ):
        # Yes, Save
            form.save()
        # Redirect to Home
            return HttpResponseRedirect('/')

        else:
          # No show Error
            return HttpResponseRedirect(form.errors.as_json())  
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
     
    return render(request, 'posts.html',
                        {'posts':posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
