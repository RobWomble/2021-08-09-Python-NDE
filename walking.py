import os

print(os.walk("/home/student"))
print(type(os.walk("/home/student")))


for root, dirs, files in os.walk("/home/student/mycode/challenges"):
    print(files)

path_1 = "/home/student/"
path_2 = "myfile.txt"

print(path_1 + path_2)
print(os.path.join(path_1, path_2))


rel_1 = "template_dir"
rel_2 = "my_template.j2"

print(f"{rel_1}\\{rel_2}")
print(os.path.join(rel_1, rel_2))
