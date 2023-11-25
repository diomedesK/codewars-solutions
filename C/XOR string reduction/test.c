#include <stdbool.h>
#include <criterion/criterion.h>

static void do_test (const char *string, bool expected);

Test(tests_suite, sample_tests)
{
	do_test("1 0 0 1 0", 0);
	do_test("1 0 1 1 1 0 0 1 0 0 0 0", 1);
	do_test("1 0 0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0", 0);
	do_test("1", 1);
	do_test("0", 0);
	do_test("0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 1 1 1 1 0", 0);
}

extern bool X (const char *bitstring);

static void do_test (const char *bitstring, bool expected)
{
	bool actual = X(bitstring);
	cr_assert_eq(actual, expected,
		"expected %d, but got %d, for string:\n\"%s\"",
		expected, actual, bitstring
	);
}

