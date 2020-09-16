# simple search of a word in a list

def main():
    def load_file(file_name):
        input_file = open(file_name,"r")
        check_var = input_file.readline()
        try:
            new_var = int(check_var)
        except ValueError:
            try:
                new_var = float(check_var)
        return check_var
        input_file.close()


if __name__ == "__main__":
    main()