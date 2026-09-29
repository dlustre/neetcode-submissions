class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        # keep a queue of rotten cells
        # for each rotten cell, make adjacent cells rotten and add each conversion to queue
        # increment a time variable

        result = 0
        queue = deque()
        num_fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                
                if grid[i][j] == 1:
                    num_fresh += 1

        deltas = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        if num_fresh == 0:
            return result

        while queue:
            new_queue = deque()

            for i, j in queue:
                for delta_i, delta_j in deltas:
                    neighbor_i = i + delta_i
                    neighbor_j = j + delta_j

                    if not (0 <= neighbor_i <= len(grid) - 1):
                        continue
                    
                    if not (0 <= neighbor_j <= len(grid[0]) - 1):
                        continue
                    
                    if grid[neighbor_i][neighbor_j] != 1:
                        continue

                    grid[neighbor_i][neighbor_j] = 2
                    num_fresh -= 1

                    new_queue.append((neighbor_i, neighbor_j))
            
            queue = new_queue
            result += 1

            if num_fresh == 0:
                return result

        return -1