from rest_framework import viewsets
from .tasks import send_booking_confirmation_email
from .serializers import BookingSerializer
from .models import Booking
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment, Booking


class InitiatePaymentView(APIView):
    def post(self, request):
        booking_id = request.data.get("booking_id")
        booking = Booking.objects.get(id=booking_id)
        payload = {
            "amount": str(booking.total_amount),
            "currency": "ETB",
            "email": booking.guest.email,
            "tx_ref": f"txn-{booking.id}",
            "callback_url": "https://yourapp.com/payment/verify/",
            "return_url": "https://yourapp.com/payment/success/"
        }
        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }
        r = requests.post(
            "https://api.chapa.co/v1/transaction/initialize", json=payload, headers=headers)
        res = r.json()
        if res["status"] == "success":
            Payment.objects.create(
                booking=booking,
                transaction_id=res["data"]["tx_ref"],
                amount=booking.total_amount,
                status="Pending"
            )
            return Response({"checkout_url": res["data"]["checkout_url"]})
        return Response({"error": "Payment initiation failed"}, status=400)


class VerifyPaymentView(APIView):
    def get(self, request, tx_ref):
        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"
        }
        r = requests.get(
            f"https://api.chapa.co/v1/transaction/verify/{tx_ref}", headers=headers)
        res = r.json()
        payment = Payment.objects.get(transaction_id=tx_ref)
        if res["status"] == "success":
            payment.status = "Completed"
        else:
            payment.status = "Failed"
        payment.save()
        return Response({"status": payment.status})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # Trigger async email
        send_booking_confirmation_email.delay(
            booking.guest.email, booking.id
        )
