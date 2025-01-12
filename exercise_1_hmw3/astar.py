from heapq import heappush, heappop
import matplotlib.pyplot as plt
import numpy as np
import heapq
from typing import List, Tuple, Optional

class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

class MuseumEvacuation:
    def __init__(self):
        self.layout = [
            ['0', '0', '1', '0', 'E'],
            ['0', '1', '0', '1', '0'],
            ['P', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def find_person_and_exits(self) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
        person_pos = None
        exits = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.layout[row][col] == 'P':
                    person_pos = (row, col)
                elif self.layout[row][col] == 'E':
                    exits.append((row, col))
        return person_pos, exits

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for d in directions:
            new_row, new_col = position[0] + d[0], position[1] + d[1]
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.layout[new_row][new_col] != '1':
                    neighbors.append((new_row, new_col))
        return neighbors

    def find_evacuation_path(self) -> Optional[List[Tuple[int, int]]]:
        start, exits = self.find_person_and_exits()
        if not start or not exits:
            return None

        open_list = []
        heapq.heappush(open_list, Node(start))
        closed_list = set()

        while open_list:
            current_node = heapq.heappop(open_list)
            closed_list.add(current_node.position)

            if current_node.position in exits:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            for neighbor_pos in self.get_neighbors(current_node.position):
                if neighbor_pos in closed_list:
                    continue

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = min(self.manhattan_distance(neighbor_pos, exit_pos) for exit_pos in exits)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                heapq.heappush(open_list, neighbor_node)
        return None

    def display_path(self, path: List[Tuple[int, int]]):
        for row, col in path:
            if self.layout[row][col] == '0':
                self.layout[row][col] = '.'
        for row in self.layout:
            print(' '.join(row))

    def visualize(self, path: List[Tuple[int, int]] = None):
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.cm.colors.ListedColormap(['#FFFFFF', '#404040', '#FF4444', '#4444FF', '#FFCC00'])
        numeric_layout = np.zeros((self.rows, self.cols))
        text_annotations = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == '1':
                    numeric_layout[i][j] = 1
                    text_annotations.append((i, j, ''))
                elif self.layout[i][j] == 'E':
                    numeric_layout[i][j] = 2
                    text_annotations.append((i, j, 'EXIT'))
                elif self.layout[i][j] == 'P':
                    numeric_layout[i][j] = 3
                    text_annotations.append((i, j, 'P'))
                else:
                    text_annotations.append((i, j, ''))
        if path:
            for row, col in path[1:-1]:
                numeric_layout[row][col] = 4
                text_annotations.append((row, col, '→'))
        im = ax.imshow(numeric_layout, cmap=cmap)
        for i in range(self.rows + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(self.cols + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)
        for i, j, text in text_annotations:
            if text:
                color = 'white' if numeric_layout[i, j] in [1, 2, 3] else 'black'
                ax.text(j, i, text, ha='center', va='center', color=color, fontweight='bold', fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#FFFFFF', edgecolor='black', label='Free Space'),
            Patch(facecolor='#404040', edgecolor='black', label='Wall'),
            Patch(facecolor='#FF4444', edgecolor='black', label='Exit'),
            Patch(facecolor='#4444FF', edgecolor='black', label='Person'),
        ]
        if path:
            legend_elements.append(Patch(facecolor='#FFCC00', edgecolor='black', label='Path'))
        ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.05, 0.5), title='Legend', frameon=True, fontsize='small')
        plt.title('Museum Layout', pad=10)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("Testing Museum Evacuation System")
    museum = MuseumEvacuation()
    path = museum.find_evacuation_path()
    if path:
        print("Evacuation path found!")
        museum.display_path(path)
        museum.visualize(path)
    else:
        print("No evacuation path available!")
