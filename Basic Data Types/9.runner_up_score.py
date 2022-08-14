if __name__ == '__main__':
    n = int(input())
    score_ip = input()
    arr = score_ip.split()
    scores_int = [int(item) for item in arr]
    max_value = max(scores_int)
    scores_updated = [score for score in scores_int if score is not max_value]
    runner_up = max(scores_updated)
    print(runner_up)