from __future__ import annotations

import os
from typing import Union, Any, List


class Node:
    parent_node = None
    _location = ''

    def __init__(self, name: str):
        self.name = name

    def show(self):
        """Returns structure of sub-tree starting with current node"""
        pass

    def search(self, target_name: str) -> List[Node]:
        """Returns all nodes of current nodes sub-tree with corresponding name

        :param target_name: name to search for
        :returns: list of suitable nodes or None if there are no such nodes"""
        pass


class LeafNode(Node):
    """Last node of its branch. Has no child nodes"""

    @classmethod
    def _generate_id(cls):
        """Returns id for a new object """
        if not hasattr(cls, 'last_id'):
            cls.last_id = 1
        else:
            cls.last_id += 1
        return cls.last_id

    def __str__(self):
        return f'{self.location}'

    def __repr__(self):
        return f'"{self.location}"'

    def __init__(self, name: str, value: Any = None):
        super().__init__(name)
        self.id = self._generate_id()

    def show(self):
        return self.name

    def search(self, target_name: str) -> List[LeafNode]:
        if self.name == target_name:
            return [self]
        return []

    def set_parent_node(self, parent_node):
        self.parent_node = parent_node
        self._location = f'{parent_node.location}/{self.name}'

    @property
    def location(self):
        """Returns absolute path to current node in tree"""
        return f'{self._location}'


class BranchNode:
    def __init__(self, name: str):
        self.name = name
        self.parent_node = None
        self.child_objects = []

    def __str__(self):
        return f'{self.location}'

    def __repr__(self):
        return f'"{self.location}"'

    def show(self):
        out = '\n'.join([child.show() for child in self.child_objects])
        arr = [f'--{line}' for line in out.splitlines() if line]
        out = '\n'.join(arr)

        out = f'{self.name}\n{out}'
        # TODO: beautify
        return out

    def add(self, child_object: Union[BranchNode, LeafNode]):
        self.child_objects.append(child_object)
        child_object.set_parent_node(self)

    def search(self, target_name: str) -> List[Union[BranchNode, LeafNode]]:
        out = []
        for child in self.child_objects:
            search_result = child.search(target_name)
            if search_result is not None:
                out.extend(search_result)

        if self.name == target_name: 
            out.append(self)

        out = [search_result for search_result in out]

        return out

    @property
    def location(self):
        parent_location = '' if self.parent_node is None else f'{self.parent_node.location}/'
        return f'{parent_location}{self.name}'


belarus = BranchNode('Belarus')

hrodna_reg = BranchNode('Hrodna region')
minsk_reg = BranchNode('Minsk region')

hrodna_city = BranchNode('Hrodna')
shchuchin_city = BranchNode('Schuchin')

lenin_district = BranchNode('Lenin District')

b_troickaya_st = BranchNode('Bolshaya Troitskaya st.')
sovetskaya_st = BranchNode('Sovetskaya st.')

b_troickaya_st_4 = BranchNode('4')
sovetskaya_st_4 = BranchNode('4')

b_troickaya_st_4_1st_floor = BranchNode('1st floor')
b_troickaya_st_4_2nd_floor = BranchNode('2nd floor')
sovetskaya_st_4_1st_floor = BranchNode('1st floor')

b_troickaya_st_4_1st_floor_4th_office = BranchNode('Office 4')
b_troickaya_st_4_1st_floor_6th_office = BranchNode('Office 6')
sovetskaya_st_4_1st_floor_2nd_office = BranchNode('Office 2')

b_troickaya_st_4_1st_floor_4th_office_4th_sensor = LeafNode('Sensor 4')
b_troickaya_st_4_1st_floor_4th_office_5th_sensor = LeafNode('Sensor 5')
b_troickaya_st_4_1st_floor_6th_office_1st_sensor = LeafNode('Sensor 1')
sovetskaya_st_4_1st_floor_2nd_office_1st_sensor = LeafNode('Sensor 1')

b_troickaya_st_4_1st_floor_4th_office.add(b_troickaya_st_4_1st_floor_4th_office_4th_sensor)
b_troickaya_st_4_1st_floor_4th_office.add(b_troickaya_st_4_1st_floor_4th_office_5th_sensor)
b_troickaya_st_4_1st_floor_6th_office.add(b_troickaya_st_4_1st_floor_6th_office_1st_sensor)
sovetskaya_st_4_1st_floor_2nd_office.add(sovetskaya_st_4_1st_floor_2nd_office_1st_sensor)

b_troickaya_st_4_1st_floor.add(b_troickaya_st_4_1st_floor_4th_office)
b_troickaya_st_4_1st_floor.add(b_troickaya_st_4_1st_floor_6th_office)
sovetskaya_st_4_1st_floor.add(sovetskaya_st_4_1st_floor_2nd_office)

b_troickaya_st_4.add(b_troickaya_st_4_1st_floor)
b_troickaya_st_4.add(b_troickaya_st_4_2nd_floor)
sovetskaya_st_4.add(sovetskaya_st_4_1st_floor)

b_troickaya_st.add(b_troickaya_st_4)
sovetskaya_st.add(sovetskaya_st_4)

lenin_district.add(b_troickaya_st)
lenin_district.add(sovetskaya_st)

hrodna_city.add(lenin_district)

hrodna_reg.add(hrodna_city)
hrodna_reg.add(shchuchin_city)

belarus.add(hrodna_reg)
belarus.add(minsk_reg)

search_hrodna = belarus.search('Hrodna')
search_4 = belarus.search('4')
search_sensor_1 = belarus.search('Sensor 1')
search_sensor_3 = belarus.search('Sensor 3')

belarus_show = belarus.show()
hrodna_show = hrodna_city.show()

print(search_hrodna)
print(search_4)
print(search_sensor_1)
print(search_sensor_3)
print(os.path.basename(str(search_sensor_1[0])))

print('\n\n\n')
print(belarus_show)
print('\n\n\n')
print(hrodna_show)

