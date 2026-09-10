"""Reproducible descriptive statistics and regression using only the stdlib."""

from math import sqrt


def median(values):
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def pearson(x, y):
    x_mean, y_mean = sum(x) / len(x), sum(y) / len(y)
    numerator = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    denominator = sqrt(sum((a - x_mean) ** 2 for a in x) *
                       sum((b - y_mean) ** 2 for b in y))
    return numerator / denominator


def main():
    values = [2, 3, 4, 5, 6, 20]
    q1, q3 = median(values[:3]), median(values[3:])
    iqr = q3 - q1
    print("median, IQR, upper fence:", median(values), iqr, q3 + 1.5 * iqr)

    mean = sum(values) / len(values)
    sample_sd = sqrt(sum((value - mean) ** 2 for value in values) / (len(values) - 1))
    print("sample standard deviation:", round(sample_sd, 3))
    print("z-score of 20:", round((20 - mean) / sample_sd, 3))

    x, y = [1, 2, 3, 4, 5], [2, 4, 5, 8, 10]
    x_mean, y_mean = sum(x) / len(x), sum(y) / len(y)
    slope = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    slope /= sum((a - x_mean) ** 2 for a in x)
    intercept = y_mean - slope * x_mean
    print("Pearson r:", round(pearson(x, y), 3))
    print("least-squares line: y =", round(intercept, 3), "+", round(slope, 3), "x")


if __name__ == "__main__":
    main()
