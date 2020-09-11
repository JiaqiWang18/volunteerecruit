from .models import Post
from django.core import serializers

import json

#make post object avaliable to all templates
def post_processor(request):
    data = serializers.serialize("json", Post.objects.all())
    return {'post':json.dumps(data)}