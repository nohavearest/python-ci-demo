import runpyp


def test_main_output(capsys):
    runpyp.run_path("main.py", run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out == "hello ci\n"
