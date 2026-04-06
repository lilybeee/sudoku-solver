import os, sys
import pycosat as pc

def solve_sudoku():
    if len(sys.argv) < 2:
        return

    input_file = sys.argv[1]
    output_path = os.path.join(os.path.dirname(os.path.abspath(input_file)), "output.txt")

    def get_id(row, col, value):
        return (row * 9 + col) * 9 + value

    with open(input_file, 'r') as f:
        lines = f.readlines()

    answers = []

    for line in lines:
        line = line.strip()[:81]
        if not line:
            continue
        clauses = []

        #condition 1
        for row in range(9):
            for col in range(9):
                clauses.append([get_id(row, col, v) for v in range(1, 10)])

        #condition 2
        for row in range(9):
            for col in range(9):
                for v1 in range(1, 10):
                    for v2 in range(v1+1, 10):
                        clauses.append([-get_id(row, col, v1), -get_id(row, col, v2)])

        #condition 3
        for row in range(9):
            for v in range(1, 10):
                clauses.append([get_id(row, col, v) for col in range(9)])  
                for col1 in range(9):
                    for col2 in range(col1+1, 9):
                        clauses.append([-get_id(row, col1, v), -get_id(row, col2, v)])

        #condition 4
        for col in range(9):
            for v in range(1, 10):
                clauses.append([get_id(row, col, v) for row in range(9)])
                for row1 in range(9):
                    for row2 in range(row1+1, 9):
                        clauses.append([-get_id(row1, col, v), -get_id(row2, col, v)])

        #condition 5
        for v in range(1, 10):
            for br in range(3):
                for bc in range(3):
                    box = [ 
                        get_id(br*3 + r, bc*3 + c, v)
                        for r in range(3) for c in range(3)
                    ]
                    clauses.append(box)
                    for i in range(len(box)):
                        for j in range(i+1, len(box)):
                            clauses.append([-box[i], -box[j]])

        #condition 6   
        for i, char in enumerate(line):
            if char.isdigit() and char != '0':
                r,c = i//9,i%9
                clauses.append([get_id(r, c, int(char))])

        result = pc.solve(clauses)

        if isinstance(result, list):
            res_chars = [''] * 81
            for lit in result:
                if lit > 0:
                    val = (lit - 1) % 9 + 1
                    idx = (lit - 1) // 9
                    res_chars[idx] = str(val)
            answers.append("".join(res_chars))
        else:
            answers.append("No solution found")

    with open(output_path, 'w') as f:
        f.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    solve_sudoku()