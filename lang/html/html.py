from talon import Context, Module, actions, settings
from ...core.user_settings import get_list_from_csv

ctx = Context()
mod = Module()
ctx.matches = r"""
code.language: html
code.language: javascriptreact
code.language: typescriptreact
"""

default_tags = {
    "html": "html",
    "head": "head",
    "body": "body",
    "title": "title",
    "meta": "meta",
    "link": "link",
    "script": "script",
    "div": "div",
    "span": "span",
    "image": "img",
    "bold": "b",
    "italic": "i",
}


tags = get_list_from_csv(
    "html_tags.csv",
    headers=("Tag", "Spoken"),
    default=default_tags,
)

mod.list("html_tag", desc="HTML tags")
ctx.lists["self.html_tag"] = tags

@mod.action_class
class Actions:
    def insert_html_tag(tag: str):
        """Inserts a new tag of a given type"""


@ctx.action_class("user")
class UserActions:
    def insert_html_tag(tag: str):
         actions.user.insert_between(f"<{tag}>", f"</{tag}>")
