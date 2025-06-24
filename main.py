from stats import print_pretty_book_stats
import sys

def main():
    
    num_args = len(sys.argv)

    if num_args == 1 or num_args > 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

    print_pretty_book_stats(sys.argv[1])
    
   # filepath = "books/frankenstein.txt"
   # print_pretty_book_stats(filepath)


main()