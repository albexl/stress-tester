@echo off
for /l %%x in (1, 1, 100) do (
    python generator.py > input.in
    python solution.py < input.in > solution.out 
    brute < input.in > brute.out
    fc solution.out brute.out > diagnostics || exit /b
    echo Test case: %%x
)
echo All tests passed