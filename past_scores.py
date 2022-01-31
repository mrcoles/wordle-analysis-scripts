from common import words


TODAY_INDEX = 221  # Jan 30, 2022


def run(guess: str, day_index=TODAY_INDEX):
    for word in words[: day_index + 1]:
        vs = visual_score(guess, word)
        print(vs)


#

GRAY = "⬜"
GREEN = "🟩"
YELLOW = "🟨"


def visual_score(guess, word):
    result = [GRAY for _ in range(5)]

    g_rest_tuples = []
    w_rest = set()

    for i, (g_l, w_l) in enumerate(zip(guess, word)):
        if g_l == w_l:
            result[i] = GREEN
        else:
            g_rest_tuples.append((i, g_l))
            w_rest.add(w_l)

    for i, g_l in g_rest_tuples:
        if g_l in w_rest:
            w_rest.remove(g_l)
            result[i] = YELLOW

    return "".join(result)


#


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="output the emoji match visual for each answer from previous days against the given guess"
    )
    parser.add_argument(
        "-d",
        "--day",
        type=int,
        default=TODAY_INDEX,
        help=f"go up to this day index (inclusive) (defaults to {TODAY_INDEX})",
    )
    parser.add_argument(
        "guess",
        help="the guess (must be 5-letters)",
    )
    args = parser.parse_args()
    guess = args.guess
    assert len(guess) == 5, f"Invalid guess, must be len 5"
    run(guess.lower(), args.day)


if __name__ == "__main__":
    main()
