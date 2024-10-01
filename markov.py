import collections, random, sys, textwrap


def generate_text():
    length = int(input("How many words? > "))
    source = input("What text source file? (books/poetry/report/elements) > ")
    source = f"text_sources/{source}.txt"
    # Build possibles table indexed by pair of prefix words (w1, w2)
    w1 = w2 = ''
    possibles = collections.defaultdict(list)
    lines = open(source, "r+").readlines()
    for line in lines:
        for word in line.split():
            possibles[w1, w2].append(word)
            w1, w2 = w2, word

    # Avoid empty possibles lists at end of input
    possibles[w1, w2].append('')
    possibles[w2, ''].append('')

    # Generate randomized output (start with a random capitalized prefix)
    w1, w2 = random.choice([k for k in possibles if k[0][:1].isupper()])
    output = [w1, w2]
    for _ in range(length):
        word = random.choice(possibles[w1, w2])
        output.append(word)
        w1, w2 = w2, word

    out_readable = ""
    for i in output:
        out_readable += (i + " ")

    out_readable = out_readable[:-1]
    if out_readable[-1] != ".":
        out_readable += "."
    
    print("\n", out_readable)