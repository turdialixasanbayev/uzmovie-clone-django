from django.shortcuts import render

from django.views import View


class PageNotFoundView(View):
    status = 404
    template_name = 'base/404.html'

    def get(self, request, exception=None):
        return render(request=request, template_name=self.template_name, status=self.status)


def custom_400_view(request, exception):
    return render(request, 'base/400.html', status=400)

def custom_401_view(request, exception):
    return render(request, 'base/401.html', status=401)

def custom_403_view(request, exception):
    return render(request, 'base/403.html', status=403)

def custom_500_view(request, exception=None):
    return render(request, 'base/500.html', status=500)
