def main():
    try:
        number = int(input("Enter a number: "))
        print(1/number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("You need to enter a number")
    except Exception:
        print("Something went wrong")
    finally:
        print("Finally...")

if __name__ == "__main__":
    main()