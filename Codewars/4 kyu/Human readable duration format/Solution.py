def format_duration(seconds):
    year = 31536000
    day = 86400
    hour = 3600
    minute = 60
    second = 1
    solution = []
    final = []

    def define(seconds):
        divider = None
        extension = None

        if seconds >= year:
            divider = year
            extension = "year"

        elif seconds >= day:
            divider = day
            extension = "day"

        elif seconds >= hour:
            divider = hour
            extension = "hour"

        elif seconds >= minute:
            divider = minute
            extension = "minute"

        elif seconds >= second:
            divider = second
            extension = "second"

        return divider, extension

    if seconds == 0:
        return "now"
    else:
        while seconds > 0:
            carrier = False
            old = seconds
            divider = define(seconds)[0]
            extension = define(seconds)[1]

            seconds = seconds % divider
            toadd = (old - seconds) / divider

            if toadd > 1:
                carrier = True
                extension = extension + "s"

            toadd = " ".join([str(int(toadd)), extension])
            solution.append(toadd)

        counter = 0

        if len(solution) == 1:
            return solution[0]
        else:
            for each in range(len(solution)):
                if counter == len(solution) - 2:
                    final.append(f"{solution[-2]} and {solution[-1]}")
                    break
                else:
                    final.append(solution[counter])
                    final.append(", ")
                counter += 1

            return "".join(final)
