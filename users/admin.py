from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_model


class RoomInline(admin.TabularInline):
    model = room_model.Room


# Register your models here. 모델을 가져오는것
@admin.register(models.User)  # <-데코레이터. 아래 클래스는 기본적으로 데코레이터의 모델을 조종 가능
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin"""

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",  # 파란부분
            {
                "fields": (  # 필드 정의
                    "avatar",  # 필드들
                    "gender",
                    "bio",
                    "language",
                    "birthdate",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
