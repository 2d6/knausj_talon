os: linux
tag: user.kde
-
^desk one: key("super-1")
^desk two: key("super-2")
^desk three: key("super-3")
^desk four: key("super-4")

^desk last: key("super-ctrl-left")
^desk next: key("super-ctrl-right")

snap max: key("super-up")

^window move desk one: key("super-ctrl-1")
^window move desk two: key("super-ctrl-2")
^window move desk three: key("super-ctrl-3")
^window move desk four: key("super-ctrl-4")
^window move desk last: key("ctrl-alt-shift-left")
^window move desk next: key("ctrl-alt-shift-right")

computer end program: key("alt-f4")

window next: key("alt-`")
window last: key("alt-~")

#computer fuck:
#  key("alt-f2")
#  sleep(50ms)
#  insert("bash -c 'echo bar | xsel -b'")
#  key("enter")
