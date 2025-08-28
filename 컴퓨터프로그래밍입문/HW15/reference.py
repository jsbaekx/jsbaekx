import sys
import re

def main():
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    text = '\n'.join(input_lines[1:])  # 줄바꿈 유지하여 결합

    # 줄바꿈 포함 대괄호 안 숫자들을 매칭하는 정규표현식
    pattern = re.compile(r'\[\s*([\d\s,]+?)\s*\]', re.DOTALL)

    cited = set()

    for match in pattern.finditer(text):
        content = match.group(1)
        # 공백 제거하고 숫자 추출
        numbers = re.findall(r'\d+', content)
        for num in numbers:
            cited.add(int(num))

    # 범위 내인데 한번도 언급되지 않은 번호
    missing = [i for i in range(1, k+1) if i not in cited]
    # k를 초과한 번호
    exceeded = [i for i in cited if i > k]

    errors = sorted(missing + exceeded)

    if errors:
        for e in errors:
            print(e)
    else:
        print(0)

if __name__ == "__main__":
    main()
