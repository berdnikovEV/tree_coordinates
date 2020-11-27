from __future__ import annotations

from typing import Union, List


class Node:
    parent_node = None

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.location}'

    def __repr__(self):
        return f'"{self.location}"'

    def show(self):
        """Returns structure of sub-tree starting with current node"""
        pass

    def search(self, target_name: str, is_final: bool = True) -> Union[List[LeafNode], str]:
        """Returns all nodes of current nodes sub-tree with corresponding name

        :param target_name: name to search for
        :param is_final: if True returns message when no results are found
        :returns: list of suitable nodes or None if there are no such nodes"""
        pass

    @property
    def location(self):
        """Path to current node in tree"""
        parent_location = f'{self.parent_node.location}/' if self.parent_node else ''
        return f'{parent_location}{self.name}'


class LeafNode(Node):
    """Last node of its branch. Has no child nodes"""
    @classmethod
    def _generate_id(cls):
        """Returns id for a new object """
        if not hasattr(cls, 'last_id'):
            cls.last_id = 0
        else:
            cls.last_id += 1
        return cls.last_id

    def __init__(self, name: str):
        super().__init__(name)
        self.id = self._generate_id()

    def show(self):
        """Returns structure of sub-tree starting with current node"""
        return self.name

    def search(self, target_name: str, is_final: bool = True) -> Union[List[LeafNode], str]:
        """Returns all nodes of current nodes sub-tree with corresponding name

        :param target_name: name to search for
        :param is_final: if True returns message when no results are found
        :returns: list of suitable nodes or None if there are no such nodes"""

        if self.name == target_name:
            return [self]

        if is_final:
            return "No nodes found"

        return []


class BranchNode(Node):
    def __init__(self, name: str):
        super().__init__(name)
        self.parent_node = None
        self.child_nodes = []

    def show(self):
        """Returns structure of sub-tree starting with current node"""
        child_show_results = '\n'.join([child.show() for child in self.child_nodes])
        if child_show_results:
            child_tree_elements = [f'--{line}' for line in child_show_results.splitlines()]
            child_structure = '\n'.join(child_tree_elements)

            full_tree_structure = f'{self.name}\n{child_structure}'
        else:
            full_tree_structure = f'{self.name}'

        return full_tree_structure

    def add(self, child_object: Union[BranchNode, LeafNode]):
        self.child_nodes.append(child_object)
        child_object.parent_node = self

    def search(self, target_name: str, is_final: bool = True) -> Union[List[Node], str]:
        """Returns all nodes of current nodes sub-tree with corresponding name

        :param target_name: name to search for
        :param is_final: if True returns message when no results are found
        :returns: list of suitable nodes or None if there are no such nodes"""
        search_results = []
        for child in self.child_nodes:
            search_result = child.search(target_name, is_final=False)
            if search_result is not None:
                search_results.extend(search_result)

        if self.name == target_name: 
            search_results.append(self)

        if is_final and not search_results:
            return "No nodes found"

        return search_results

