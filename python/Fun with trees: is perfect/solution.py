# pyright: reportGeneralTypeIssues=false

# preloaded TreeNode class:
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right
# In a perfect tree, the sum of the amount of leaves in the depth D will equal the ( sum of all the leaves in the previous layers MINUS 1 )

def traverseNode(tree : TreeNode, depths, depth = 0) -> [int]:
    if tree == None:
        return

    if len(depths) < depth + 1:
        depths.append(0)

    depths[depth] += 1

    traverseNode(tree.left, depths, depth + 1)
    traverseNode(tree.right, depths, depth + 1)

    return depths

def is_perfect(tree : TreeNode) -> bool:
    if tree == None:
        return True

    depths = traverseNode(tree, [])
    return  sum( depths[:len(depths) - 1] ) == depths[-1] - 1
