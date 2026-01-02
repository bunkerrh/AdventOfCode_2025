def main():
    with open('inputs/puzzleOneInput.txt') as input_file:
        rotations = list(map(int, input_file.read().replace('R', '').replace('L', '-').split()))

    with open('outputs/puzzleOneOutput.txt', 'w') as output:

        def log(msg):
            output.write(str(msg) + "\n")

        currentPos = 50
        passCount = 0

        for rotation in rotations:
            startingPosition = currentPos
            loopPassCount = 0
            log("Current Position: " + str(currentPos))
            log("Rotation: " + str(rotation))
            log("Current passcount: " + str(passCount))
            # we need to determine the new position

            
            currentPos += rotation
            log("Raw new position: " + str(currentPos))

            # we are now handling where clicks are less than 100 but we still cross that threshold
            if(abs(rotation) < 100 and (startingPosition != 0)): 
                # lets instead do it where we are less than 0 and more than 0 for
                if(rotation >= 0): 
                    if(startingPosition + rotation) >= 100:
                        loopPassCount += 1
                        log("DEBUGGING 1")
                        log("Adding to passcount: " + str(1))
                        log("Starting position + rotation: " + str(startingPosition) + "+" + str(rotation))
                if(rotation <0):
                    if(startingPosition + rotation) <= 0:
                        loopPassCount += 1
                        log("DEBUGGING 2")
                        log("Adding to passcount: " + str(1))
                        log("Starting position + rotation: " + str(startingPosition) + "+" + str(rotation))

            # We have added the number of times we have cross zero with 100
            else: 
                loopPassCount += abs(currentPos) // 100
                log("Adding to passcount: " + str(abs(rotation) // 100))
                log("Loop passcount: " + str(loopPassCount))
                log("DEBUGGING 3")

                #now we need to handle spillover
                if(rotation < 0):
                    spillOver = abs(rotation) % 100
                    if(startingPosition - spillOver < 0):
                        loopPassCount += 1
                        log("DEBUGGING 4")
                        log("Adding to passcount: " + str(1))
                if(rotation > 0):
                    spillOver = rotation % 100
                    if(spillOver + startingPosition > 100):
                        loopPassCount += 1
                        log("DEBUGGING 5")

            remaining = currentPos % 100
            log("Remaining: " + str(remaining))

            #now we are going to determine the new position
            currentPos %= 100

            passCount += loopPassCount
            log("Loop Passcount: " + str(loopPassCount))
            log("Total passcount: " + str(passCount))

            #Now we need to check if we have crossed zero using the left over numbers
            #To do that we are going to take the current position and then we are 

            log("Final new position: " + str(currentPos))
            log("")
        log("My password is " + str(passCount))
        print("My password is " + str(passCount))
        output.write("\n")


if __name__ == "__main__":
    main()


#6705