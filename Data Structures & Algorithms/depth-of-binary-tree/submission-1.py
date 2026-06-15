from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize a queue with the root node
        queue = deque([root])
        depth = 0
        
        # Loop while there are still nodes to process
        while queue:
            # Increment depth since we are entering a new level
            depth += 1
            
            # Process all nodes currently at this specific level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add the children of the current node to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return depth