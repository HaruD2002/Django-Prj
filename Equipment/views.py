'''
    Creating view for all equipment
'''
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .models import Equipment, Catagory
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateEquipment, UpdateEquipmentInfo, CreateCatagoryForm


def admin_required(login_url=None):
    'Check if the user is super user or not and return a true or false value'
    return user_passes_test(lambda x: x.is_superuser, login_url=login_url)


@login_required(login_url='/login')
def view_all_equipment(request):
    'all user can see all the device they can borrow from the system'
    equipment = Equipment.objects.all()
    catagory = Catagory.objects.all()
    if request.method == 'POST':
        form = CreateEquipment(request.POST, request.FILES)
        equipment_id = request.POST['equip_id']
        equipment_name = request.POST['equip_name']
        equipment_description = request.POST['equip_des']
        catagory_id = request.POST['cata_id']
        try:
            Equipment.objects.get(equipment_id=equipment_id)
            messages.error(request, 'Equipment cant have same id')
        except Exception:
            if len(equipment_id) > 0 and len(equipment_name) > 0:
                new_equipment = Equipment()
                new_equipment.equipment_id = equipment_id
                new_equipment.equipment_name = equipment_name
                new_equipment.equiment_description = equipment_description
                new_equipment.catagory_id = Catagory.objects.get(
                    catagory_id=catagory_id)
                new_equipment.save()
                messages.success(request, 'Create item successfully')
            else:
                messages.error(request, 'error adding new equipment')
        return HttpResponseRedirect(reverse("equipment:all_equipment"))
    else:
        catagoryform = CreateCatagoryForm()

    return render(request, 'Equipment/viewEquipment.html',
                  {'Equipemnts': equipment,
                   'catagory': catagory, 'catagoryform': catagoryform})


@admin_required(login_url='/profile/{user.username}')
@login_required(login_url='/login')
def delete_equip(request, equipment_id):
    '''
        delete the equipment from the databases
    '''
    this_equipment = Equipment.objects.get(equipment_id=equipment_id)
    this_equipment.delete()

    messages.warning(request, 'delete successfully')
    return HttpResponseRedirect(reverse("equipment:all_equipment"))


@admin_required(login_url='/profile/{user.username}')
@login_required(login_url='/login')
def update_equip(request, equipment_id):
    get_equipment = Equipment.objects.get(equipment_id=equipment_id)
    if request.method == 'POST':
        form = UpdateEquipmentInfo(request.POST, instance=get_equipment)

        if form.is_valid():
            form.save()
            messages.success(request, 'update item successfully')
            return HttpResponseRedirect(reverse("equipment:all_equipment"))
        else:
            messages.error(request, 'something went wrong')
            return HttpResponseRedirect(reverse("equipment:all_equipment"))
    else:
        form = UpdateEquipmentInfo(instance=get_equipment)

    return render(request, 'Equipment/update_equip_info.html', {'form': form})


@login_required(login_url='/login')
def view_all_catagory(request):
    catagory_all = Catagory.objects.all()
    if request.method == "POST":
        form = CreateCatagoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'new catagory added')
            return HttpResponseRedirect(reverse())
        else:
            messages.error(request, 'Something when wrong')
            return HttpResponseRedirect(reverse())
    else:
        form = CreateCatagoryForm()
    return render(request, 'Equipment/view_all_catagory.html',
                  {"catagory_list": catagory_all,
                   "form": form})


@login_required(login_url='/login')
def update_catagory(request, catagoryid):
    catagory = Catagory.objects.get(id=catagoryid)
    return render(request, 'Equipment/update_catagory.html}')


@login_required(login_url='/login')
def delete_catagory(request, catagoryid):
    catagory = Catagory.objects.get(id=catagoryid)
    catagory.delete()
    return HttpResponseRedirect(reverse('Equipment:view_all_catagory'))


@login_required(login_url='/login')
@admin_required(login_url='/profile/{user.usææername}')
def create_catagory(request):
    if request.method == 'POST':
        form = CreateCatagoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '''new catagory was added''')
        else:
            messages.error(request, '''Something went wrong!!!''')
        return HttpResponseRedirect(reverse('equipment:all_equipment'))
    else:
        form = CreateCatagoryForm()
    return HttpResponseRedirect(reverse('equipment:all_equipment'),
                                {'form': form})
