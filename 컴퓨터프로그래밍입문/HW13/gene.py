import sys


def find_gene_sequence(genome, starting_markers, ending_markers):
    shortest_gene = None

    # 모든 starting marker와 ending marker를 순차적으로 검사
    for start in starting_markers:
        for end in ending_markers:
            start_len = len(start)
            end_len = len(end)

            # genome에서 시작 마커가 존재하는 위치를 찾기
            start_pos = 0
            while start_pos < len(genome):
                start_pos = genome.find(start, start_pos)
                if start_pos == -1:
                    break  # 더 이상 찾을 수 없으면 종료

                # 시작 마커가 발견되었을 때 종료 마커를 찾기
                end_pos = genome.find(end, start_pos + start_len)
                while end_pos != -1:
                    # 유전자 조건을 만족하는지 체크
                    gene_candidate = genome[start_pos:end_pos + end_len]

                    # 조건을 만족하면 가장 짧고 사전식 순으로 가장 빠른 유전자 선택
                    if shortest_gene is None or (len(gene_candidate) < len(shortest_gene)) or \
                            (len(gene_candidate) == len(shortest_gene) and gene_candidate < shortest_gene):
                        shortest_gene = gene_candidate

                    # 끝 마커 이후로 다시 찾기
                    end_pos = genome.find(end, end_pos + 1)

                # 시작 마커 이후로 다시 찾기
                start_pos = start_pos + 1

    return shortest_gene


def main():
    # genome.txt 파일을 읽기
    with open('genome.txt', 'r') as f:
        genome = f.read().replace('\n', '')  # 여러 줄을 하나로 합침

    # stdin에서 입력 받기
    starting_markers = sys.stdin.readline().strip().split()
    ending_markers = sys.stdin.readline().strip().split()

    # 유전자 서열 찾기
    result = find_gene_sequence(genome, starting_markers, ending_markers)

    # 결과 출력
    if result:
        print(result)
    else:
        print("None")


if __name__ == "__main__":
    main()
