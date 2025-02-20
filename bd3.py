from collections import deque
import re

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS traversal:", end=" ")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    print(vertex, end=" ")
    visited.add(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def input_graph():
    graph = {}
    edges = get_valid_input("Enter the number of edges: ", input_type='number')
    for _ in range(edges):
        while True:
            u, v = input("Enter edge (u v): ").split()
            if is_valid_input(u) and is_valid_input(v):
                break
            else:
                print("Invalid input. Please enter only letters and numbers.")
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def is_valid_input(value):
    return re.match("^[A-Za-z0-9]*$", value)

def get_valid_input(prompt, input_type='text'):
    while True:
        value = input(prompt)
        if input_type == 'number':
            if value.isdigit():
                return int(value)
            else:
                print("Invalid input. Please enter a number.")
        elif input_type == 'text':
            if is_valid_input(value):
                return value
            else:
                print("Invalid input. Please enter only letters and numbers.")

def main_menu():
    graph = {}
    start_vertex = None

    while True:
        print("\nMenu:")
        print("1. Input graph")
        print("2. BFS traversal")
        print("3. DFS traversal")
        print("4. Exit")
        choice = get_valid_input("Enter your choice: ", input_type='number')

        if choice == 1:
            graph = input_graph()
            start_vertex = get_valid_input("Enter the starting vertex: ", input_type='text')
        elif choice == 2:
            if graph and start_vertex:
                print("\nBFS traversal:")
                bfs(graph, start_vertex)
            else:
                print("Please input the graph and starting vertex first.")
        elif choice == 3:
            if graph and start_vertex:
                print("\nDFS traversal:")
                dfs_recursive(graph, start_vertex)
            else:
                print("Please input the graph and starting vertex first.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
