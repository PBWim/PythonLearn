from project import module1, module2

def main():
    print("Welcome to my project!")
    result1 = module1.do_something()
    result2 = module2.do_something_else()
    print(f"Results: {result1}, {result2}")

# The __name__ variable in Python is a special built-in variable that determines the name 
# of the module or script that is being executed
if __name__ == "__main__":
    main()
