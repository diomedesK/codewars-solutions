import codewars_test as test
from solution import rotate

@test.describe("Example Tests")
def test_group():
    @test.it("Test a matrix with equal numbers of rows/cols")
    def test_case():       
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3,6,9],[2,5,8],[1,4,7]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[7,4,1],[8,5,2],[9,6,3]])
        test.assert_equals(rotate(rotate(matrix, 'counter-clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])
        test.assert_equals(rotate(rotate(rotate(rotate(matrix, 'clockwise'), 'clockwise'), 'clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])

    @test.it("Test a matrix with unequal number of rows/cols")
    def test_case():  
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]]

        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3,6,9,12],[2,5,8,11],[1,4,7,10]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[10,7,4,1],[11,8,5,2],[12,9,6,3]])

    @test.it("Test a matrix with only one row/col")
    def test_case(): 
        matrix = [[1,2,3]]
        
        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[3],[2],[1]])
        test.assert_equals(rotate(matrix, 'clockwise'), [[1],[2],[3]])
        test.assert_equals(rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3,2,1]])

    @test.it("Test a single cell matrix")
    def test_case(): 
        matrix = [[1]]
        
        test.assert_equals(rotate(matrix, 'counter-clockwise'), [[1]])
