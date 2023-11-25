import codewars_test as test
from solution import ips_between

test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)
