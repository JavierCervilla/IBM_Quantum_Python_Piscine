#!/usr/bin/env python3

class Evaluator:
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        return sum([c * len(w) for c, w in zip(coefs, words)])

    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        return sum([coefs[i] * len(w) for i, w in enumerate(words)])

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    x = Evaluator.zip_evaluate(coefs, words)
    print(x)
    x = Evaluator.enumerate_evaluate(coefs, words)
    print(x)
    words = ["Le", "Lorem", "Ipsum", "n`", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    x = Evaluator.enumerate_evaluate(coefs, words)
    print(x)