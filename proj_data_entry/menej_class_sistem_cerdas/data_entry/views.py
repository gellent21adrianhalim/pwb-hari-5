from django.shortcuts import render
from .forms import AddressForm, PenggunaForm, ContentForm, SearchPengguna
from .models import Pengguna,Content
from django.http import JsonResponse

# Create your views here.
def set_data_entry(request):
    form = AddressForm()
    context = {
        'form':form,
    }
    return render(request, 'data_entry/input_data_1.html',context)

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all()
    context = None
    form = PenggunaForm(None)
    if request.method =="POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            list_pengguna = Pengguna.objects.all()
            context = {
                'form':form,
                'list_pengguna':list_pengguna,
            }
            return render(request, 'data_entry/input_data_1.html',context)
    else:
        list_pengguna = Pengguna.objects.all()
        context = {
            'form':form,
            'list_pengguna':list_pengguna,
        }
        return render(request, 'data_entry/input_data_1.html',context)

def view_pengguna(request, id):
    try:
        pengguna = Pengguna.objects.get(pk=id)
        return render(request,'data_entry/pengguna_detail.html',{'user_id':pengguna.id})
    except Pengguna.DoesNotExist:
        return JsonResponse({'error': 'user not found'},status=404)

def get_pengguna_detail_api(requst, user_id):
    try:
        pengguna = Pengguna.objects.get(pk=user_id)
        data = {
            'email':pengguna.email,
            'address_1':pengguna.address_1,
            'address_2':pengguna.address_2,
            'city':pengguna.city,
            'state':pengguna.city,
            'zip_code':pengguna.zip_code,
            'tanggal_join':pengguna.tanggal_join.strftime('%Y-%m-%d') #format date as string
        }
        return JsonResponse(data)
    except Pengguna.DoesNotExist:
        return JsonResponse({'error':'User not found'},status=404)
    
def set_content(request):
    list_content = Content.objects.all()
    form = ContentForm(None)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            list_content = Content.objects.all()
            context = {
                'form':form,
                'list_content':list_content,
            }
            return render(request, 'data_entry/content.html',context)
    else:
        context = {
            'form':form,
            'list_content':list_content,
        }
        return render(request, 'data_entry/content.html',context)
    
def search_pengguna_by_state(request):
    pesan = None
    tampil = None
    form = None
    listpengguna = None
    status = None
    if request.method == 'POST':
        form = SearchPengguna(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            listpengguna = Pengguna.objects.filter(state=state)
            if not listpengguna.exists():
                pesan = 'Data Pengguna Tidak Ditemukan'
                status = True
            else :
                tampil = True
    else:
        form = SearchPengguna()
    
    context = {
        'form': form,
        'tampil': tampil,
        'pesan': pesan,
        'tatus': status,
        'listpengguna': listpengguna,
    }
    return render(request, "data_entry/list_pengguna.html", context=context)