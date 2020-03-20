from django.db.models import Q
from django.http import Http404
from django.views.generic import View
from django.shortcuts import redirect, reverse, render
from users import models as user_models
from . import models, forms

# Create your views here.


def go_conversation(request, a_pk, b_pk):
    user_one = user_models.User.objects.get_or_none(pk=a_pk)
    user_two = user_models.User.objects.get_or_none(pk=b_pk)

    if user_one is not None and user_two is not None:
        try:
            conversation = models.Conversation.objects.filter(
                participants=user_one
            ).filter(participants=user_two)
            conversation = conversation[0]
            print("Complete Get")
        except models.Conversation.DoesNotExist:
            conversation = models.Conversation.objects.create()
            conversation.participants.add(user_one, user_two)
            print("Complete Create")

        return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))


class ConversationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        message = self.request.POST.get("message", None)
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))
