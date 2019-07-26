'''
    Re-built the binary tree based on preorder and postorder.
'''

from utils import TreeNode, preorder_traversal, inorder_traversal


def buildTree(preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
    '''
        Method 1: In an extreme case, where preorder is [1, 2, 3, 4, 5]
        and inorder is [5, 4, 3, 2, 1], in this case we only have left subtree,
        therefore when we use index to find root the time complexity becomes
        O(n^2).
    '''
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    cut = inorder.index(root_val)
    root.left = buildTree(preorder[1:cut+1], inorder[:cut])
    root.right = buildTree(preorder[cut+1:], inorder[cut+1:])
    return root


def buildTree2(preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
    '''
        Method 2: Resolve the issue mentioned above with no additional use 
        of memory and less time complexity.
    '''
    preo, inor = list(preorder), list(inorder)
    def build(stop):
        if inor and inor[-1] != stop:
            print(preo, inor)
            root = TreeNode(preo.pop())
            root.left = build(root.val)
            inor.pop()
            root.right = build(stop)
            if root:
                print('root:', root.val)
            if stop:
                print('stop:', stop)
            print()
            return root
    preo.reverse()
    inor.reverse()
    return build(None)


# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]

# print(preorder_traversal(buildTree(preorder, inorder)))
# t1 = buildTree(preorder, inorder)
# print(preorder == preorder_traversal(t1))
# print(inorder == inorder_traversal(t1))

t3 = buildTree2(preorder, inorder)


