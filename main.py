import sys


memory_size: int = 256
debug: bool = False


def main() -> None:
    file = sys.argv[1]
    code = open(file).read()
    interpret(code)


def interpret(code: str) -> None:
    global memory_size
    memory = [0] * memory_size
    return_stack = []
    input_buffer = ""
    output = ""
    char = ""
    pointer = 0
    i = 0

    while i < len(code):
        char = code[i]
        start = i

        if char in "+-*/%=.,>&#":
            operator = char
            i += 1
            temp = ""

            while i < len(code):
                char = code[i]

                if char in ":;":
                    break

                temp += char
                i += 1

            if char == ":":
                i += 1
                temp2 = ""

                while i < len(code):
                    char = code[i]

                    if char == ";":
                        break

                    temp2 += char
                    i += 1

                if operator == "+":
                    memory[int(temp)] += int(temp2)
                elif operator == "-":
                    memory[int(temp)] -= int(temp2)
                elif operator == "*":
                    memory[int(temp)] *= int(temp2)
                elif operator == "/":
                    memory[int(temp)] /= int(temp2)
                elif operator == "%":
                    memory[int(temp)] %= int(temp2)
                elif operator == "=":
                    memory[int(temp)] = int(temp2)
                elif operator == ".":
                    temp_pointer = int(temp)

                    for j in range(int(temp2)):
                        print(chr(memory[int(temp_pointer)]), end="")
                        output += chr(memory[int(temp_pointer)])
                        temp_pointer += 1
                        temp_pointer %= memory_size
                elif operator == ",":
                    temp_pointer = int(temp)

                    for j in range(int(temp2)):
                        while len(input_buffer) == "":
                            input_buffer = input()

                        memory[int(temp_pointer)] = ord(input_buffer[0])
                        input_buffer = input_buffer[1:]
                        temp_pointer += 1
                        temp_pointer %= memory_size
                elif operator == ">":
                    pointer = int(temp) + int(temp2)
                elif operator == "&":
                    temp_pointer = int(temp)
                    temp_pointer %= memory_size

                    for j in range(int(temp2)):
                        memory[int(temp_pointer)] = memory[int(temp)]
                        temp_pointer += 1
                        temp_pointer %= memory_size
                elif operator == "#":
                    temp_pointer = int(temp)

                    for j in range(int(temp2)):
                        print(memory[int(temp_pointer)], end=" ")
                        output += str(memory[int(temp_pointer)])
                        temp_pointer += 1
                        temp_pointer %= memory_size

                memory[int(temp)] %= 256
            elif char == ";":
                if len(temp) > 0:
                    if operator == "+":
                        memory[pointer] += int(temp)
                    elif operator == "-":
                        memory[pointer] -= int(temp)
                    elif operator == "*":
                        memory[pointer] *= int(temp)
                    elif operator == "/":
                        memory[pointer] /= int(temp)
                    elif operator == "%":
                        memory[pointer] %= int(temp)
                    elif operator == "=":
                        memory[pointer] = int(temp)
                    elif operator == ".":
                        temp_pointer = pointer

                        for j in range(int(temp)):
                            print(chr(memory[temp_pointer]), end="")
                            output += chr(memory[temp_pointer])
                            temp_pointer += 1
                            temp_pointer %= memory_size
                    elif operator == ",":
                        temp_pointer = pointer

                        for j in range(int(temp)):
                            while len(input_buffer) == "":
                                input_buffer = input()

                            memory[temp_pointer] = ord(input_buffer[0])
                            input_buffer = input_buffer[1:]
                            temp_pointer += 1
                            temp_pointer %= memory_size
                    elif operator == ">":
                        pointer += int(temp)
                        pointer %= memory_size
                    elif operator == "&":
                        temp_pointer = pointer + int(temp)
                        temp_pointer %= memory_size
                        memory[temp_pointer] = memory[pointer]
                    elif operator == "#":
                        temp_pointer = pointer

                        for j in range(int(temp)):
                            print(memory[temp_pointer], end=" ")
                            output += str(memory[temp_pointer])
                            temp_pointer += 1
                            temp_pointer %= memory_size
                else:
                    if operator == "+":
                        memory[pointer] += 1
                    elif operator == "-":
                        memory[pointer] -= 1
                    elif operator == "*":
                        memory[pointer] *= 2
                    elif operator == "/":
                        memory[pointer] /= 2
                    elif operator == "%":
                        memory[pointer] %= 2
                    elif operator == "=":
                        memory[pointer] = 0
                    elif operator == ".":
                        print(chr(memory[pointer]), end="")
                        output += chr(memory[pointer])
                    elif operator == ",":
                        while len(input_buffer) == "":
                            input_buffer = input()

                        memory[pointer] = ord(input_buffer[0])
                        input_buffer = input_buffer[1:]
                    elif operator == ">":
                        pointer += 1
                        pointer %= memory_size
                    elif operator == "&":
                        temp_pointer = pointer + 1
                        temp_pointer %= memory_size
                        memory[temp_pointer] = memory[pointer]
                    elif operator == "#":
                        print(memory[pointer], end="")
                        output += str(memory[pointer])

                memory[pointer] %= 256
        elif char in "!<":
            operator = char
            i += 1

            while i < len(code):
                char = code[i]

                if char == ";":
                    break

                i += 1

            if operator == "<":
                i = return_stack.pop()
        elif char == "?":
            i += 1
            temp = ""

            while i < len(code):
                char = code[i]

                if char in ":;":
                    break

                temp += char
                i += 1

            if char == ":":
                operator = temp[0]
                temp = temp[1:]
                i += 1
                temp2 = ""

                while i < len(code):
                    char = code[i]

                    if char in ":;":
                        break

                    temp2 += char
                    i += 1

                if char == ":":
                    i += 1
                    temp3 = ""

                    while i < len(code):
                        char = code[i]

                        if char == ";":
                            break

                        temp3 += char
                        i += 1

                    return_stack.append(i)

                    if (operator == ">" and memory[pointer] > int(temp)) or \
                       (operator == "<" and memory[pointer] < int(temp)) or \
                       (operator == "=" and memory[pointer] == int(temp)):
                        i = code.rfind(f"!{temp2};") + len(f"!{temp2};") - 1
                    else:
                        i = code.rfind(f"!{temp3};") + len(f"!{temp3};") - 1
                elif char == ";":
                    return_stack.append(i)

                    if (operator == ">" and memory[pointer] > int(temp)) or \
                       (operator == "<" and memory[pointer] < int(temp)) or \
                       (operator == "=" and memory[pointer] == int(temp)):
                        i = code.rfind(f"!{temp2};") + len(f"!{temp2};") - 1
            elif char == ";":
                return_stack.append(i)
                i = code.rfind(f"!{temp};") + len(f"!{temp};") - 1
        elif char == "~":
            i += 1
            temp = ""

            while i < len(code):
                char = code[i]

                if char == ";":
                    break
                elif char == "\\":
                    i += 1
                    char = code[i]

                    if char == "n":
                        char = "\n"
                    elif char == "t":
                        char = "\t"

                temp += char
                i += 1

            temp_pointer = pointer

            for j in range(len(temp)):
                memory[temp_pointer] = ord(temp[j])
                temp_pointer += 1
                temp_pointer %= memory_size
        else:
            i += 1
            continue

        i += 1

        if debug:
            print("")
            ln, col = code.count("\n", 0, start), start - code.rfind("\n", 0, start)
            print(output)
            print(f"{ln}:{col}")
            print(code[start:i])
            print([f"[{x}]" if i == pointer else x for i, x in enumerate(memory)])
            print(return_stack)
            input("")


if __name__ == "__main__":
    main()