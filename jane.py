def parse_facts(query,facts):
    if query == 1:
        print("m = 3.28 ft, ft = 12 inches")
    elif query == 2:
        print("hr = 60 min, min = 60 sec")

def answer_query(query,facts):
    print("Select the conversion you want to do")
    print("0 : Distance && 2 : Time")
    query = int(input())
    print("Write your query in int string string format")
    print("like convert 1 m inch")
    first_input = int(input())
    second_input = string(input())
    thrid_input = string(input())
    if second_input == m and thrid_input == inch:
        answer = first_input * 3.28 * 12
    elif second_input == ft and third_input == inch:
        answer = first_input * 12


def main():
    print("Select the conversion you want to do")
    print("0 : Distance && 2 : Time")
    query = int(input())
    print("Write your query in int string string format")
    print("like convert 1 m inch")
    first_input = int(input())
    second_input = string(input())
    thrid_input = string(input())
 

    answer_query()
