#!/usr/bin/env python3

"""Write (at least one) test for a function you have written, or some code you write now."""


def twinkle(sw="twinkle"):

    if sw == "twinkle":
        return "How I wonder what you are!"
    else:
        return "Get outta here...."

def test_twinkle_pass():
    
    assert twinkle("twinkle") == "How I wonder what you are!"

def test_twinkle_fail():
    
    assert twinkle("poland") == "Get outta here...."
