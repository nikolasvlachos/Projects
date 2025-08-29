class Leaderboard ():

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__ (self, file_name):
        # Opens the leaderboard text file
        self.leaderboard_file_name = file_name
        leaderboard_file = open (self.leaderboard_file_name, "a")
        leaderboard_file.close ()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def reorder_leaderboard (self, leaderboard_history):
        # Re-orders the leaderboard stats from highest score to lowest
        for index in range (len (leaderboard_history)):
            for position_of_line_moving in \
                    range (len (leaderboard_history) - 1):
                if (len (leaderboard_history) > 1):
                    # Checks if the stat next to the current index
                    # is a bigger number or not
                    if (int (leaderboard_history[position_of_line_moving][1]) <
                            int (leaderboard_history
                                 [position_of_line_moving + 1][1])):
                        array_to_move = leaderboard_history \
                        [position_of_line_moving]
                        leaderboard_history.pop \
                            (position_of_line_moving)
                        leaderboard_history.\
                            insert(position_of_line_moving + 1,
                            array_to_move)

                        if (position_of_line_moving != 0):
                            position_of_line_moving -= 1

        leaderboard_file = open (self.leaderboard_file_name, "w")
        # Write the new order into the leaderboard file
        for write_to_leaderboard in range (len (leaderboard_history)):
            leaderboard_file.write \
                (leaderboard_history[write_to_leaderboard][0] + " ~ " +
                 leaderboard_history[write_to_leaderboard][1] + "\n")
        leaderboard_file.close ()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_score (self, name, score):
        # Sets a new score into the leaderboard
        leaderboard_history = []
        leaderboard_file = open (self.leaderboard_file_name, "a")
        # Adds score and name into the leaderboard
        leaderboard_file.write(name + " ~ " + str (score + "\n"))
        leaderboard_file.close ()

        leaderboard_file = open (self.leaderboard_file_name, "r")
        line_read = leaderboard_file.readline ()
        line_read = line_read.strip ("\n")
        while (line_read != ""):
            dash_counter = -1
            dash_found = False
            while (not dash_found):
                if (line_read[dash_counter] != "~"):
                    dash_counter -= 1
                else:
                    dash_found = True
            current_line = [line_read[0:dash_counter - 1],
                            line_read[dash_counter +
                            2:len (line_read)]]
            # Re-calculate the order of the stats
            leaderboard_history.append (current_line)
            line_read = leaderboard_file.readline ()
            line_read = line_read.strip ("\n")
        leaderboard_file.close ()
        Leaderboard.reorder_leaderboard (self, leaderboard_history)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def get_stats (self):
        # This gets the leaderboard stats and returns a list
        leaderboard_list = []
        leaderboard_file = open (self.leaderboard_file_name, "r")
        line_read = leaderboard_file.readline ()
        line_read = line_read.strip ("\n")

        if (line_read != ""):
            while (line_read != ""):
                # If a line with a stat is found, add it into a list
                leaderboard_list.append (line_read)
                line_read = leaderboard_file.readline ()
                line_read = line_read.strip ("\n")


        leaderboard_file.close ()

        for i in range (0, len (leaderboard_list)):
            current_entry = leaderboard_list[i]
            index = current_entry.index ("~")
            first_name = current_entry[0:index]
            for j in range (0, len (first_name)):
                if (first_name[j] == " "):
                    first_name = first_name[:j] + first_name[j:-1]
                    break
            score = current_entry[index + 2:]
            new_entry = [first_name, "-", score]
            leaderboard_list[i] = new_entry

        if (len (leaderboard_list) > 10):
            leaderboard_list = leaderboard_list[0:10]

        return leaderboard_list
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
