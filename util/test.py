import sys
import os


def is_empty(file):
    if not os.path.exists(file):
        return True
    return os.stat(file).st_size == 0


def run_test(file, fun):
    if is_empty(f"{file}.out"):
        return

    with open(f"{file}.in") as input:
        result = fun(input.read())
    
    with open(f"{file}.out") as output:
        expected = output.read()

    assert str(result) == str(expected), f"Expected: '{expected}', got: '{result}'"

    print(f"{file} passed", file=sys.stderr)


def test_task(task_number, state=globals()):
    runner = state[f"task{task_number}"]
    preprocess = state.get("preprocess", lambda stdin: stdin)

    # test example
    run_test(f"example{task_number}", lambda stdin: runner(preprocess(stdin)))

    # run regression tests
    run_test(f"task{task_number}", lambda stdin: runner(preprocess(stdin)))
    

def run_tests(state):
    if "task1" in state:
        test_task(1, state=state)
    if "task2" in state:
        test_task(2, state=state)
