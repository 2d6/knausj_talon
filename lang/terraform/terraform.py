from talon import Context, Module, actions

from ...core.user_settings import get_list_from_csv

ctx = Context()
mod = Module()
ctx.matches = r"""
code.language: terraform
"""

types = {
    "string": "string",
    "number": "number",
    "bool": "bool",
    "list": "list",
    "map": "map",
    "null": "null",
    "object": "object",
    "set": "set",
    "tuple": "tuple",
    "optional": "optional",
}

ctx.lists["user.code_type"] = types

# currently, this exists to prevent "prop for each" being rendered as "for = e"
common_properties = {
    "for each": "for_each",
    "user data": "user_data",
    "namespace": "namespace",
}

mod.list("terraform_common_property", desc="Terraform Modifier")
ctx.lists["self.terraform_common_property"] = common_properties


@mod.capture(rule="({self.terraform_common_property} | <user.text>)")
def terraform_common_property(m) -> str:
    return common_properties.get(m) or actions.user.formatted_text(m, 'SNAKE_CASE')


# spoken: (name, argument_count)
blocks = {
    "variable": ("variable", 1),
    "output": ("output", 1),
    "provider": ("provider", 1),
    "module": ("module", 1),
    "lifecycle": ("lifecycle", 0),
    "locals": ("locals", 0),
    "resource": ("resource", 2),
    "data source": ("data", 2),
    "dynamic": ("dynamic", 1),
    "backend": ("backend", 1),
}

block_argument_count = {name: argument_count for (name, argument_count) in
                        blocks.values()}

mod.list("terraform_block", desc="Simple Terraform Block")
ctx.lists["self.terraform_block"] = {spoken: name for spoken, (name, _) in
                                     blocks.items()}


@mod.capture(rule="({self.terraform_block} | <user.text>)")
def terraform_block_name(m) -> str:
    return actions.user.formatted_text(m, 'SNAKE_CASE')


ctx.lists["user.code_common_function"] = {
    # numeric functions
    "absolute": "abs",
    "seal": "ceil",
    "floor": "floor",
    "log": "log",
    "max": "max",
    "min": "min",
    "parse int": "parseint",
    "power": "pow",
    "signum": "signum",

    # string functions
    "chomp": "chomp",
    "ends with": "endswith",
    "format": "format",
    "format list": "formatlist",
    "indent": "indent",
    "join": "join",
    "lower": "lower",
    "regex all": "regexall",
    "regex": "regex",
    "replace": "replace",
    "split": "split",
    "starts with": "startswith",
    "string reverse": "strrev",
    "sub string": "substr",
    "title": "title",
    "trim prefix": "trimprefix",
    "trim space": "trimspace",
    "trim suffix": "trimsuffix",
    "trim": "trim",
    "upper": "upper",

    # collection functions
    "all true": "alltrue",
    "any true": "anytrue",
    "chunk list": "chunklist",
    "coalesce": "coalesce",
    "coalesce list": "coalescelist",
    "compact": "compact",
    "concat": "concat",
    "contains": "contains",
    "distinct": "distinct",
    "element": "element",
    "flatten": "flatten",
    "index": "index",
    "keys": "keys",
    "length": "length",
    "lookup": "lookup",
    "match keys": "matchkeys",
    "merge": "merge",
    "one": "one",
    "range": "range",
    "reverse": "reverse",
    "set intersection": "setintersection",
    "set product": "set product",
    "set subtract": "setsubtract",
    "set union": "setunion",
    "slice": "slice",
    "sort": "sort",
    "sum": "sum",
    "transpose": "transpose",
    "values": "values",
    "zip map": "zipmap",

    # encoding functions
    "base sixty four decode": "base64decode",
    "base sixty four encode": "base64encode",
    "base sixty four g zip": "base64gzip",
    "c s v decode": "csvdecode",
    "json decode": "jsondecode",
    "json encode": "jsonencode",
    "text decode base sixty four": "textdecodebase64",
    "text encode base sixty four": "textencodebase64",
    "earl encode": "urlencode",
    "yaml decode": "yamldecode",
    "yaml encode": "yamlencode",

    # filesystem functions
    "absolute path": "abspath",
    "directory name": "dirname",
    "dear name": "dirname",
    "base name": "basename",
    "file": "file",
    "template file": "templatefile",

    # date and time functions
    "format date": "formatdate",
    "timestamp": "timestamp",

    # hash and crypto functions
    "you you id": "uuid",

    # IP network functions
    "cider host": "cidrhost",
    "cider net mask": "cidrnetmask",
    "cider subnet": "cidrsubnet",
    "cider subnets": "cidrsubnets",

    # type conversion functions
    "can": "can",
    "nonsensitive": "nonsensitive",
    "sensitive": "sensitive",
    "to bool": "tobool",
    "to list": "tolist",
    "to map": "tomap",
    "to number": "tonumber",
    "to set": "toset",
    "to string": "tostring",
    "try": "try",
    "type": "type",
}

_resource_defaults = {
    "amazon instance": "aws_instance",
    "hetzner firewall": "hcloud_firewall",
}

resources = get_list_from_csv(
    "terraform_resources.csv",
    headers=("Resource name", "Spoken"),
    default=_resource_defaults,
)

mod.list("terraform_resource", desc="Terraform resources")
ctx.lists["self.terraform_resource"] = resources


@mod.action_class
class Actions:
    def code_terraform_block(text: str):
        """Inserts a new block of a given type (e.g. variable, output, provider...)"""


@ctx.action_class("user")
class UserActions:
    def code_terraform_block(text: str):
        argument_count = block_argument_count.get(text) or 0
        if argument_count == 0:
            actions.insert(text + ' {}')
            actions.edit.left()
        else:
            suffix = "".join([' ""'] * (argument_count - 1))
            actions.user.insert_between(text + ' "', '"' + suffix + ' {}')

    def code_block():
        actions.user.insert_between("{", "}")

    def code_operator_assignment():
        actions.insert(" = ")

    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_division():
        actions.insert(" / ")

    def code_operator_modulo():
        actions.insert(" % ")

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

    def code_insert_true():
        actions.insert("true")

    def code_insert_false():
        actions.insert("false")

    def code_operator_lambda():
        actions.insert(" => ")

    def code_insert_null():
        actions.insert("null")

    def code_insert_is_null():
        actions.insert(" == null")

    def code_insert_is_not_null():
        actions.insert(" != null")

    def code_comment_line_prefix():
        actions.insert("# ")

    def code_state_for():
        actions.user.insert_between("for ", " in")

    def code_insert_function(text: str, selection: str):
        actions.user.insert_between(text + "(", (selection or '') + ")")
