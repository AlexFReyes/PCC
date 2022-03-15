# Python variables are read from top to bottom so if a global variable is changed at the end of a script then its final value is the most recent one

message = 'Hello World!'
print(message)
message = 'Hellow Python Crash Course World!'
print(message)


