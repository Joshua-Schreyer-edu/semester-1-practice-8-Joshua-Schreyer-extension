
import subprocess

def test(inputs):

    arguments = []
    arguments.append("python3")
    arguments.append("change_maker.py")
    for i in inputs:
        arguments.append(i)

    subprocess.run(arguments)
    print("--- END OF TEST ---")

test(["23.12", "25.00"])