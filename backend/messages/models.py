from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from backend.classes.models import Classes


class Message(models.Model):
    body = models.TextField(_("Body"))

    sender = models.ForeignKey(
        User, related_name='sender', verbose_name=_("Sender"),
        on_delete=models.DO_NOTHING)

    parent_msg = models.ForeignKey(
        'self', related_name='next_messages', null=True,
        blank=True, verbose_name=_("Parent message"),
        on_delete=models.DO_NOTHING)

    sent_at = models.DateTimeField(
        _("sent at"), auto_now_add=True, null=True, blank=True)

    ip = models.GenericIPAddressField(
        verbose_name=_('IP'), null=True, blank=True)

    user_agent = models.CharField(verbose_name=_(
        'User Agent'), blank=True, max_length=255)

    def __str__(self):
        return f"{self.sender.username} - {self.body}"


class ClassMessage(models.Model):
    classes = models.ForeignKey(
        Classes, related_name='Class', verbose_name=_("Class"),
        on_delete=models.DO_NOTHING)

    msg = models.ForeignKey(
        Message, unique=True, related_name='msg',
        verbose_name=_("Message"),
        on_delete=models.DO_NOTHING)

    def __str__(self):
        class_code = self.classes.code
        sender = self.msg.sender.username
        msg = self.msg.body
        return f"{class_code} - {sender} :- {msg}"
