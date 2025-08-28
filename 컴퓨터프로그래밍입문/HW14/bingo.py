# bingo.py
import numpy as np

def read_input():
    """표준 입력으로부터 0과 1로 이루어진 문자열을 읽어 2D numpy 배열로 반환"""
    lines = [line.strip() for line in sys.stdin if line.strip()]
    arr = np.array([[int(ch) for ch in line] for line in lines])
    return arr

def max_run_length(arr):
    max_len = 0
    count = 0

    def process_line(line):
        nonlocal max_len, count
        current = 0
        for val in line:
            if val == 1:
                current += 1
                if current > max_len:
                    max_len = current
                    count = 1
                elif current == max_len:
                    count += 1
            else:
                current = 0

def main():
    arr = read_input()
    max_len, count = max_run_length(arr)
    print(f"{max_len} {count}")

if __name__ == "__main__":
    main()
