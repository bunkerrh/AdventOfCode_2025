def main():
    with open('inputs/puzzleOneInput.txt') as input_file:
        rotations = input_file.read().splitlines()

    with open('outputs/puzzleOneOutput.txt', 'w') as output:

        def log(msg):
            output.write(str(msg) + "\n")

        currentPos = 50
        passCount = 0

        for rotation in rotations:
            turns = int(rotation[1:])

            log("Turns: " + str(rotation))
            log("Current Position: " + str(currentPos))
            log("Current Passcount " + str(passCount))
            log("Adding to passcount: " + str(abs(turns // 100)))

            passCount += abs(turns // 100)

            if rotation.startswith("L"):
                log("Subtracting from current: " + str(currentPos))
                currentPos -= turns
                currentPos %= 100
                if currentPos == 0:
                    log("Adding one to passcount: " + str(passCount))
                    passCount += 1
                log("New Position: " + str(currentPos))
                continue

            elif rotation.startswith("R"):
                log("Adding to current: " + str(currentPos))
                currentPos += turns
                currentPos %= 100
                if currentPos == 0:
                    log("Adding one to passcount: " + str(passCount))
                    passCount += 1
                log("New Position: " + str(currentPos))
                continue

        log("My password is " + str(passCount))
        output.write("\n")


if __name__ == "__main__":
    main()
