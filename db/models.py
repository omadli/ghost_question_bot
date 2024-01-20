from tortoise.models import Model
from tortoise import fields

from settings import DEFAULT_LANGUAGE


class DbUser(Model):
    id = fields.BigIntField(pk=True, index=True)
    full_name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=255, null=True)
    join_date = fields.DatetimeField(auto_now_add=True)
    language = fields.CharField(max_length=3, default=DEFAULT_LANGUAGE)
    is_active = fields.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.id} {self.full_name}"    
    
    def html_mention(self, name: str = None) -> str:
        if name is None:
            name = self.full_name
        return f"<a href='tg://user?id={self.id}'>{name}</a>"
