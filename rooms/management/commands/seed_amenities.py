from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "Creates Amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="How my times blahlblahblah")

    def handle(self, *args, **options):

        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Wifi",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Private bathroom",
            "Hide",
            "Extras",
            "Washing machine",
            "Dryer",
            "Breakfast",
            "Indoor fireplace",
            "Cot",
            "High chair",
            "Self check-in",
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
            "Hide",
            "Safety features",
            "Smoke detector",
            "Carbon monoxide detector",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
