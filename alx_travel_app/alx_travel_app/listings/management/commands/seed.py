from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()

        titles = ['Beach House', 'Mountain Cabin', 'City Apartment', 'Country Villa']
        locations = ['Cape Coast', 'Aburi', 'Accra', 'Kumasi']
        for i in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description='A beautiful place to stay.',
                location=random.choice(locations),
                price_per_night=random.uniform(100, 500),
                max_guests=random.randint(1, 10),
                available=True
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added: {listing.title}'))
