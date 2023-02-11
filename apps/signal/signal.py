from talon import Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.slack = "app.name: Signal-desktop"
mod.apps.slack = """
os: linux
and app.name: Signal-desktop
"""
ctx.matches = r"""
app: signal
"""


@ctx.action_class("edit")
class EditActions:
    def line_insert_down():
        actions.edit.line_end()
        actions.key("shift-enter")


@mod.action_class
class Actions:

    def signal_conversation_new():
        """Initiate a new conversation"""

    def signal_conversation_open_menu():
        """Open the current conversation's menu"""

    def signal_settings():
        """Open the settings menu"""

    def signal_focus_message_input():
        """Focus the message input field"""

    def signal_open_media_overview():
        """Open the media overview for the current conversation"""

    def signal_insert_emoji(text: str):
        """Insert the given emoji"""


@ctx.action_class("user")
class UserActions:
    def messaging_open_channel_picker():
        actions.key("ctrl-f")

    def messaging_channel_previous():
        actions.key("alt-up")

    def messaging_channel_next():
        actions.key("alt-down")

    def messaging_unread_previous():
        actions.key("alt-shift-up")

    def messaging_unread_next():
        actions.key("alt-shift-down")

    def messaging_open_search():
        actions.key("ctrl-shift-f")

    def messaging_mark_workspace_read():
        # currently not possible in Signal desktop
        pass

    def messaging_mark_channel_read():
        # currently not possible in Signal desktop
        pass

    # Files and Snippets
    def messaging_upload_file():
        actions.key("ctrl-u")

    def signal_conversation_new():
        actions.key("ctrl-n")

    def signal_settings():
        actions.key("ctrl-,")

    def signal_focus_message_input():
        actions.key("ctrl-shift-t")

    def signal_open_media_overview():
        actions.key("ctrl-shift-m")

    def signal_insert_emoji(text: str):
        emoji_id = actions.user.formatted_text(
            text, "SNAKE_CASE"
        )
        actions.insert(":{}".format(emoji_id))

    def signal_conversation_open_menu():
        actions.key("ctrl-shift-l")
