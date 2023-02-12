tag: user.bash
-
tag(): user.unix_utilities
tag(): user.code_imperative

tag(): user.code_comment_line
tag(): user.code_functions
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"

she bang: "#!/bin/bash"
she bang environment: "#!/usr/bin/env bash"
option {user.bash_option}: "{bash_option}"
option set <user.bash_options>: "set -{bash_options}"
option unset <user.bash_options>: "set +{bash_options}"
op pipe: " | "
op right to: " > "
op append to: " >> "
op from: " < "
op append: "+="

state test: "[["
state end test: "]]"

state {user.bash_keyword}: insert("{bash_keyword} ")

state (continuation|continue):
    insert(" \\")
    key("enter")

reference [<user.text>]:
    insert("${")
    user.insert_between(user.formatted_text(text or '', "SNAKE_CASE"), "}")
quoted reference [<user.text>]:
    insert('"${')
    user.insert_between(user.formatted_text(text or '', "SNAKE_CASE"), '}"')
# add default inside variable reference
state with default: ":-"

state (command|subshell):
    user.insert_between("$(", ")")
state math:
    user.insert_between("(( ", " ))")
state math reference:
    user.insert_between("$(( ", " ))")

declare <user.declare_options> [<user.text>]:
    insert("declare -{declare_options} ")
    insert(user.formatted_text(text or '', "SNAKE_CASE"))
