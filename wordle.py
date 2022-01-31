import time

from common import words, NON_ANSWERS_START

DEFAULT_LIMIT = -1
DEFAULT_LIMIT_OUTPUT = 200


def run(
    answers_only=False, limit_input=DEFAULT_LIMIT, limit_output=DEFAULT_LIMIT_OUTPUT
):
    guesses = words if limit_input < 0 else words[:limit_input]
    sources = guesses[:NON_ANSWERS_START] if answers_only else guesses

    start = time.time()
    scores_to_word = [
        ([sum(vals) for vals in zip(*(_score(w1, w2) for w2 in sources))], w1)
        for w1 in guesses
    ]
    end = time.time()
    total = len(guesses) * len(sources)
    dur = end - start
    print(f"{total} in {dur}s = {total / dur}ops/s")

    scores_to_word.sort(reverse=True)

    if limit_output >= 0:
        scores_to_word = scores_to_word[:limit_output]

    for i, (scores, word) in enumerate(scores_to_word):
        print(f"{i + 1}.", word, *scores, sep="\t")


def _score(w1, w2):
    g = 0
    y = 0

    rw1 = []
    rw2 = []

    # check for exact matches
    for i, (c1, c2) in enumerate(zip(w1, w2)):
        if c1 == c2:
            g += 1
        else:
            rw1.append(c1)
            rw2.append(c2)

    # check for other matches
    for c1 in rw1:
        if c1 in rw2:
            rw2.remove(c1)
            y += 1

    return (g + y, g, y)


#


def main():
    import argparse

    parser = argparse.ArgumentParser(description="wordle analysis")
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="limit input words list (for testing)",
    )
    parser.add_argument(
        "-o",
        "--limit-output",
        type=int,
        default=DEFAULT_LIMIT_OUTPUT,
        help=f"limit output length (defaults to {DEFAULT_LIMIT_OUTPUT}, set to -1 to output everything)",
    )
    parser.add_argument(
        "-a",
        "--answers",
        action="store_true",
        default=False,
        help="compare guesses against answers only",
    )
    args = parser.parse_args()
    run(args.answers, args.limit, args.limit_output)


if __name__ == "__main__":
    main()
