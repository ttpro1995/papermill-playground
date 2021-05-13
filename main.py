import papermill as pm
import os


def clean_run():
    param_dict = {"a": 1, "b": 2, "c": 3, "d": "woof"}
    pm.execute_notebook(
        "notebook/parameter_clean.ipynb",
        "notebook/parameter_clean_output.ipynb",
        param_dict)


def exception_run():
    """
    will throw exception
    :return:
    """
    param_dict = {"a": 1, "b": 2, "c": 3, "d": "woof"}
    pm.execute_notebook(
        "notebook/papermill_exception.ipynb",
        "notebook/papermill_exception_output.ipynb",
        param_dict)



if __name__ == "__main__":
    clean_run()
    try:
        exception_run()
    except Exception as e:
        print("exception is throw")
        print(e)
        print("this is exception run()")
