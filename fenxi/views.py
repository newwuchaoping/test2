from django.shortcuts import render

# Create your views here.
from django.views import View
from fenxi.models import Preview


class AnimationView(View):
    """
    轮播图
    """
    def get(self, request):
        previews = Preview.objects.all()
        return render(request, 'animation.html', {"previews": previews})
