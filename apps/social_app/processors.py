from .models import Networks

def context_dict(request):
    ctx = {}
    links = Networks.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx