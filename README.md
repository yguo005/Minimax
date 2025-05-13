
## Assignment Overview

This assignment involves writing a solver for the game of Tic Tac Toe using the Minimax algorithm. The goal is to implement an AI that can play optimally.

## Questions Specific to This Assignment

### 1. Score Inversion in Minimax

*   **Question:** In `solve_opponent_move()`, why do we return the opposite (negative) of the score used in the base case of `solve_my_move()`?
*   **Answer:** This is a core concept in zero-sum games handled by Minimax. The player's win is the opponent's loss, and vice-versa. If the player (maximizing player) achieves a score of +1 (win), this is equivalent to a -1 score for the opponent (minimizing player). The Minimax algorithm works by having the maximizing player try to maximize their score, and the minimizing player try to minimize the maximizing player's score (which is equivalent to maximizing their own score if scores are inverted). So, when evaluating from the opponent's perspective, their "good" outcome is the player's "bad" outcome, hence the score negation.

### 2. No Winner with Optimal Play

*   **Question:** Why is there no winner in Tic Tac Toe if both sides are playing optimally?
*   **Answer:** The 3x3 Tic Tac Toe board is small enough that its entire game tree can be explored. With optimal play from both sides, every possible winning threat can be blocked. If one player (e.g., X) makes an optimal move, the opponent (O), also playing optimally, can always make a defensive move to prevent X from creating a winning line. This leads to a draw when both players execute perfect strategies.
*   **Example Game Trace (Optimal Play):**
    *   Initial: `None|None|None` / `None|None|None` / `None|None|None`
    *   X: `X|None|None` / `None|None|None` / `None|None|None`
    *   O: `X|O|None` / `None|None|None` / `None|None|None`
    *   X: `X|O|X` / `None|None|None` / `None|None|None`
    *   O: `X|O|X` / `O|None|None` / `None|None|None`
    *   X: `X|O|X` / `O|X|None` / `None|None|None`
    *   O: `X|O|X` / `O|X|None` / `O|None|None`
    *   X: `X|O|X` / `O|X|X` / `O|None|None` (Error in transcript: X would play in `Player.O|Player.X|Player.X` in the last row, center)
    *   Corrected optimal sequence often leads to:
        *   X places center. O places corner. X places opposite corner. O blocks. etc.
    *   **Final Board from document:**
        ```
        Player.X|Player.O|Player.X
        Player.O|Player.X|Player.X
        Player.O|Player.X|Player.O
        It's a draw
        ```
    *   This demonstrates that with optimal play, the game results in a draw.

### 3. Minimax Pseudocode (Without Alpha-Beta Pruning)

*   **Question:** The assignment's pseudocode likely included alpha-beta pruning. What would be the pseudocode for implementing this same algorithm, but *without* alpha-beta pruning?
*   **Answer (Standard Minimax):**
    ```
    function minimax(node, maximizingPlayer):
        If node is a terminal node: // Game over (win, loss, or draw)
            return score of the terminal node // e.g., +1 for MAX win, -1 for MIN win (MAX loss), 0 for draw

        If maximizingPlayer:
            node.value = -infinity
            For each child of the node:
                node.value = max(node.value, minimax(child, false)) // Switch to minimizing player
            Return node.value
        Else (minimizingPlayer):
            node.value = +infinity
            For each child of the node:
                node.value = min(node.value, minimax(child, true)) // Switch to maximizing player
            Return node.value
    ```
    *Note: The document's pseudocode snippet seems to directly assign `node.value = score` for terminal nodes and uses `node.value` as an accumulator. The more common return pattern is shown above, where the function returns the score directly.*


*   **Most Difficult Part:**
    *   Understanding the role and update mechanism of `alpha`. The student felt `alpha` should be `max(alpha, node.value)` for the maximizing player during its turn, not the "smallest best_move value."
*   **Most Rewarding Part:**
    *   Practicing the implementation of the Minimax algorithm and alpha-beta pruning.
*   **What was Learned:**
    *   How to use Minimax to determine the best move at each turn and the resulting game value.
    *   How alpha-beta pruning can be used to reduce the search space by eliminating branches that won't influence the final decision.

