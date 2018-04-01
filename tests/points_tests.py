from nose.tools import *
import points.catmodule

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")

def test_cat():
    output=points.catmodule.cat(['tests/fixtures/a.txt','tests/fixtures/b.txt'])
    assert output == 'abc123'