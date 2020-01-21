import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from lists import models as list_models


NAME = "lists"


class Command(BaseCommand):

    help = f"Creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help=f"How my {NAME} do you want create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users),},
        )
        seeder.execute()
        created = seeder.execute()  # primary key를 저장
        cleaned = flatten(list(created.values()))  # primary key를 정제
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.room.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
