from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create or get a host user
        host, created = User.objects.get_or_create(
            username='hostuser',
            defaults={'email': 'host@example.com'}
        )
        if created:
            host.set_password('password123')
            host.save()

        # Sample listings data
        sample_listings = [
            {
                'title': 'Beachfront Villa',
                'description': 'Beautiful villa near the beach',
                'location': 'Mombasa',
                'price_per_night': 120.00
            },
            {
                'title': 'City Apartment',
                'description': 'Cozy apartment in the city center',
                'location': 'Nairobi',
                'price_per_night': 80.00
            },
        ]

        for item in sample_listings:
            Listing.objects.create(
                host=host,
                title=item['title'],
                description=item['description'],
                location=item['location'],
                price_per_night=item['price_per_night']
            )

        self.stdout.write(self.style.SUCCESS('✅ Database seeded with sample listings!'))
