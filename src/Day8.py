from AOCChallenge import AOCChallenge
from Types import *


class Node:
    node_count = 0

    def __init__(self, num_children, num_metadata):
        self._num_children = num_children
        self._num_metadata = num_metadata
        self._children_ids = []
        self._metadata = []
        self._value = -1
        self._id = Node.node_count
        Node.node_count += 1

    def get_num_children(self) -> int:
        return self._num_children

    def get_children_ids(self) -> ListInt:
        return self._children_ids

    def get_num_metadata(self) -> int:
        return self._num_metadata

    def get_metadata(self) -> ListInt:
        return self._metadata

    def get_sum_metadata(self, set_value=True) -> int:
        if set_value:
            self._value = sum(self._metadata)
            return self._value
        return sum(self._metadata)

    def get_id(self) -> int:
        return self._id

    def append_child_id(self, node_id: int) -> None:
        self._children_ids.append(node_id)

    def append_metadata(self, metadata: int) -> None:
        self._metadata.append(metadata)

    def set_value(self, value: int) -> None:
        self._value = value

    def get_value(self) -> int:
        return self._value

    @staticmethod
    def reset_node_count() -> None:
        Node.node_count = 0


class Day8(AOCChallenge):
    INPUT_FILENAME = "resources/day8_input.dat"

    # Public
    def __init__(self):
        super().__init__(Day8.INPUT_FILENAME, Input.SPACE_SEPARATED_INT)
        self._create_tree()

    def run_part_one(self) -> int:
        return sum([metadata for node in self._nodes for metadata in node.get_metadata()])

    def run_part_two(self) -> int:
        return self._get_node_value(0)

    # Private
    def _create_tree(self) -> None:
        Node.reset_node_count()
        self._nodes = []
        current_input = self._input
        while current_input:
            self._process_node(current_input)

    def _process_node(self, current_tree) -> Node:
        if len(current_tree) < 2:
            current_tree.clear()
            return None
        node = Node(current_tree.pop(0), current_tree.pop(0))
        self._nodes.append(node)
        self._process_children(current_tree, node)
        self._process_metadata(current_tree, node)
        return node

    def _process_children(self, current_tree, parent_node) -> None:
        for _ in range(parent_node.get_num_children()):
            child_node = self._process_node(current_tree)
            parent_node.append_child_id(child_node.get_id())

    def _process_metadata(self, current_tree, node) -> None:
        for _ in range(node.get_num_metadata()):
            node.append_metadata(current_tree.pop(0))

    def _get_node_value(self, node_id) -> int:
        node = self._nodes[node_id]
        if not node.get_num_children():
            return node.get_sum_metadata()

        node.set_value(sum([self._get_node_value(node.get_children_ids()[metadata-1]) for metadata in node.get_metadata()
                            if 0 < metadata <= node.get_num_children()]))
        return node.get_value()
