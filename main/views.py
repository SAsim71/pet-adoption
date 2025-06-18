from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pet, Adoption

def home(request):
    pets = Pet.objects.filter(adopted=False)
    return render(request, 'main/home.html', {'pets': pets})

@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'main/pet_detail.html', {'pet': pet})

@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if pet.adopted:
        messages.warning(request, f"{pet.name} has already been adopted.")
        return redirect('home')

    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        address = request.POST['address']
        Adoption.objects.create(
            user=request.user,
            pet=pet,
            adopter_name=name,
            contact=contact,
            address=address
        )
        pet.adopted = True
        pet.save()
        messages.success(request, f"You have successfully adopted {pet.name}!")
        return redirect('thank_you')

    return render(request, 'main/adopt_form.html', {'pet': pet})

@login_required
def thank_you(request):
    return render(request, 'main/thank_you.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')
