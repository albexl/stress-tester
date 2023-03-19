"""Module to stress test solutions that return exact output in Python."""


import argparse
import subprocess

from colorama import Fore


def check(
    test_cases: int,
    generator_path: str,
    solution_path: str,
    naive_path: str,
    tests_path: str,
) -> bool:
    """Checks the output of two solutions against a set of generated test cases.

    Args:
        test_cases (int): Number of test cases to try.
        generator_path (str): Path of the test case generator script.
        solution_path (str): Path of the solution to test.
        naive_path (str): Path of the naive solution.
        tests_path (str): Directory to store the test cases's input and output.

    Returns:
        bool: True if the output for all tests cases match, False otherwise.
    """
    print(f"Starting stress testing with {test_cases} test case(s)...")
    for i in range(1, test_cases + 1):
        # Generate random test case
        with open(f"{tests_path}/input-{i}.in", "w", encoding="utf-8") as test_case:
            subprocess.run(["python3", generator_path], stdout=test_case)

        # Open test case input file
        with open(f"{tests_path}/input-{i}.in", "r", encoding="utf-8") as test_case:
            # Run solution and store the output in a file
            with open(f"{tests_path}/solution-{i}.out", "w", encoding="utf-8") as solution_file:
                test_case.seek(0)
                subprocess.run(["python3", solution_path], stdin=test_case, stdout=solution_file)

            # Run naive solution and store the output in a file
            with open(f"{tests_path}/naive-{i}.out", "w", encoding="utf-8") as naive_file:
                test_case.seek(0)
                subprocess.run(["python3", naive_path], stdin=test_case, stdout=naive_file)

            # Check for differences in both output files
            output = subprocess.run(
                ["diff", f"{tests_path}/solution-{i}.out", f"{tests_path}/naive-{i}.out"], stdout=subprocess.PIPE
            )

            # Return code different from 0 means that the outputs differ
            if output.returncode == 0:
                print(f" • Test case {i}: {Fore.GREEN}OK!{Fore.WHITE}")
            else:
                print(f" • Test case {i}: {Fore.RED}Wrong Answer!{Fore.WHITE}")
                return False
    return True


def parse_args():
    """Parse arguments passed through CLI.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(prog="Stress Tester", description="Stress tests solutions written in Python")
    parser.add_argument("--test-cases", type=int, required=True, help="Number of test cases to run")
    parser.add_argument("--generator-path", required=True, help="Path to the generator file")
    parser.add_argument("--solution-path", required=True, help="Path to the solution to stress test")
    parser.add_argument("--naive-path", required=True, help="Path to the naive solution")
    parser.add_argument("--tests-path", required=True, help="Directory to store test cases")
    return parser.parse_args()


def _main():
    args = parse_args()
    check(
        args.test_cases,
        args.generator_path,
        args.solution_path,
        args.naive_path,
        args.tests_path,
    )


if __name__ == "__main__":
    _main()
