from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()
ctx.matches = r"""
tag: user.bash
"""

bash_option = {
    "error": "e",
    "unset": "u",
    "fail": "o pipefail",
    "no log": "o nolog",
    "trace": "x",
    "verbose": "v",
}

mod.list("bash_option", desc="Bash options")
ctx.lists["user.bash_option"] = bash_option


@mod.capture(rule="{user.bash_option}+")
def bash_options(m) -> str:
    """
    Matches a nonempty list of bash options
    """
    return "".join(m.bash_option_list)


declare_option = {
    "array": "a",
    "integer": "i",
    "lowercase": "l",
    "read only": "r",
    "exported": "x",
    "global": "g",
}

mod.list("declare_option", desc="Options to builtin 'declare'")
ctx.lists["user.declare_option"] = declare_option


@mod.capture(rule="{user.declare_option}+")
def declare_options(m) -> str:
    """
    Matches a nonempty list of declare options
    """
    return "".join(m.declare_option_list)


bash_keywords = {
    "exit": "exit",
    "local": "local",
    "read only": "readonly",
    "end if": "fi",
    "end case": "esac",
    "end for": "done",
    "end while": "done",
    "execute": "exec",
    "built in": "builtin",
    "alias": "alias",
}

mod.list("bash_keyword", desc="Bash Keywords")
ctx.lists["user.bash_keyword"] = bash_keywords


@ctx.action_class("user")
class UserActions:
    def code_comment_line_prefix():
        actions.insert("#")

    def code_private_function(text: str):
        name = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )
        actions.insert(f"{name}() ")
        actions.user.code_block()

    def code_block():
        """Inserts equivalent of {\n} for the active language, and places the cursor appropriately"""
        actions.insert("{}")
        actions.edit.left()
        actions.key("enter")

    def code_state_if():
        """Inserts if statement"""
        actions.user.insert_between("if ", "; then")

    def code_state_else_if():
        """Inserts else if statement"""
        actions.user.insert_between("elif ", "; then")

    def code_state_else():
        """Inserts else statement"""
        actions.insert("else")

    def code_state_switch():
        """Inserts switch statement"""
        actions.user.insert_between("case ", " in")

    def code_state_case():
        """Inserts case statement"""
        actions.user.insert_between("", ") ;;")

    def code_state_for():
        """Inserts for statement"""
        actions.user.insert_between("for ", " in ; do")

    def code_state_while():
        """Inserts while statement"""
        actions.user.insert_between("while ", "; do")

    def code_state_infinite_loop():
        """Inserts infinite loop statement"""
        actions.user.insert_between("while true; do ", " done")

    def code_state_return():
        """Inserts return statement"""
        actions.insert("return")

    def code_break():
        """Inserts break statement"""
        actions.insert("break")

    def code_next():
        """Inserts next statement"""
        actions.insert("continue")

    def code_operator_subscript():
        """code_operator_subscript (e.g., C++ [])"""
        actions.user.insert_between("[", "]")

    def code_operator_assignment():
        """code_operator_assignment"""
        actions.insert("=")

    def code_operator_subtraction():
            actions.insert(" - ")

    def code_operator_subtraction_assignment():
        actions.insert(" -= ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_addition_assignment():
        actions.insert(" += ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_multiplication_assignment():
        actions.insert(" *= ")

    def code_operator_exponent():
        actions.insert(" ^ ")

    def code_operator_division():
        actions.insert(" / ")

    def code_operator_division_assignment():
        actions.insert(" /= ")

    def code_operator_modulo():
        actions.insert(" % ")

    def code_operator_modulo_assignment():
        actions.insert(" %= ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" != ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    def code_operator_and():
        actions.insert(" && ")

    def code_operator_or():
        actions.insert(" || ")
