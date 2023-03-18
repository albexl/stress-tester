# Number of test cases
TEST_CASES=100

# Commands to execute python scripts
RUN_GENERATOR="python3 ./generators/random_generator.py"
RUN_SOLUTION="python3 ./solutions/solution.py"
RUN_NAIVE="python3 ./solutions/naive.py"

# Test directory
TEST_CASES_DIRECTORY="./test_cases"

# Console Colors
RESET_COLOR="\x1b[0m"
OK_COLOR="\x1b[32m"
WA_COLOR="\x1b[31m"

echo "Starting stress testing with $TEST_CASES test case(s)..."

mkdir -p "$TEST_CASES_DIRECTORY" # Create directory to store test cases
for i in `seq -f "%0${#TEST_CASES}g" 1 $TEST_CASES`
do
    INPUT="$TEST_CASES_DIRECTORY/$i.in"

    eval "$RUN_GENERATOR" > "$INPUT"  # Generate a test case
    DIFF=$(diff -w <(eval "$RUN_SOLUTION" < "$INPUT") <(eval "$RUN_NAIVE" < "$INPUT"))  # Evaluate the test case in both solutions and get their output differences
    if [ "$DIFF" == "" ] ; then  # Same output
        echo -e " • Test case $i: ${OK_COLOR}OK!${RESET_COLOR}"
    else  # Different output
        echo -e " • Test case $i: ${WA_COLOR}Wrong Answer!${RESET_COLOR}"
        break
    fi
done