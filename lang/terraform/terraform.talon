code.language: terraform
-
tag(): user.code_comment_block_c_like
tag(): user.code_comment_line
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_imperative
tag(): user.code_operators_assignment
tag(): user.code_operators_lambda
tag(): user.code_operators_math
tag(): user.code_functions_common

black <user.terraform_block_name>:
    user.code_terraform_block("{terraform_block_name}")

resource {user.terraform_resource} [<user.text>]:
    user.insert_between('resource "{terraform_resource}" "{user.formatted_text(text or "", "SNAKE_CASE")}', '" {}')
data source {user.terraform_resource} [<user.text>]:
    user.insert_between('resource "{terraform_resource}" "{user.formatted_text(text or "", "SNAKE_CASE")}', '" {}')
variable [<user.text>]:
    user.insert_between('variable "{user.formatted_text(text or "", "SNAKE_CASE")}', '" {}')
output [<user.text>]:
    user.insert_between('output "{user.formatted_text(text or "", "SNAKE_CASE")}', '" {}')


reference {user.terraform_resource} [<user.text>]:
    "{terraform_resource}.{user.formatted_text(text or '', 'SNAKE_CASE')}"
reference data [source] {user.terraform_resource} [<user.text>]:
    "data.{terraform_resource}.{user.formatted_text(text or '', 'SNAKE_CASE')}"
reference variable [<user.text>]:
    "var.{user.formatted_text(text or '', 'SNAKE_CASE')}"
reference local [<user.text>]:
    "local.{user.formatted_text(text or '', 'SNAKE_CASE')}"
reference module [<user.text>]:
    "module.{user.formatted_text(text or '', 'SNAKE_CASE')}"

prop <user.terraform_common_property>:
    insert("{terraform_common_property}")
    user.code_operator_assignment()

type {user.code_type}: insert("{code_type}")

