app: signal
#todo: some sort of plugin, consolidate with teams or something?
-
tag(): user.messaging

# Navigation
(conversation | convo) new: user.signal_conversation_new()
(conversation | convo) next: user.messaging_channel_next()
(conversation | convo) last: user.messaging_channel_previous()
(conversation | convo) unread next: user.messaging_unread_next()
(conversation | convo) unread last: user.messaging_unread_previous()
(conversation | convo) <number>: key("ctrl-{number}")
(conversation | convo) menu: user.signal_conversation_open_menu()

# Conversations
find in (conversation | convo): user.messaging_open_search()
signal attach file: user.messaging_upload_file()
signal focus input: user.signal_focus_message_input()
signal open media [overview]: user.signal_open_media_overview()
emote <user.text>: user.signal_insert_emoji(text)
emote last: key("up")
emote next: key("down")

# Miscellaneous
signal open settings: user.signal_settings()