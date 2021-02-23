from run_raindrops import *
import pytest

class Test_Class():

    ## This tests if 28 is the given number the output should be Plong
    def test_one(self):
        assert pling_plang_plong(28) == 'Plong'

    ## This tests if 30 is the given number the output should be Pling
    def test_two(self):
        assert pling_plang_plong(30) == 'PlingPlang'

    ## This tests if 34 is the given number the output should be 34
    def test_three(self):
        assert pling_plang_plong(34) == 34