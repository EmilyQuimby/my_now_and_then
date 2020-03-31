import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mynowandthen.settings')

import django

django.setup()
from nowandthen.models import Picture, Comment


def populate():
    maryhill_comments = [
        {'body': 'wowo I love this photo - reminds me of when I used to live there!'},
        {'body': 'I love Maryhill - its such a pretty part of Glasgow lol'},
        {'body': 'gonnae no dae that lol', 'user_id': 3}]

    fireworks_comments = [
        {'body': 'amazing fireworks - thanks for sharing :)'},
        {'body': 'love fireworks, love this, love YOU!'},
        {'body': 'whoop!'}]

    cityscape_comments = [
        {'body': 'more pics like this one please!!'},
        {'body': 'what a sucky picture hahahaaaa'},
        {'body': 'great - love it!'}]

    pics = {'media/shared_pics/View-from-kitchen-window-of-Maryhill-tenements.1970.jpg':
                {'comments': maryhill_comments, 'title': 'Maryhill Laundry', 'description':
                    'view from my back door when I lived here in the 70s', 'tag_one': 'Maryhill', 'tag_two': 'Laundry',
                 'era': '1970s', 'likes': 64},
            'media/shared_pics/fireworks.jpg': {'comments': fireworks_comments, 'title': 'Glasgow Fireworks',
                                                'description': 'Fireworks at Glasgow Green',
                                                'tag_one': 'Glasgow', 'tag_two': 'Fireworks',
                                                'era': '2010s', 'likes': 32},
            'media/shared_pics/glasgow_cityscape_copy.jpg': {'comments': cityscape_comments, 'title': 'Glasgow Cityscape', 'descrpition':
                'View over Glasgow', 'tag_one': 'Cityscape', 'tag_two': 'Glasgow',
                'era': '1990s',  'likes': 16}}

    for pic, pic_data in pics.items():
        p = add_picture(pic, pic_data['title'], pic_data['description'], pic_data['tag_one'], pic_data['tag_two'],
                        pic_data['era'], pic_data['likes'])
        for c in pic_data['comments']:
            add_comment(p, c['body'])

    for p in Picture.objects.all():
        for c in Comment.objects.filter(picture=p):
            print(f' - {p}: {c}')


def add_picture(image, title, description, tag_one, tag_two, era, likes=0):
    p = Picture.objects.get_or_create(image=image, title=title)[0]
    p.description = description
    p.tag_one = tag_one
    p.tag_two = tag_two
    p.era = era
    p.like = likes
    p.save()
    return p


def add_comment(image, body):
    c = Comment.objects.get_or_create(body=body)[0]
    c.image = image
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Now And Then population script...')
    populate()
