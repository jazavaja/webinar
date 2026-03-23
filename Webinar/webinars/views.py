from django.shortcuts import render, redirect
from models.models import *
# Create your views here.
def webinar_detail(request, id):
    if request.method == 'POST':
        if request.POST.get('buy') == 'yes':
            w = Webinar.objects.get(id=id)
            w.stock -= 1
            w.save()
            Webinar_User.objects.create(
                user_id=User.objects.get(id=int(request.session.get('user'))),
                webinar_id=w,
                role='PARTICIPANT',
            )
        else:
            host_edit_webinar(request, id)

    webinar = Webinar.objects.get(id=id)
    role = Webinar_User.objects.filter(webinar_id=id,user_id=request.session.get('user')).first()
    # if request.method == 'POST':
    #     host_edit_webinar(request, id)

    if role:
        if request.session.get('user'):
            print('lol')
            return render(request, 'webinar-details.html',{'webinar':webinar,'role':role,'user':True})
        else:
            print('not lol')
            return render(request, 'webinar-details.html',{'webinar':webinar,'role':role})
    if request.session.get('user'):
        print('lol')
        return render(request, 'webinar-details.html',
                      {'webinar': webinar, 'user': True})
    else:
        return render(request, 'webinar-details.html', {'webinar': webinar})
def host_edit_webinar(request, id):
    webinar = Webinar.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('delete') == 'yep':
            webinar.delete()

            return redirect('home')
        webinar.name = request.POST.get('name')
        webinar.description = request.POST.get('description')
        # webinar.title_image = request.FILES['image']
        webinar.hosted_at = request.POST.get('hosted_at')
        webinar.link = request.POST.get('link')
        webinar.ticket_expiration = request.POST.get('ticket_expiration')
        webinar.type = request.POST.get('type')
        webinar.price = request.POST.get('price')
        webinar.stock = request.POST.get('stock')
        webinar.save()

        role = Webinar_User.objects.filter(webinar_id=id).first()
        return render(request, 'webinar-details.html',{'webinar':webinar,'role':role.role})
    # return render(request, 'host-edit-webinar.html',{'webinar':webinar})
def add_webinar(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')
        # image = request.FILES['image']
        hosted_at = request.POST.get('hosted_at')
        link = request.POST.get('link')
        ticket_expiration = request.POST.get('ticket_expiration')
        # type = request.POST.get('type')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        other_hosts = request.POST.getlist('other_hosts')
        webinar = Webinar.objects.create(
            name=name,
            description=description,
            hosted_at=hosted_at,
            link=link,
            ticket_expiration=ticket_expiration,
            price=price,
            stock=stock,
            type='public',
        )
        Webinar_User.objects.create(
            user_id=User.objects.get(id=int(request.session.get('user'))),
            webinar_id=webinar,
            role='HOST',
        )
        if other_hosts:
            for i in other_hosts:
                Webinar_User.objects.create(
                    user_id=User.objects.get(id=int(i)),
                    webinar_id=webinar,
                    role='HOST',
                )
        cat = Type.objects.get(name='normall')
        Category_Webinar.objects.create(
            webinar_id=webinar.id,
            category_id=cat.id,
        )

        return redirect('webinar_detail', webinar.id)
    users = User.objects.exclude(id=int(request.session.get('user')))
    return render(request, 'add_webinar.html',{'users':users})