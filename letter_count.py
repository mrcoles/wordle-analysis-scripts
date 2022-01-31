import collections

from common import words, NON_ANSWERS_START

ALL_LEN = len(words)
ANSWERS_LEN = NON_ANSWERS_START

A_ORD = ord("a")


def run():
    history_all = collections.defaultdict(int)
    history_answers = collections.defaultdict(int)

    for i, word in enumerate(words):
        for c in word:
            history_all[c] += 1
            if i < NON_ANSWERS_START:
                history_answers[c] += 1

    print("letter", "all", "answers", "diff", sep="\t")

    for i in range(A_ORD, A_ORD + 26):
        c = chr(i)
        h_all = history_all[c] / ALL_LEN / 5
        h_ans = history_answers[c] / ANSWERS_LEN / 5
        print(
            c,
            h_all,
            h_ans,
            h_ans - h_all,
            sep="\t",
        )


#


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Calculate the frequency histograms of each letter in both the full dictionary and also the answers list."
    )
    parser.parse_args()
    run()


if __name__ == "__main__":
    main()
