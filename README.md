# Stress-Tester

Code examples used for the [NAME](LINK) article in Hashnode.

## Usage

In case you want to try the solution you can follow these steps:

1. Replace the code in `./generators/random_generator.py` for the test case generator suitable for your use case.
2. Replace the code in `./solutions/solution.py` with the code that you want to test.
3. Replace the code in `./solutions/naive.py` with the naive solution for the problem you are trying to solve.
4. Run the checker scripts:

   1. Using `shell`: Execute the following command in the root of the project.

      ```shell
      ./check.sh
      ```

   2. Using `python`: Execute the following command in the root of the project.

      ```shell
      python3 check.py --test-cases 100 --generator-path ./generators/random_generator.py --solution-path ./solutions/correct.py --naive-path ./solutions/naive.py --tests-path ./test_cases
      ```

      The arguments in the `python` are customizable. For example, the `--test-cases` argument can be changed to try with more or less cases. The arguments that are paths can be changed as well. Be careful when doing this, the specified paths should exist.

## Next steps

List of future improvements:

1. Make it work not only for python solutions/generators.
