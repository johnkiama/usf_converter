import sys

with open(sys.argv[1]) as infile, open(sys.argv[2], "w+") as outfile:
  reader = infile.readlines()
  for line in reader:
    old_header = " TIME,      WIDTH,     VOLTAGE,    ERROR_BAR"
    new_header = "INDEX,  TIME,      WIDTH,     VOLTAGE,    ERROR_BAR,   MASK"
    if line.find(old_header) >=0:
      line = line.replace(old_header, new_header)
    if line.find("/SWEEPS: 1") >=0:
#      print("found")
      line = line + "/SWEEP_NUMBER: 1\n"
    outfile.write(line)
    
with open(sys.argv[2]) as usf_file, open("chtem16ttedit3.usf", "w+") as outfile2:
  read = usf_file.readlines()
  for lines in read:
    if lines.startswith(" "):
      l = lines.rstrip("\n").split(",")
      if len(lines.split()) == 0:
        continue
#      lines = "1, " + lines + "  ,2"
      lines = "  1,  " +  l[0] + "," +  l[1]+ "," +  l[2]+ "," +  l[3]+ "," + "   1\n"
    print(lines)
    outfile2.write(lines)
