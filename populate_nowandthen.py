import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'nowandthen_project.settings')

import django
django.setup()
from nowandthen.models import Comment, Picture


# No population script was created for this project, as it was not applicable to this project, given that 
# any population script would need to include images, as all comments, likes and tags need to go against an 
# image.
