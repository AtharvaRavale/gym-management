from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Membership
from django.shortcuts import render, get_object_or_404
from .models import Trainer  




@login_required
def trainers(request):
    trainers_list = Trainer.objects.all()     # get all trainers   
    if request.user.is_authenticated:
            pass
    return render(request, 'memberships/trainers.html', {'trainers_list': trainers_list})




def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id) #single trainers 

    return render(request, 'memberships/trainer_detail.html', {'trainer': trainer})












@login_required
def memberships(request):
    membership_plans=Membership.objects.all()
    if request.user.is_authenticated:
        messages.info(request, f"Welcome back, {request.user.first_name}!")

    return render(request, 'memberships/memberships.html', {
        'membership_plans': membership_plans
    })



from .models import Membership, MembershipPurchase
from .forms import *

@login_required
def purchase_membership(request):
    if request.method == 'POST':
        form = MembershipPurchaseForm(request.POST)
        if form.is_valid():
            membership = form.cleaned_data['membership_id']
            purchase_date = form.cleaned_data['purchase_date']
            start_date = form.cleaned_data['start_date']

            # Save the purchase details to the database
            MembershipPurchase.objects.create(
                user=request.user,
                membership=membership,
                purchase_date=purchase_date,
                start_date=start_date
            )

            return redirect('membership_success')  # Redirect to a success page
    else:
        form = MembershipPurchaseForm(initial={"username": request.user.username, "purchase_date": now().date()})

    return render(request, 'memberships/purchase_membership.html', {'form': form})
