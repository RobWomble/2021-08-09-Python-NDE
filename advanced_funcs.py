def really_pretty_print(x, *args, pre="*"*16, post="-----", **kwargs):
    print(pre)
    print(x)
    for ar in args:
        print(ar)
    print("Your system settings are")
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")
    print(post)


really_pretty_print("please print this", "and this", "and this too", "oh and pick me!", pre=" &&&&&&&&& ")
really_pretty_print("x is the bomb", name="bchd", host="alta3", time="break time")
