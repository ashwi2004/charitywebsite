from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.utils import timezone
from .models import User,Cause,Donation
from .forms import UserForm,DonationForm
import datetime
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        existing_user = User.objects.filter(phone=phone).first()
        if existing_user:
            return HttpResponse("User already registered.", status=400)
        new_user = User(name=name, phone=phone, points=0)
        new_user.save()

        return redirect('donate')

    return render(request, 'register.html')

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            phone_no = form.cleaned_data['phone']
            cause_id = form.cleaned_data['cause'].id
            amount = form.cleaned_data['amount']
            donation_type = form.cleaned_data['donation_type']

            try:
                user = User.objects.get(phone=phone_no)
            except User.DoesNotExist:
                return JsonResponse({"success": False, "message": "Enter a registered phone number."}, status=400)

            try:
                cause = Cause.objects.get(id=cause_id)
            except Cause.DoesNotExist:
                return JsonResponse({"success": False, "message": "Selected cause does not exist."}, status=400)

            # Create and save the donation
            donation = Donation(
                user=user,
                cause=cause,
                amount=amount,
                date=timezone.now()
            )
            donation.save()

            # Update the total donations collected for the cause
            cause.amount_raised += amount
            points=amount
            cause.save()

            return JsonResponse({
                "success": True, 
                "message": "Donation recorded successfully.", 
                "redirect": f"/congrats/{user.id}/100/"
            })
        else:
            return JsonResponse({"success": False, "message": "Invalid form data."}, status=400)

    else:
        form = DonationForm()
        causes = Cause.objects.all()
        return render(request, 'donate.html', {'form': form, 'causes': causes})
    
def congrats(request, id, points):
    user = User.objects.filter(id=id).first()
    if not user:
        return HttpResponseNotFound("User not found")

    return render(request, 'congrats.html', {'user': user, 'points': points, 'id': id})

def causespage(request, id):
    causes = Cause.objects.all()
    user = get_object_or_404(User, id=id)
    return render(request, 'causespage.html', {'causes': causes})

def available_causes(request):
    causes = Cause.objects.all()
    return render(request, 'causespage.html', {'causes': causes})