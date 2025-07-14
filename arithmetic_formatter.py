def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_line = ""
    bottom_line = ""
    dash_line = ""
    answer_line = ""
    for problem in problems:
        if top_line != "":
            top_line += " " * 4
            bottom_line += " " * 4
            dash_line += " " * 4
            answer_line += " " * 4

        if "/" in problem or "*" in problem:
            return "Error: Operator must be '+' or '-'."
        else:
            operator = "+"
            if "-" in problem:
                operator = "-"
            
            operand_1_str = problem.split(operator)[0].strip()
            operand_2_str = problem.split(operator)[1].strip()
            
            if not operand_1_str.isnumeric() or not operand_2_str.isnumeric():
                return "Error: Numbers must only contain digits."
            elif len(operand_1_str) > 4 or len(operand_2_str) > 4:
                return "Error: Numbers cannot be more than four digits."
            
            operand_1 = int(operand_1_str)
            operand_2 = int(operand_2_str)
            operand_length = max(len(operand_1_str), len(operand_2_str))

            top_line += str(operand_1).rjust(operand_length + 2)
            bottom_line += operator + str(operand_2).rjust(operand_length + 1)
            dash_line += "-" * (operand_length + 2)

            if operator == "+":
                answer_line += str(operand_1 + operand_2).rjust(operand_length + 2)
            else:
                answer_line += str(operand_1 - operand_2).rjust(operand_length + 2)
    
    result = top_line + "\n"
    result += bottom_line + "\n"
    result += dash_line
    if show_answers:
        result += "\n" + answer_line

    return result

print(f'{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False)}')
