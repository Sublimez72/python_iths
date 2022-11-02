import solution_with_np

assert solution_with_np.solution(1, 1) == "1"
assert solution_with_np.solution(1, 2) == "2"
assert solution_with_np.solution(1, 3) == "4"
assert solution_with_np.solution(1, 4) == "7"
assert solution_with_np.solution(1, 5) == "11"
assert solution_with_np.solution(1, 6) == "16"
assert solution_with_np.solution(1, 7) == "22"
assert solution_with_np.solution(1, 8) == "29"

assert solution_with_np.solution(2, 1) == "3"

assert solution_with_np.solution(3, 1) == "6"
assert solution_with_np.solution(3, 2) == "9"

assert solution_with_np.solution(4, 1) == "10"

assert solution_with_np.solution(5, 1) == "15"
assert solution_with_np.solution(5, 10) == "96"
