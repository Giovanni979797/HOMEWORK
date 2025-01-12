from heapq import heappush, heappop
from typing import Dict, List, Set, Tuple
import matplotlib.pyplot as plt
import numpy as np


class PowerStation:
    def __init__(self, name: str, location: Tuple[float, float]):
        self.name = name
        self.location = location
        self.connections: Dict[str, float] = {}

class PowerGrid:
    def __init__(self):
        self.stations: Dict[str, PowerStation] = {
            'Downtown': PowerStation('Downtown', (0, 0)),
            'Northside': PowerStation('Northside', (2, 4)),
            'Westpark': PowerStation('Westpark', (-3, 1)),
            'Eastville': PowerStation('Eastville', (4, 0)),
            'Southend': PowerStation('Southend', (1, -3)),
            'Industrial': PowerStation('Industrial', (-1, -2))
        }
        self.setup_connection_costs()

    def setup_connection_costs(self):
        connections = [
            ('Downtown', 'Northside', 8500),
            ('Downtown', 'Westpark', 6200),
            ('Downtown', 'Eastville', 7800),
            ('Downtown', 'Southend', 5400),
            ('Northside', 'Westpark', 9100),
            ('Northside', 'Eastville', 6700),
            ('Westpark', 'Southend', 8300),
            ('Eastville', 'Southend', 7200),
            ('Southend', 'Industrial', 4800),
            ('Downtown', 'Industrial', 5900)
        ]
        for station1, station2, cost in connections:
            self.stations[station1].connections[station2] = cost
            self.stations[station2].connections[station1] = cost

    def optimize_connections(self) -> List[Tuple[str, str, float]]:
        visited = set()
        unvisited = set(self.stations.keys())
        mst = []
        start_station = next(iter(self.stations))
        visited.add(start_station)
        unvisited.remove(start_station)

        while unvisited:
            edges = [(s1, s2, self.stations[s1].connections[s2])
                     for s1 in visited for s2 in self.stations[s1].connections if s2 in unvisited]
            if not edges:
                break
            edge = min(edges, key=lambda x: x[2])
            mst.append(edge)
            visited.add(edge[1])
            unvisited.remove(edge[1])

        return mst

    def get_total_cost(self, mst: List[Tuple[str, str, float]]) -> float:
        return sum(cost for _, _, cost in mst)

    def display_network(self, mst: List[Tuple[str, str, float]]):
        for station1, station2, cost in mst:
            print(f"{station1} <--> {station2} : €{cost:,.2f}")

    def visualize(self, mst: List[Tuple[str, str, float]] = None):
        fig, ax = plt.subplots(figsize=(12, 8))
        x_coords = [station.location[0] for station in self.stations.values()]
        y_coords = [station.location[1] for station in self.stations.values()]
        for station_name, station in self.stations.items():
            for neighbor, cost in station.connections.items():
                neighbor_station = self.stations[neighbor]
                ax.plot([station.location[0], neighbor_station.location[0]],
                        [station.location[1], neighbor_station.location[1]],
                        'lightgray', zorder=1, linewidth=1, alpha=0.5)
        if mst:
            for station1, station2, _ in mst:
                station1_loc = self.stations[station1].location
                station2_loc = self.stations[station2].location
                ax.plot([station1_loc[0], station2_loc[0]],
                        [station1_loc[1], station2_loc[1]],
                        'green', zorder=2, linewidth=2)
        ax.scatter(x_coords, y_coords, c='red', s=100, zorder=3)
        for station_name, station in self.stations.items():
            ax.annotate(station_name, (station.location[0], station.location[1]), xytext=(5, 5), textcoords='offset points')
        if mst:
            for station1, station2, cost in mst:
                station1_loc = self.stations[station1].location
                station2_loc = self.stations[station2].location
                midpoint = np.array(station1_loc) + (np.array(station2_loc) - np.array(station1_loc)) * 0.5
                ax.annotate(f'€{cost:,.0f}', midpoint, bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        plt.title('Power Grid Network')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("\nTesting Power Grid Optimization")
    grid = PowerGrid()
    mst = grid.optimize_connections()
    if mst:
        print("Optimal power grid configuration:")
        grid.display_network(mst)
        grid.visualize(mst)
        print(f"Total installation cost: €{grid.get_total_cost(mst):,.2f}")
    else:
        print("Could not find valid power grid configuration!")
