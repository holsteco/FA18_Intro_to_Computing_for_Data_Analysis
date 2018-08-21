#corey b. holstege
#2018-08-21
#http://interactivepython.org/runestone/static/thinkcspy/SimplePythonData/Input.html

str_seconds = input("Please enter the number of seconds you wish to convert:")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hours=", hours, "Minutes=", minutes, "Seconds=", secs_finally_remaining)