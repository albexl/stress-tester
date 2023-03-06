TEST_CASES=100  # number of test cases
RUN_GENERATOR="python3 ./generators/random.py"  # how to run the generator in terminal
RUN_SOLUTION="g++ ./solutions/solution.cpp -o ./solutions/solution && ./solutions/solution"  # how to run the solution in terminal
RUN_NAIVE="python3 ./solutions/naive.py"  # how to run the naive solution in terminal
STOP_FIRST_WA=false  # true: stops when it reaches the first WA
SAVE_ALL_TEST_CASES=true  # true: saves all test cases
TEST_CASES_DIRECTORY="./test_cases"  # directory to save the test cases

RESET_COLOR="\x1b[0m"  # reset terminal foreground color
OK_COLOR="\x1b[32m"  # green
WA_COLOR="\x1b[31m"  # red

echo "Starting stress testing with $TEST_CASES test case(s)..."
for i in `seq -f "%0${#TEST_CASES}g" 1 $TEST_CASES`  # from 1 to TEST_CASES, padding with 0s
do
    if $SAVE_ALL_TEST_CASES ; then  # if save the test cases then save it
        mkdir -p "$TEST_CASES_DIRECTORY"
        INPUT="$TEST_CASES_DIRECTORY/$i.in"
    else  # otherwise use a temp file
        INPUT=".temp_input"
    fi

    eval "$RUN_GENERATOR" > "$INPUT"  # generate a test case
    DIFF=$(diff -w <(eval "$RUN_SOLUTION" < "$INPUT") <(eval "$RUN_NAIVE" < "$INPUT"))  # eval the test case in both solutions and get their output differences
    if [ "$DIFF" == "" ] ; then  # their outputs are the same
        echo -e " • Test case $i: ${OK_COLOR}OK!${RESET_COLOR}"
    else  # their outputs differ
        echo -e " • Test case $i: ${WA_COLOR}Wrong Answer!${RESET_COLOR}"
        if $STOP_FIRST_WA ; then  # breaks the program, but the failed test case is stored in the temporal file
            break
        fi
    fi

if ! $SAVE_ALL_TEST_CASES ; then  # remove the temporal file
    rm "$INPUT"
fi
done