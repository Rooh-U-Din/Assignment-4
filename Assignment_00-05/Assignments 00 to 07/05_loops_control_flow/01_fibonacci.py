# 01_fibonacci

def main():
    max_term_value = 10000
    curr_term = 0
    next_term = 1

    while next_term < max_term_value:
        print(next_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
if __name__ == "__main__":
    main()