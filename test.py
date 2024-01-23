from x7 import check as c

def test(avs, b):
    c(avs, b)
    host = avs+b
    assert host == c(avs, b)


test(avs=14, b=20)
test(avs=14, b=26)
test(avs=14, b=28)