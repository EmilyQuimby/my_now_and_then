from django import forms
from nowandthen.models import Picture, Comment
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from nowandthen.models import UserProfile

ERA_CHOICES = [
    ('Present_day', 'Present Day'),
    ('2010-2020', '2010-2020'),
    ('2000-2010', '2000-2010'),
    ('1990s', '1990s'),
    ('1980s', '1980s'),
    ('1970s', '1970s'),
    ('1960s and earlier', '1960s and earlier')
]


# For the page for adding photos.

class PictureForm(forms.ModelForm):
    title = forms.CharField(help_text="What is your picture's title?", widget=forms.TextInput(attrs={'size': '170'}),
                            required=True)
    description = forms.CharField(help_text="Please tell us about a bit about your picture.", widget=forms.Textarea(),
                                  required=True)
    tag_one = forms.CharField(
        help_text="Please provide a word to describe your image. This will help people to find it.", required=False)
    tag_two = forms.CharField(help_text="Please give us an additional word to describe the picture.", required=False)
    era = forms.CharField(help_text="What era does this picture relate to?", widget=forms.Select(choices=ERA_CHOICES),
                          required=True)
    image = forms.ImageField()

    class Meta:
        model = Picture
        fields = ('image', 'title', 'description', 'tag_one', 'tag_two', 'era',)

    def as_p(self):
        # Returns this form rendered as HTML <p>s.
        return self._html_output(
            normal_row='<p%(help_text)s<p></p>%(field)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)


# For the comment functionality (not completed).
class CommentForm(forms.ModelForm):
    body = forms.CharField(help_text="What is your comment?", widget=forms.TextInput(attrs={'size': '1000'}),
                           required=True)

    class Meta:
        model = Comment
        fields = ('body',)


# Form below are for new user registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
