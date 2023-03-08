from sys import argv
import sys

def parse_state_information(filename):
    """
    Opens the state information file named in filename, loads all of the 
    values, placing them in a single data structure. Returns that data 
    structure.  You may created nested data structures.
    """
    result = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            items = line.split(':')
            state_info = { "population": int(items[1]), "electoralVotes": int(items[2])}
            result[items[0]] = state_info
    return result

def print_state_information(state_info):
    """
    For the state_info data structure (produced as a result),  
    print all statues in alphabetical order using the string:
    "{}: Population - {:,d}, Electoral Votes: {:d}"
    """
    for state in sorted(state_info):
        print("{}: Population - {:,d}, Electoral Votes: {:d}".format(state,state_info[state]["population"], state_info[state]["electoralVotes"]))


def parse_vote_information(filename):
    """
    Opens the vote information file and returns the information 
    in a data structure
    """
    result = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            items = line.split(':')
            result[items[0]] = int(items[1])
    return result


def count_electoral_votes(state_info,vote_info):
    """
    Counts and returns the number of electoral votes received by 
    Candidate A in the election.

    For our purposes, Candidate A receives ALL electoral votes for a
    state if Candidate A receives strictly more than 50% of the votes in
    that State.  [Yes, we know that in the US there are a few states
    with more complex rules, but we will ignore them.  We will also
    ignore the electoral complexities of what would happen if a
    candidate received exactly 50%, and in this case, just say that
    Candidate A does not receive those electoral votes.  We are also
    assuming everyone in every state votes--while this doesn't happen in
    a real election, it is what we are doing here].
    """
    candidate_a_votes = 0
    for state in state_info:
        pop = state_info[state]["population"]
        votes = vote_info[state]
        if votes > (pop // 2): candidate_a_votes += state_info[state]["electoralVotes"]

    return candidate_a_votes

def determine_winner(state_info, candidate_a_electoral_votes):
    """
    Determines whether Candidate A or Candidate B won based upon who
    won the majority of the electoral votes. If there is a tie, return None.
    Returns "A", "B", or None    the last one is the value None
    """
    total_votes = count_total_electoral_votes(state_info)
    required_votes = total_votes // 2
    if candidate_a_electoral_votes < required_votes:
        return "B"
    elif candidate_a_electoral_votes > required_votes:
        return "A"
    else:
        return None

def print_winner(winner_name, number_of_votes):
    """
    Prints the winner.  If Candidate A or B wins, print
    "Candidate {} wins the election with {:d} votes" using the winner_name
    and number of Electoral College votes.

    If neither won the vote, print "It's a tie in the Electoral College."
    """
    if winner_name is None:
        print("It's a tie in the Electoral College.")
        return
    else:
        print("Candidate {} wins the election with {:d} votes".format(winner_name,number_of_votes))

def determine_recounts(state_info, vote_info):
    """
    Produces a list of strings, where each string represents information
    about a state the requires a recount. Recounts are required when a 
    Candidate A is within +/ 0.5% of 50% of the votes.  So 49.50% or 50.50%
    require a recount, while 49.49% and 50.51% do not require a recount.
    
    Only include states that require a recount in the result. For each state
    that requires a recount, include a line of the form:
    "{} requires a recount (Candidate A has {:.2f}% of the vote)".
    """
    results = []
    for state in state_info:
        pop = state_info[state]["population"]
        votes = vote_info[state]
        if 0.495 <= votes/pop <= 0.505:
            results.append("{} requires a recount (Candidate A has {:.2f}% of the vote)".format(state, votes/pop*100))
    return results

def save_recounts(recount_list):
    """
    saves each entry of the list to a file named "recounts.txt".  The
    entries must be printed in alphabetical order.
    """
    with open("recounts.txt","w") as f:
        for item in sorted(recount_list):
            print(item, file=f)

def determine_largest_win(state_info, vote_info):
    """
    Determines in which state Candidate A won the largest percentage 
    of the vote.

    returns a string with the following format:
    "Candidate A won {} with {:.2f}% of the vote"

    where the first {} should be the name of the state, and the {.2f} 
    should be the percentage of the vote won.  For example, it might return
    "Candidate A won California with 73.24% of the vote"

    None is returned if candidate A did not win a state
    """
    largest_win_percent = 0.0
    largest_win_state   = ""

    for state in state_info:
        pop = state_info[state]["population"]
        votes = vote_info[state]
        if votes > (pop // 2): 
            if votes/pop > largest_win_percent:
                largest_win_percent = votes/pop
                largest_win_state = state
    
    if largest_win_percent > 0.0:
        return "Candidate A won {} with {:.2f}% of the vote".format(largest_win_state,largest_win_percent*100)
    else:
        return None

#### HELPER FUNCTIONS
def count_total_electoral_votes(state_info):
    return sum([ state_info[x]["electoralVotes"] for x in state_info ])

def determine_winner_votes(state_info,winner,candidate_a_votes):
    if (winner is None): return None
    if (winner == "A"): return candidate_a_votes
    return count_total_electoral_votes(state_info) - candidate_a_votes

#### END OF HELP FUNCTIONS


def process(state_info_filename, voter_info_filename):
    """
    Implements the "Several steps exist for this assignment" section
    """
    state_info = parse_state_information(state_info_filename)
    print_state_information(state_info)
    vote_info = parse_vote_information(voter_info_filename)
    candidate_a_votes = count_electoral_votes(state_info,vote_info)
    winner = determine_winner(state_info,candidate_a_votes)
    winner_votes = determine_winner_votes(state_info,winner,candidate_a_votes)
    print_winner(winner,winner_votes)
    recounts = determine_recounts(state_info,vote_info)
    save_recounts(recounts)
    largest_win = determine_largest_win(state_info,vote_info)
    print(largest_win)


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python3 election.py state_info vote_info")
        sys.exit(1)
    process(argv[1],argv[2])
