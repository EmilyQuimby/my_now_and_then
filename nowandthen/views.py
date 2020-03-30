from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from pip._vendor.requests import post

from nowandthen.forms import PictureForm, CommentForm, UserProfileForm, UserForm
from nowandthen.models import Picture, Comment


def index(request):
    context_dict = {}
    return render(request, 'nowandthen/index.html', context=context_dict)


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'nowandthen/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('nowandthen:index'))
            else:
                return HttpResponse("Your nowandthen account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'nowandthen/login.html')


@login_required
def add_picture(request):
    form = PictureForm()
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('nowandthen:index'))
        else:
            print(form.errors)
    return render(request, 'nowandthen/add_picture.html', {'form': form})


@login_required
def add_comment(request, image_id):
    new_comment = None
    template_name = 'add_comment.html'
    image = get_object_or_404(Picture, id=image_id)
    comments = image.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object and don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'comment_form': comment_form, 'image': image,'comments': comments, 'new_comment': new_comment,'comment_form': comment_form}

    return render(request, template_name, context)


def photo_feed(request):
    picture_list = Picture.objects.all().order_by('when_added')
    comment_form = CommentForm()

    context_dict = {}
    context_dict['pictures'] = picture_list
    context_dict['comment_form'] = comment_form

    return render(request, 'nowandthen/photo_feed.html', context=context_dict)

def photo70(request):
    picture_list_70 = Picture.objects.filter(era=1970)

    context_dict = {}
    context_dict['pictures70'] = picture_list_70

    return render(request, 'nowandthen/1970.html', context=context_dict)


def photo80(request):
    picture_list_80 = Picture.objects.filter(era=1980)

    context_dict = {}
    context_dict['pictures80'] = picture_list_80

    return render(request, 'nowandthen/1980.html', context=context_dict)


def photo10(request):
    picture_list_10 = Picture.objects.filter(era=2010)

    context_dict = {}
    context_dict['pictures10'] = picture_list_10

    return render(request, 'nowandthen/2010.html', context=context_dict)

def search_results(request):
    return render(request, 'nowandthen/search_results.html')


# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('nowandthen:index'))
