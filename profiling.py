"""
This is just an example script to show profiling with runsnakerun and debugging
with PyCharm.
"""
import time


def main():
    t = .3
    time.sleep(t)
    deeper(t)


def deeper(x):
    for i in range(10):
        time.sleep(x/20)
        deepest(x)


def deepest(x):
    time.sleep(x/20)
    y = x ** 2
    y


if __name__ == '__main__':
    main()

