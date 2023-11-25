import codewars_test as test
from solution import is_perfect, TreeNode

def do_test (tree : TreeNode, expected : bool):
    log = f'for tree:\n{tree}\n'
    actual = is_perfect(tree)
    test.assert_equals(actual, expected, log)

@test.describe("sample tests")
def sample_tests():
    @test.it("empty tree")
    def empty_tree():
        do_test(None, True)

    @test.it("leaf tree")
    def leaf_tree():
        do_test(TreeNode('A'), True)

    @test.it("perfect 1 level")
    def perfect_1_level():
        do_test(
            TreeNode('A',
                TreeNode('B'),
                TreeNode('C')
            )
        , True)

    @test.it("perfect 2 levels")
    def perfect_2_levels():
        do_test(
            TreeNode('A',
                TreeNode('B',
                    TreeNode('D'),
                    TreeNode('E')
                ),
                TreeNode('C',
                    TreeNode('F'),
                    TreeNode('G')
                )
            )
        , True)

    @test.it("one child")
    def one_child():
        do_test(TreeNode('A', TreeNode('B')), False)

    @test.it("full nonperfect tree")
    def full_nonperfect():
        do_test( TreeNode('A',
                TreeNode('B',
                    TreeNode('D'),
                    TreeNode('E')
                ),
                TreeNode('C')
            )
        , False)

    @test.it("balanced nonperfect")
    def balanced_nonperfect():
        do_test(
            TreeNode('A',
                TreeNode('B',
                    TreeNode('D'),
                ),
                TreeNode('C',
                    TreeNode('F'),
                )
            )
        , False)

