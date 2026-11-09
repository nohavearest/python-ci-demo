import runpy


def test_main_output(capsys):
    runpy.run_path("main.py", run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out == "hello ci\n"
