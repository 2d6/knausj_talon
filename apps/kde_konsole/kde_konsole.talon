os: linux
and app.name: konsole
-
# makes the commands in terminal.talon available
tag(): terminal

# activates the implementation of the commands/functions in terminal.talon
tag(): user.generic_unix_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application
tag(): user.git
tag(): user.anaconda
# tag(): user.kubectl

tag(): user.tabs
# TODO: add file_manager support

term split right: key("ctrl-(")
term split down: key("ctrl-)")
split grow: key("ctrl-shift-]")
split shrink: key("ctrl-shift-[")
split reset: key("ctrl-shift-\")

split left: key("ctrl-shift-left")
split right: key("ctrl-shift-right")
split up: key("ctrl-shift-up")
split down: key("ctrl-shift-down")

term save output: key("ctrl-shift-s")
term selection mode: key("ctrl-shift-d")

term toggle menu: key("ctrl-shift-m")

term zoom in: key("ctrl-+")
term zoom out: key("ctrl--")
term zoom reset: key("ctrl-alt-0")

term find: key("ctrl-shift-f")
^find up: key("f3")
^find down: key("shift-f3")

clear all: key("ctrl-u")
clear line: key("ctrl-u")
