# Exceptions
An exception is an event that interrupts the flow of a program.

There are different kinds of exceptions and, just like Java, there are three ways to deal with them:
1. ```try```: the block of code to execute
2. ```except```: the custom behavior to deal with an exception
3. ```finally```: the code to execute before exiting

An exception can occur because of an unexpected operation, such as ```1/0``` (*ZeroDivisionError*).

A *TypeError* can occur when trying to perform operations not compatible with a certain data type ```1 + "1"```.

Exception handling consists in:
```
try:
    # do something that is "dangerous" (such as user input)
except <exception_name>:
    # handle exception
finally:
    # do some clean up
```

You could, but not should, catch all exceptions as one:

```except Exception:```

Usually you use it **only after** having dealt with the most predictable exceptions

The ```finally``` section gets executed regardless of the try-except statement, 
and can be used to do some cleanup operations (i.e. closing a file)