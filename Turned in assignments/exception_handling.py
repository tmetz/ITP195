def main():
    line_count = 1
    file_name = input("Please input a file name: ")
    line_number = input("Please enter a line number: ")
    output_list = []
    try:
        line_number_int = int(line_number)
        input_file = open(file_name, "r")
        for line in input_file:
            if line_count == line_number_int:
                print("Line {} of the file {} is {}".format(line_number_int, file_name, line))
                line = line.strip()[::-1] + "\n" # Reverse, but first strip carriage return...then put another one at the end of line
            line_count += 1
            output_list.append(line)
        input_file.close()
        if line_number_int > line_count - 1:
            print("Sorry, there is no line {} in {}".format(line_number_int, file_name))
        else:
            output_file = open("output_lab_8.txt", "w")
            for line in output_list:
                output_file.write(line)
            output_file.close()

    except FileNotFoundError:
        print("Sorry, {} cannot be found.".format(file_name))

    except ValueError:
        print("Sorry, {} is not a valid line number.".format(line_number))



if __name__ == "__main__":
    main()