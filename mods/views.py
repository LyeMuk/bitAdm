from django.shortcuts import redirect, render
from .models import Alert

# Create your views here.

def bhm(request):
    notice=Alert.objects.filter(alert_department="bhm")
    context={
        'notice' : notice,
    }
    return render(request, 'bhm.html', context)

def csem(request):
    notice=Alert.objects.filter(alert_department="csem")
    context={
        'notice' : notice,
    }
    return render(request, 'csem.html', context)

def erpm(request):
    notice=Alert.objects.filter(alert_department="erpm")
    context={
        'notice' : notice,
    }
    return render(request, 'erpm.html', context)

def som(request):
    notice=Alert.objects.filter(alert_department="som")
    context={
        'notice' : notice,
    }
    return render(request, 'som.html', context)

def view_notice(request,id):
    g=Alert.objects.filter(id=id).first()
    context={
        'notice' : g,
    }
    return render(request, 'view_notice.html', context) 

def delete_notice(request,id):
    record = Alert.objects.get(id = id)
    kis = record.alert_department
    record.delete()
    if kis == 'bhm':
        return redirect(bhm)
    elif kis == 'csem':
        return redirect(csem)
    elif kis == 'erpm':
        return redirect(erpm)
    else:
        return redirect(som)


def redirect_me(request,slug):
    if slug == 'bhm':
        return redirect(bhm)
    elif slug == 'csem':
        return redirect(csem)
    elif slug == 'erpm':
        return redirect(erpm)
    else:
        return redirect(som)


temp = "null"
def create_notice(request,slug=None):
    global temp
    if slug == None:
        slug = temp
    else:
        temp = slug
    if request.method == "POST":
        a=Alert()
        a.alert_department=slug
        a.alert_date=request.POST.get("alert_date")
        a.alert_subject=request.POST.get("alert_subject")
        a.alert_body=request.POST.get("alert_body")
        a.save()
    return render(request, 'create_notice.html', {'slug':slug})