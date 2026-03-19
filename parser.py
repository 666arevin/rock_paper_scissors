import argparse

def parser_command_line():
    
    global argparse

    parser = argparse.ArgumentParser(prog="Rock Paper Scissors game", description="You can play rock paper scissors with this program.")
    
    parser.add_argument('command', choices=['start', 'exit'], help="Выберите одно из этих действи -> ['start', 'exit']")
    
    args = parser.parse_args()
    return args


print(parser_command_line())
