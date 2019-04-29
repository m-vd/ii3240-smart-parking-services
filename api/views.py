from django.conf import settings
import json, datetime
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render

#Import models
from ticketing.models import Ticket 
from parkingLot.models import Lot
from user.models import User
from payment.models import Payment
from help.models import Help
from disaster.models import Disaster
from parkingLot.models import Lot


def CheckInAPI(request, *args, **kwargs):
    #API to check in to park
    #Needed parameters: userID and location
    if (request.method == 'POST'):
        user_id = request.POST.get('userID')
        if (User.objects.filter(userID=user_id)):
            if (Ticket.objects.filter(userID=user_id, exitTime__isnull=True)):
                return HttpResponse("You are already in")
            else: 
                parkloc = request.POST.get('location')
<<<<<<< Updated upstream
                lot = Lot.objects.get(lotName=parkloc)
                t = Ticket(userID = User.objects.get(userID=user_id), location = lot)
                
                if (lot.lotName == "Sipil" or lot.lotName == "SR"):
                    lot.capacity -= 1
                    lot.save()
                t.save()
                
=======
                u = User.objects.get(userID = user_id)
                l = Lot.objects.get(lotName = parkloc)  
                t = Ticket(userID = u, location = l)
                t.save()
                l.capacity=l.capacity-1
                l.save()
>>>>>>> Stashed changes
                output = {
                    'ticketID' : str(t.ticketID),
                    'entryTime' : str(t.entryTime),
                    'exitTime' : str(t.exitTime),
                }
                subject = 'You just check In!'
                message = 'Welcome to ITB! \n You just park your motorcycle at ' + str(t.location.lotName) + '\n The parking will cost you IDR2000 perhour'
                from_email = settings.EMAIL_HOST_USER
                to_list = [t.userID.userEmail]

                send_mail(subject,message,from_email,to_list,fail_silently=True)
                return HttpResponse(json.dumps(output))
        else:
            return HttpResponse("You're not allowed to park here")
    else:
        return HttpResponseForbidden()

def CheckOutAPI(request, *args, **kwargs):
    #API to checkout
    #Needed parameters: userID
    if (request.method == 'POST'):
        user_id = request.POST.get('userID')
        u = User.objects.get(userID = user_id)
        if (Ticket.objects.filter(userID=u, exitTime__isnull=True)):
            t = Ticket.objects.get(userID=u, exitTime__isnull=True)
            t.exitTime = datetime.datetime.now()
<<<<<<< Updated upstream
            t.save()
            print(t)
            resp = __PaymentAPI(t)
=======
            t.save()    
            l = t.location
            l.capacity=l.capacity+1            
            l.save()            
            resp = PaymentAPI(t)
>>>>>>> Stashed changes
            return resp
        else: 
            return HttpResponse("You have not checked in yet")
    else:
        return HttpResponseForbidden()

<<<<<<< Updated upstream
def __PaymentAPI(ticket, *args, **kwargs):
    u   = User.objects.get(userID = ticket.userID.userID)
    if (not u):
        return HttpResponse("error")
=======
def PaymentAPI(t, *args, **kwargs):
    u = t.userID
    price = 2000
    dur = (t.exitTime-t.entryTime).seconds//3600 
    remain = (t.exitTime-t.entryTime).seconds%3600 
    print(dur)
    total = dur*price 
    if (remain):
        total += price
    if (u.userBalance >= total):
        u.userBalance = u.userBalance - total
        u.save()
        p = Payment(userID = u, ticketID=t, duration=dur, amount=total)
        p.save()
        return HttpResponse("Payment successfull! \nIDR " + str(total) + " is deduced from your account\nYou have IDR" + str(u.userBalance) + " left")
>>>>>>> Stashed changes
    else:
        price   = 2000
        dur     = (ticket.exitTime-ticket.entryTime).seconds//3600 
        remain  = (ticket.exitTime-ticket.entryTime).seconds%3600 

        print(dur)
        total = dur*price 

        if (remain):
            total += price
        if (u.userBalance >= total):
            u.userBalance = u.userBalance - total
            u.save()
            p = Payment(userID = ticket.userID, ticketID=Ticket.objects.get(ticketID = ticket.ticketID), duration=dur, amount=total)
            loc_obj = ticket.location
            loc_obj.capacity += 1
            loc_obj.save()
            p.save()
            return HttpResponse("Payment successfull, you have IDR" + str(u.userBalance) + " left")
        else:
            ticket.exitTime = None
            ticket.save()
            return HttpResponse("Your balance is not sufficient, Amount = " + str(total))

def AskHelpAPI(request, *args, **kwargs):
    # API to handle POST Request asking a question or help
    if (request.method == 'POST'):
        question = request.POST.get('question')
        if (question):
            try:
                u = User.objects.get(userID = request.POST.get('userID'))
                h = Help(user = u, question = question)
                h.save()
                output = {
                    'helpID' : str(h.helpID),
                    'userID' : str(h.user.userID),
                    'question' : str(h.question),
                }
                return HttpResponse(json.dumps(output))
            except:
                return HttpResponseBadRequest("User not registered")
        else:
            return HttpResponseBadRequest("No questions asked")
    else:
        return HttpResponseForbidden()

def AnswerHelpAPI(request, *args, **kwargs):
    #API to handle POST Request answering a question or help
    if (request.method == 'POST'):
        answer = request.POST.get('answer')
        help_id = request.POST.get('helpID')
        if (answer):
            try:
                h = Help.objects.get(helpID = help_id)
                h.answer = answer
                h.answerTime = datetime.datetime.now()
                h.save()
                output = {
                    'helpID' : str(h.helpID),
                    'question' : str(h.question),
                    'answer' : str(h.answer),
                }
                return HttpResponse(json.dumps(output))
            except: 
                return HttpResponseBadRequest("Help ID not valid")
        else:
            return HttpResponseBadRequest("No answer is given")
    else:
        return HttpResponse("Hello")

def CheckInLotAPI(request, *args, **kwargs):
    #API to add or remove capacity per Lot.
    if (request.method == 'POST'):
        location_id = request.POST.get('locationID')
        if (location_id):
            lot_obj = Lot.objects.get(lotID = location_id)
            lot_obj.capacity -= 1
            lot_obj.save()
        else:
            return HttpResponseBadRequest()

    else:
<<<<<<< Updated upstream
        return HttpResponseForbidden()
        
=======
        return HttpResponse("Hello")

def AddDisaster(request, *args, **kwargs):
    if (request.method == 'POST'):
        location = request.POST.get('location')
        status = request.POST.get('status')
        description = request.POST.get('description')
        d = Disaster(location=location, status=status, description=description)
        d.save()
        output = {
            'disasterID' : str(d.disasterID),
            'status' : str(d.user.userID),
            'location' : str(d.location),
            'description' : str(d.description),
        }
        return HttpResponse(json.dumps(output))
    else:
        return HttpResponse("Hello")

def UpdateDisaster(request, *args, **kwargs):
    if (request.method == 'POST'):
        disaster_id = request.POST.get('disasterID')
        status = request.POST.get('status')
        description = request.POST.get('description')
        d = Disaster.objects.get(disasterID = disaster_id)
        if (d):
            d.status = status
            d.updateTime = datetime.datetime.now()
            d.description = description
            d.save()
            output = {
                'disasterID' : str(d.disasterID),
                'status' : str(d.user.userID),
                'location' : str(d.location),
                'description' : str(d.description),
            }
            return HttpResponse(json.dumps(output))
        else: 
            return HttpResponse("Disaster ID not valid")
    else:
        return HttpResponse("Hello")

def getCapacity(request, *args, **kwargs):
    if (request.method == 'GET'):
        lot_name = request.GET.get('location')
        l = Lot.objects.get(lotName = lot_name)
        if (l):
            output = {
                'lotID' : str(l.lotID),
                'location' : str(l.lotName),
                'capacity' : str(l.capacity),
            }
            return HttpResponse(json.dumps(output))
        else: 
            return HttpResponse("Lot Name not valid")
    else:
        return HttpResponse("Hello")
            

#Yang perlu dikerjain
#1. Location tuh perlu ada koordinat gitu biar bisa dikasih navigasi
#4. Generate Laporan
#5. Add booking
#6. Manage booking
#7. Navigate
>>>>>>> Stashed changes
