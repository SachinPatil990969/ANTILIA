from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from authentication.helpers import require_access_token, decode_jwt_token, dt_to_str
from authentication.models import membersModel, memberProfileModel
from .models import services, clubBooking, Events, Gallery

# Create your views here.

@require_access_token
def dashboard_view(request):
 # Get the current time
    current_time = datetime.now().time()
    # print(current_time)

    # Define greeting messages based on the time of day
    if current_time.hour < 12:
        greeting = 'Good morning'
    elif current_time.hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'

     # Get the user's name (you can replace 'John' with the actual user's name)

    email = decode_jwt_token(request.session.get('token'))['email']
    getMember = membersModel.objects.get(email=email)
    getMemberProfile = memberProfileModel.objects.get(member_id_id= getMember.id)
    
    member_data = {
        'member_id': getMember.id,
        'first_name':getMember.first_name,
        'last_name':getMember.last_name,
        'email':getMember.email,
        'mobile':getMember.mobile,
        'profile': getMemberProfile.profile.url,
        'gender': getMemberProfile.gender
    }
    request.session['member_data'] = member_data


    # Pass the greeting and user_name to the template
    context = {
        'greeting': greeting,
        'member_name': f"{getMember.first_name} {getMember.last_name}"
    }
    return render(request, 'dashboard.html', context)

@require_access_token
def services_view(request):
    services_ = services.objects.all().order_by('name')
    bookings_ = clubBooking.objects.all()
    context = {
       'services' : services_,
       'bookings' : bookings_
    }
    return render(request, 'services.html', context)

@require_access_token
def addEvent(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        content = request.POST['content']

        member_id = request.session.get('member_data')['member_id']
        # print(event_name, from_date, to_date, content, member_id)

        create_club = clubBooking.objects.create(
            member_id_id=member_id,
            event_name=event_name,
            from_date=from_date,
            to_date=to_date,
            content=content
        )
        create_club.save()
        messages.success(request, f'{event_name} - Event added')
        return redirect('services_view')
    return redirect('services_view')

@require_access_token
def delete_event(request, booking_id):
    getBooking = clubBooking.objects.get(id = booking_id)
    getBooking.delete()
    return redirect('services_view')

@require_access_token
def update_event(request, booking_id):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        content = request.POST['content']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        getBooking = clubBooking.objects.get(id=booking_id)
        getBooking.event_name = event_name
        getBooking.content = content
        # Convert the date format before saving
        getBooking.from_date = from_date
        getBooking.to_date = to_date
        getBooking.save()
        return redirect('services_view')

    getBooking = clubBooking.objects.get(id = booking_id)
    context = {
        'event_name': getBooking.event_name,
        'from_date':getBooking.from_date.strftime('%Y-%m-%d'),
        'to_date':getBooking.to_date.strftime('%Y-%m-%d'),
        'content': getBooking.content
    }
    print(context)
    return render(request, 'update_event.html', context)

@require_access_token
def gallery_view(request):
    galleries = Gallery.objects.all()
    context = {
        'galleries' : galleries
    }
    return render(request, 'gallery.html', context)

@require_access_token
def events_view(request):
    events = Events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events.html', context)

@require_access_token
def emergency_contact_view(request):
    return render(request, 'emergency_contact.html')

@require_access_token
def suggestion_view(request):
    return render(request, 'suggestion.html')

@require_access_token
def profile_view(request):
    return render(request, 'profile.html')

