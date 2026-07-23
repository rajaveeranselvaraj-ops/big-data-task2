import subprocess

with open("input.txt", "r") as infile:
    mapper = subprocess.Popen(
        ["python", "mapper.py"],
        stdin=infile,
        stdout=subprocess.PIPE,
        text=True
    )
    sorted_output = sorted(mapper.stdout.readlines())

reducer = subprocess.Popen(
    ["python", "reducer.py"],
    stdin=subprocess.PIPE,
    text=True
)

reducer.communicate(input="".join(sorted_output))
