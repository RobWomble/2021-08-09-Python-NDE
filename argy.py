import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Playing around with argparse")
    parser.add_argument("me", help="Put your name in here")
    parser.add_argument("greet", choices=['hi', 'bye'], help="Say 'hi' to greet, say 'bye' to leave")
    parser.add_argument("-i", "--insult", action="store_true", help="Would you like to insult them?")
    parser.add_argument("-c", "--compliment", action="store_true", default="yes", help="Would you like to compliment them?")
    return parser.parse_args()


def say_hi(name, insult, compliment):
    if insult:
        print(f"Hello there {name}, you stink")
    elif compliment == True:
        print(f"Hello there {name}, I like your shirt!")
    elif compliment == "yes":        
        print(f"Hello there {name}, I like your shoes!")
    else:
        print(f"Hello there {name}")


def main():
    args = get_args()
    print(f"The args from get_args are:\n\n{args}\n")
    print(args.greet)
    if args.greet == "hi":
        say_hi(args.me, args.insult, args.compliment)
    # else:
        # say_bye 


if __name__ == "__main__":
    main()
