f = open("password-manager.py", "r")
code = ""
lines = f.readlines()
for line in lines:
    code = code + line
f.close
final_code = "#!/usr/bin/python3" + str(code)
print(final_code)
open("password-manager", 'w').close()
f = open("password-manager", "a")
f.write("#!/usr/bin/python3\n")
f.write(str(code))
f.close()
