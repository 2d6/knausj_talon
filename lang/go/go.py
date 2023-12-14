from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()
ctx.matches = r"""
code.language: go
"""

ctx.lists["user.code_type"] = golang_common_types = {
    "bool": "bool",
    "byte": "byte",
    "complex one twenty eight": "complex128",
    "complex sixty four": "complex64",
    "error": "error",
    "float sixty four": "float64",
    "float thirty two": "float32",
    "int eight": "int8",
    "int sixteen": "int16",
    "int sixty four": "int64",
    "int thirty two": "int32",
    "int": "int",
    "rune": "rune",
    "string": "string",
    "unsigned int eight": "uint8",
    "unsigned int sixteen": "uint16",
    "unsigned int sixty four": "uint64",
    "unsigned int thirty two": "uint32",
    "unsigned int": "uint",
}

golang_keywords = {
    "const": "const ",
    "constant": "const ",
    "defer": "defer ",
    "go": "go ",
    "range": "range ",
    "type": "type ",
    "var": "var ",
    "variable": "var ",
}

mod.list("golang_keyword", desc="golang Keywords")
ctx.lists["user.golang_keyword"] = golang_keywords

ctx.lists["user.code_common_function"] = {
    "append": "append",
    "error format": "fmt.Errorf",
    "json marshal": "json.Marshal",
    "json on marshal": "json.Unmarshal",
    "len": "len",
    "length": "len",
    "make": "make",
    "panic": "panic",
    "print format": "fmt.Printf",
    "print line": "fmt.Println",
    "sleep": "time.Sleep",
    "string format": "fmt.Sprintf",
}

ctx.lists["user.code_libraries"] = {
    "F S test": "testing/fstest",
    "I O test": "testing/iotest",
    "I O util": "io/ioutil",
    "I O": "io",
    "O S": "os",
    "bytes": "bytes",
    "errors": "errors",
    "file path": "path/filepath",
    "format": "fmt",
    "json": "encoding/json",
    "log": "log",
    "math": "math",
    "net H T T P": "net/http",
    "net S M T P": "net/smtp",
    "net url": "net/url",
    "net": "net",
    "path": "path",
    "quick test": "testing/quick",
    "regex": "regexp",
    "sink": "sync",
    "sort": "sort",
    "string conversion": "strconv",
    "strings": "strings",
    "testing": "testing",
    "time": "time",
}

@ctx.action_class("user")
class UserActions:
    def code_block():
        actions.insert('{}')
        actions.edit.left()
        actions.key('enter')

    def code_operator_assignment():
        actions.insert(" = ")

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

    def code_operator_bitwise_and():
        actions.insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.insert(' &= ')

    def code_operator_increment():
        actions.insert('++')

    def code_operator_bitwise_or():
        actions.insert(" | ")

    def code_operator_bitwise_exclusive_or():
        actions.insert(" ^ ")

    def code_operator_bitwise_left_shift():
        actions.insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.insert(" >>= ")

    def code_insert_null():
        actions.insert("nil")

    def code_insert_is_null():
        actions.insert(" == nil")

    def code_insert_is_not_null():
        actions.insert(" != nil")

    def code_operator_indirection():
        actions.insert("*")

    def code_operator_address_of():
        actions.insert("&")

    def code_state_if():
        actions.insert("if ")

    def code_state_else_if():
        actions.insert("else if ")

    def code_state_else():
        actions.insert("else ")

    def code_state_switch():
        actions.insert("switch ")

    def code_state_case():
        actions.insert("case :")
        actions.edit.left()

    def code_state_for():
        actions.insert("for ")

    def code_break():
        actions.insert('break')

    def code_next():
        actions.insert('continue')

    def code_insert_true():
        actions.insert('true')

    def code_insert_false():
        actions.insert('false')

    def code_import():
        actions.insert("import ()")
        actions.edit.left()

    def code_state_return():
        actions.insert("return ")

    def code_insert_library(text: str, selection: str):
        actions.insert(f"\"{text}\"")

    def code_comment_line_prefix():
        actions.insert('// ')

    def code_comment_block():
        actions.insert('/*')
        actions.key('enter')
        actions.key('enter')
        actions.insert('*/')
        actions.edit.up()

    def code_comment_block_prefix():
        actions.insert('/*')

    def code_comment_block_suffix():
        actions.insert('*/')

    def code_insert_type_annotation(type: str):
        actions.insert(f" {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" {type}")

    def code_default_function(text: str):
        """Inserts function declaration"""
        actions.user.code_public_function(text)

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    def code_public_function(text: str):
        result = "func {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_function(text: str):
        result = "func {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)
