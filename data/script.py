def add_str_to_lines(f_name, str_to_add):
    with open(f_name, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            lines[index] = str_to_add + line.strip() + str_to_add +","

    with open("result.txt", "w") as f:
        for line in lines:
            f.write(line)

#if __name__ == "__main__":
str_to_add = '"'
f_name = "names.txt"
add_str_to_lines(f_name=f_name, str_to_add=str_to_add)