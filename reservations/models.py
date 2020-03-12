import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models
from . import managers


class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CANCELED = "canceled"
    STATUS_CONFIRMED = "confirmed"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CANCELED, "Canceled"),
        (STATUS_CONFIRMED, "confirmed"),
    )

    status = models.CharField(
        choices=STATUS_CHOICES, max_length=12, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)

    objects = managers.CustomReservationManager()

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if True:
            start = self.check_in
            print(start)
            end = self.check_out
            print(end)
            difference = end - start
            print(difference)
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            print(existing_booked_day)
            if not existing_booked_day:
                super().save(*args, **kwargs)
                print(difference.days + 1)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    print(day)
                    BookedDay.objects.create(day=day, reservation=self)
            return
        return super().save(*args, **kwargs)
