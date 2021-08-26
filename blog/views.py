from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, CommentForm
from .models import BlogPost, BlogComment

# Create your views here.


def blog(request):
    """
    Displays all blog posts.
    Parameters:
    request.
    Returns:
    Render: request, blog template and context
   """

    blogposts = BlogPost.objects.all().order_by("-date")

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blogpost_id):
    """
    Display blog detail page.
    Parameters:
    request.
    blogpost_id: ID of the blog post displayed
    Returns:
    Render: request, blog detail template and context.
   """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'comments': comments,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blogpost(request):
    """
    Create Add blog post form for admin only.
    Deal with form submission.
    Arguments:
    1. request
    Returns:
    If GET : Reverse: request, template, form in context.
    If POST: argument blogpost.id to blog_detail view.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(
                        request,
                        'Failed to add blog post.\
                        Please ensure the form is valid.')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blogpost(request, blogpost_id):
    """
    Edits an existing blogpost.
    Display form only for Admin.
    Arguments:
    request
    blogpost_id: the ID of the edited blog post.
    Returns:
    If GET: request, template, context
    f POST: redirects to blog_detail template.
            adds blogpost.id to blog_detail view.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(
                    request,
                    'Failed to update the blog post.\
                    Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blogpost)
        messages.info(request, f'You are editing {blogpost.blog_title}')

    template = 'blog/edit_blogpost.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def delete_blogpost(request, blogpost_id):
    """
    Deletes at an existing blogpost.
    Only for Admin.
    Arguments:
    request
    blogpost_id: the ID of the deleted blogpost.
    Returns:
    redirect: to blog view.
    """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        blogpost.delete()
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))


@login_required
def blog_comment(request, blogpost_id):
    """
    Create Add comment post form for regitered user only.
    Deal with form submission.
    Arguments:
    request.
    blogpost_id: ID of the blogpost linked to comment.
    Returns:
    If GET : Reverse: request, template, form in context.
    If POST: argument blogpost.id to blog_detail view.
    """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_user = request.user
            comment.blogpost = blogpost
            comment.save()
            messages.success(request, 'Thank you for your comment !')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           'Oops something went wrong. \
                            Please try again.')
    else:
        form = CommentForm(instance=blogpost)
    template = 'blog/add_comment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """
    Deletes at an existing comment.
    Only for registered user.
    Arguments:
    request
    comment_id: the ID of the deleted comment.
    Returns:
    redirect: to blog view.
    """

    comment = get_object_or_404(BlogComment, pk=comment_id)

    if request.user == comment.comment_user or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Your comment is deleted !')
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))


@login_required
def edit_comment(request, comment_id):
    """
    Edits an existing blogpost.
    Display form only for Admin.
    Arguments:
    request
    comment_id: the ID of the edited blog comment.
    Returns:
    Redirect: to blog view.
    """

    comment = get_object_or_404(BlogComment, pk=comment_id)
    if request.user == comment.comment_user or request.user.is_superuser:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(
                            request,
                            'Your comment is successfully edited')
                return redirect(reverse('blog'))
            else:
                messages.error(request,
                               'Failed to edit your comment. \
                                Please ensure the form is valid.')
        else:
            form = CommentForm(instance=comment)
        template = 'blog/edit_comment.html'
        context = {
            'form': form,
            'comment': comment,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))