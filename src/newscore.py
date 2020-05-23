import sys


file = sys.argv[1]
output = open(sys.argv[2],"w")

with open(file,"r") as f:
    output.write(str(1-float(f.read())))

