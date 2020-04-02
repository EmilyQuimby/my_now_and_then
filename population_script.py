#The team were unable to get the population script to run without error messages, but we have included the 
#code and commented it out.

#import os
#import django

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mynowandthen.settings')
#django.setup()

#from django.contrib.auth.models import User
#from nowandthen.models import Picture, Comment, UserProfile


#def populate():
#    banana_user = [
#        {'username': 'Banana',
#        'email': 'Banana@cat.com',
#         'password': 'Banana1234'},
#    ]
#    johann_user = [
#        {'username': 'Banana',
#         'email': 'Banana@cat.com',
#         'password': 'Banana1234'},
#    ]
#    wmffre_user = [
#        {'username': 'Wmffre',
#         'email': 'Wmffre@cat.com',
#         'password': 'Wmffre1234'},
#    ]
#
#    maryhill_comments = [
#                            {'user': banana_user,
#                             'body': 'wowo I love this photo - reminds me of when I used to live there!'},
#                            {'user': johann_user,
#                             'body': 'I love Maryhill - its such a pretty part of Glasgow lol'},
#                            {'user': wmffre_user,
#                             'body': 'gonnae no dae that lol', 'user_id': 3}],
#
#    fireworks_comments = [
#        {'user': banana_user,
#         'body': 'amazing fireworks - thanks for sharing :)'},
#        {'user': johann_user,
#         'body': 'love fireworks, love this, love YOU!'},
#        {'user': wmffre_user,
#         'body': 'whoop!'}]
#
#    cityscape_comments = [
#        {'user': banana_user,
#         'body': 'more pics like this one please!!'},
#        {'user': johann_user,
#         'body': 'what a sucky picture hahahaaaa'},
#        {'user': wmffre_user,
#         'body': 'great - love it!'}]
#
#    pics = {'Maryhill': {'comments': maryhill_comments,
#                         'image': 'shared_pics/View-from-kitchen-window-of-Maryhill-tenements.1970.jpg',
#                         'title': 'Maryhill Laundry',
#                         'description': 'back view',
#                         'tag_one': 'Maryhill',
#                         'tag_two': 'Laundry',
#                         'era': '1970s',
#                         'likes': 64},
#            'Fireworks': {'comments': fireworks_comments,
#                          'image': 'shared_pics/fireworks.jpg',
#                          'title': 'Glasgow Fireworks',
#                          'description': 'Fireworks at Glasgow Green',
#                          'tag_one': 'Glasgow',
#                          'tag_two': 'Fireworks',
#                          'era': '2010s',
#                          'likes': 32},
#            'Cityscape': {'comments': cityscape_comments,
#                          'image': 'shared_pics/glasgow_cityscape_copy.jpg',
#                          'title': 'Glasgow Cityscape',
#                          'descrpition': 'View over Glasgow',
#                          'tag_one': 'Cityscape',
#                          'tag_two': 'Glasgow',
#                          'era': '1990s',
#                          'likes': 16}}
#
#    for pic, pic_data in pics.items():
#        p = add_picture(pic,
#                        pic_data['image'],
#                        pic_data['title'],
#                        pic_data['description'],
#                        pic_data['tag_one'],
#                        pic_data['tag_two'],
#                        pic_data['era'])
#        for c in pic_data['comments']:
#            add_comment(c[0], c[1])
#
#    for p in Picture.objects.all():
#        for c in Comment.objects.filter(picture=p):
#            print(f' - {p}: {c}')
#
#
# def add_user(name, email, password):
#    u = User.objects.get_or_create(username=name, first_name='Test', last_name='User', email=email)[0]
#    u.set_password(password)
#    up = UserProfile.objects.get_or_create(user=u)[0]
#    u.save()
#    return up
#
#
# def add_picture(image, title, description, tag_one, tag_two, era, likes=0):
#   p = Picture.objects.get_or_create(image=image, title=title)[0]
#    p.description = description
#    p.tag_one = tag_one
#    p.tag_two = tag_two
#    p.era = era
#    p.like = likes
#    p.save()
#    return p
#
#
# def add_comment(user, body):
#    u = User.objects.get(username=user)
#    up = UserProfile.objects.get(user=u)
#    c = Comment.objects.get_or_create(user=up, body=body)[0]
#    c.save()
#    return c
#
#
#if __name__ == '__main__':
#    print('Starting Now And Then population script...')
#    populate()