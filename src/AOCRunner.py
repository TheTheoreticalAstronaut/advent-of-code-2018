from Types import *
from AOCChallenge import AOCChallenge
from Day1 import Day1
from Day2 import Day2
from Day3 import Day3
from Day8 import Day8
from time import time


def run_challenge_once(challenge: Challenge) -> None:
    start_time = time()
    challenge_runner = _create_challenge_instance(challenge)
    print("Part one = {0}".format(challenge_runner.run_part_one()))
    print("Part two = {0}".format(challenge_runner.run_part_two()))
    end_time = time()
    print("Execution took {0:.2f}ms".format(1000*(end_time - start_time)))


def run_challenge_n_times(challenge: Challenge, n: int) -> None:
    total_time_in_ms = 0
    for _ in range(n):
        start_time = time()
        challenge_runner = _create_challenge_instance(challenge)
        challenge_runner.run_part_one()
        challenge_runner.run_part_two()
        end_time = time()
        total_time_in_ms += 1000*(end_time - start_time)

    average_execution_time = total_time_in_ms / n
    print("Average execution time was {0:.2f}ms (n = {1})".format(average_execution_time, n))


def _create_challenge_instance(challenge: Challenge) -> AOCChallenge:
    if challenge == Challenge.DAY_1:
        return Day1()
    elif challenge == Challenge.DAY_2:
        return Day2()
    elif challenge == Challenge.DAY_3:
        return Day3()
    elif challenge == Challenge.DAY_8:
        return Day8()
    else:
        return AOCChallenge("", Input.UNDEFINED)
