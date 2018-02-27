# my_file = open("grade_book.txt", "r") # my_file is a list
# for line in my_file:
#     print(line)

def weighted_grade(score_list, weights_tuple=(0.3,0.3,0.4)):
    """Expects 3 elements in score_list.  Multiplies each grade by its weight.
    Returns the sum."""
    grade_float = 0
    for index, score in enumerate(score_list):
        grade_float += score*weights_tuple[index]
    # grade_float = \
    #     (score_list[0]*weights_tuple[0]) +\
    #     (score_list[1]*weights_tuple[1]) +\
    #     (score_list[2]*weights_tuple[2])
    return grade_float


def parse_line(line_str):
    """Expects a line of the form last, first, exam1, exam2, final
    Returns a tuple containing first+last and list of scores"""
    field_list = line_str.strip().split(',')
    name_str = field_list[1] + ' ' + field_list[0]
    score_list = []
    for element in field_list[2:]:
        score_list.append(int(element))
    return name_str, score_list


def main(): # main is "indent level 0"
    """Get a line_str from the file, print the final grade nicely"""
    file_name = input('Open what file:')
    grade_file = open(file_name,'r')
    print('{:>13s} {:>16s}'.format('Name', 'Grade'))
    print('-'*30)
    for line_str in grade_file:
        name_str, score_list = parse_line(line_str)
        grade_float = weighted_grade(score_list, (.5, .4, .1))
        print('{:>15s} {:14.2f}'.format(name_str, grade_float))

if __name__ ==  "__main__":
    main()
