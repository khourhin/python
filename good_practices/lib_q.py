import q

# Check the output at /tmp/q

q("Hello")


@q.t
def sayMessage(msg):
    a_var = 12
    q(a_var)
    return(msg)

sayMessage("this is a test")
