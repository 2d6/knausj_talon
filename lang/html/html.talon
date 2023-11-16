code.language: html
code.language: javascriptreact
code.language: typescriptreact
-
state tag {user.html_tag}: user.insert_html_tag("{html_tag}")
state tag open {user.html_tag}: "<{html_tag}>"
state tag void open:
    user.insert_between("<",">")
state tag close {user.html_tag}: "</{html_tag}>"
state tag void close:
    user.insert_between("</",">")
state tag name {user.html_tag}: "{html_tag}"
