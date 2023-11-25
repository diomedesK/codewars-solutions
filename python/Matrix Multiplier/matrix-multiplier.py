import codewars_test as test

from solution import get_matrix_product

@test.describe("Sample tests")
def sample_tests():
    @test.it("Handles multiplication of 1x1 matrices.")
    def _():
        test.assert_equals(get_matrix_product([[2]], [[3]]), [[6]])

    @test.it("Handles multiplication of 2x2 matrices.")
    def _():
        test.assert_equals(get_matrix_product([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

    @test.it("Handles multiplication of matrices including decimals.")
    def _():
        test.assert_equals(get_matrix_product([[0.5, 1],[1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]), [[0.7, 1.0], [1.5, 2.2]])

    @test.it("Returns None if matrices cannot be multiplied.")
    def _():
        test.assert_equals(get_matrix_product([[1, 2], [3, 4]], [[2, 4]]), None)
