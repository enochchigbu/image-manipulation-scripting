import subprocess

# Run matlab code 1
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'

with open('matlabprogram.m', 'r') as file:
    matlabcode = file.read()

matlab_process = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
                                  stdin=subprocess.PIPE, text=True)

matlab_process.communicate(input=matlabcode)

# Read from input text file
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [int(value) for value in line.split()]
    input_array = [str(value) for value in input_array]

# Run C Program
subprocess.run(["gcc", "cprogram.c", "-o", "cprog"])

process = subprocess.run(["./cprog"] + input_array,
                         capture_output=True, text=True)

output_variable = process.stdout.strip()

# Save output to text file
with open('c_output.txt', 'w') as f:
    f.write(output_variable)

# Run Haskell Code
subprocess.run(["ghc", "hsprogram.hs"])
process = subprocess.run(["./hsprogram"] + [str(x)
                         for x in input_array], text=True, capture_output=True)

output_variable = process.stdout.strip()

# Save output to text file
with open('haskell_output.txt', 'w') as f:
    f.write(output_variable)

# Run Prolog Code
prolog_input = "[" + ",".join(map(str, input_array)) + "]."

result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'plgprogram.pl'], input=prolog_input,
                        capture_output=True, text=True)

result = result.stdout.strip()

# Save output to text file
with open('prolog_output.txt', 'w') as f:
    f.write(result)

# Run Matlab 2 Code
with open('matlabprogram2.m', 'r') as file:
    matlabcode2 = file.read()

matlab_process = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
                                  stdin=subprocess.PIPE, text=True)

matlab_process.communicate(input=matlabcode2)
