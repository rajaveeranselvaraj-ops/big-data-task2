import subprocess

# Run mapper
with open("input.txt", "r") as infile:
    mapper = subprocess.Popen(
        ["python", "mapper.py"],
        stdin=infile,
        stdout=subprocess.PIPE,
        text=True
    )

    # Sort mapper output
    sorted_output = sorted(mapper.stdout.readlines())

# Run reducerpython
reducer = subprocess.Popen(
    ["python", "reducer.py"],
    stdin=subprocess.PIPE,
    text=True
)

reducer.communicate(input="".join(sorted_output))