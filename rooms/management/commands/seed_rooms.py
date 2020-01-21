import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "Creates Reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How my revies do you want create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "bath": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()  # primary key를 저장
        created_clean = flatten(list(created_rooms.values()))  # primary key를 정제
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        houserules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)  # pk로 방을 찾음
            for i in range(random.randint(3, 14)):  # 사진의 갯수(최소 3개~최대 14개)
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,  # 아까 찾은 방을 참조하는 사진 객체 생성
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
            #  이 아래로는 다대다 필드의 추가 방법
            for a in amenities:  # 모든 amenities를 for로 순회
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:  # 매직넘버가 짝수면
                    room.amenities.add(a)  # 해당 amenitie를 room에 추가
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in houserules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
