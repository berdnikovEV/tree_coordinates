import unittest

from nodes import BranchNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_generate_id(self):
        LeafNode.last_id = 999
        assert LeafNode('test').id == 1000

    def test_show(self):
        branch_node = BranchNode('Branch level 1')
        leaf_node = LeafNode('Leaf')
        branch_node.add(leaf_node)

        assert leaf_node.show() == 'Leaf'

    def test_search(self):
        leaf_node = LeafNode('Leaf')

        assert leaf_node.search('Leaf') == [leaf_node]
        assert leaf_node.search('Test') == "No nodes found"
        assert leaf_node.search('Test', is_final=False) == []

    def test_location(self):
        branch_node = BranchNode('Branch')
        leaf_node = LeafNode('Leaf')

        branch_node.add(leaf_node)

        assert leaf_node.location == 'Branch/Leaf'


class TestBranchNode(unittest.TestCase):
    def test_add_branch_node(self):
        branch_level_1 = BranchNode('Level 1')
        branch_level_2 = BranchNode('Level 2')
        branch_level_1.add(branch_level_2)

        assert branch_level_2.parent_node == branch_level_1
        assert branch_level_2 in branch_level_1.child_nodes

    def test_add_leaf_node(self):
        branch_node = BranchNode('Branch level 1')
        leaf_node = LeafNode('Leaf')
        branch_node.add(leaf_node)

        assert leaf_node.parent_node == branch_node
        assert leaf_node in branch_node.child_nodes

    def test_show(self):
        branch_level_1 = BranchNode('Branch level 1')
        branch_level_2 = BranchNode('Branch level 2')

        branch_level_1.add(branch_level_2)

        big_tree = branch_level_1.show()
        small_tree = branch_level_2.show()

        assert big_tree == 'Branch level 1\n--Branch level 2'
        assert small_tree == 'Branch level 2'

    def test_search_multiple_results(self):
        branch_level_1 = BranchNode('Branch level 1')
        branch_level_1.add(BranchNode('Branch level 2'))
        branch_level_1.add(BranchNode('Branch level 2'))
        branch_level_1.add(BranchNode('Branch level 2'))

        search_results = branch_level_1.search('Branch level 2')

        assert len(search_results) == 3
        for branch in search_results:
            assert branch.name == 'Branch level 2'

    def test_search_single_result(self):
        branch_level_1 = BranchNode('Branch level 1')
        branch_level_1.add(BranchNode('Branch level 2'))
        branch_level_1.add(BranchNode('Branch level 2 with changes'))
        branch_level_1.add(BranchNode('Branch level 2 with more changes'))

        search_results = branch_level_1.search('Branch level 2')

        assert len(search_results) == 1
        assert search_results[0].name == 'Branch level 2'

    def test_search_no_results(self):
        branch_level_1 = BranchNode('Branch level 1')
        branch_level_1.add(BranchNode('Branch level 2'))
        branch_level_1.add(BranchNode('Branch level 2 with changes'))

        search_results = branch_level_1.search('Branch level 99')

        assert search_results == "No nodes found"

    def test_location(self):
        branch_level_1 = BranchNode('Branch level 1')
        branch_level_2 = BranchNode('Branch level 2')

        branch_level_1.add(branch_level_2)

        assert branch_level_1.location == 'Branch level 1'
        assert branch_level_2.location == 'Branch level 1/Branch level 2'
