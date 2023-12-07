from tortoise import fields
from tortoise.models import Model


class User(Model):
    class Meta:
        table = "users"
        ordering = ["created_at"]

    id = fields.BigIntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class News(Model):
    class Meta:
        table = "news"
        ordering = ["created_at"]

    id = fields.BigIntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    text = fields.TextField()

    is_active = fields.BooleanField(default=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
