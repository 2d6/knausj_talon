app: keepassxc
-
# Database
open database: key(cmd-o)
save database: key(cmd-s)
close database: key(cmd-w)
lock database: key(cmd-l)

# Entries
[add] new entry: key(cmd-n)
clone entry: key(cmd-k)
(view | edit) entry: key(cmd-e)
delete entry: key(cmd-d)
copy user [name]: key(cmd-b)
copy password: key(cmd-c)
find: key(cmd-f)
find <user.text>:
    key(cmd-f)
    insert("{text}")
