from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Listing(models.Model):
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="bookings")
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest} booking {self.listing}"


class Review(models.Model):
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name="review")
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} for {self.booking.listing}"


class Payment(models.Model):
    booking = models.ForeignKey(
        'Booking', on_delete=models.CASCADE, related_name='payments')
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Pending, Completed, Failed
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking} - {self.status}"
