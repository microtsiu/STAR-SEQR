import unittest
import os
import sys
sys.path.insert(0, '../')
import starseqr_utils as su

path = os.path.dirname(__file__)
if path != '':
    os.chdir(path)


class CrossHomologyTestCase(unittest.TestCase):
    '''Tests cross homology'''

    def test_crosshom_v1(self):
        """test homology paired.fastq TUBA1B--TUBA1A test case"""
        res1 = su.cross_homology.get_cross_homology('chr12:49521770:-:chr12:49578857:-:6:0')
        # print(res1)
        assert(res1 == (.75, 1.0))

    def test_crosshom_v2(self):
        """test homology paired.fastq no reads in fastq test case"""
        res1 = su.cross_homology.get_cross_homology('chr2:131389025:+:chr2:131996848:+:0:4')
        # print(res1)
        assert(res1 == (0, 0))

    def test_crosshom_v3(self):
        """test homology TRIM46--TMEM161A--a known FP with borderline homology """
        res1 = su.cross_homology.get_cross_homology('1:155152411:+:19:19243318:-:1:0')
        # print(res1)
        assert(res1 == (0.0, 0.5))

    def test_crosshom_v4(self):
        """test homology a known TP with borderline homology """
        res1 = su.cross_homology.get_cross_homology('5:149206449:+:1:156848913:pos:1:0')
        # print(res1)
        assert(res1 == (0.0, 0.0))


if __name__ == '__main__':
    unittest.main()
