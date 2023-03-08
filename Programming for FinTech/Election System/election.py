from sys import argv
import sys

def parse_state_information(filename):
    """
    Opens the state information file named in filename, loads all of the 
    values, placing them in a single data structure. Returns that data 
    structure.  You may created nested data structures.
    """
  
    '''
    with open(filename) as f:
        #stateCount =  51
        for line in f:
        count = 0   
           for s in range(3):
               char = f.read(1)
              
               l = char
               while char != ":" and char!='\n':
                   char = f.read(1)
                   if char!=':' and char!='\n':
                       l += char
               l.strip('\n')
               st.append(l)
                 
           stateData.append(st)
           st = []
  
    '''  
    #try to use split, readlines()
    stateData = []
    st = []
    with open(filename) as f:
        #stateData = []
        #st = []
        for line in f.readlines():
            sl = line.split(":")
            stateData.append([sl[0],sl[1],sl[2].replace('\n',"")])
        
    f.close()
    stateData.sort()
    return stateData


def print_state_information(state_info):
    """
    For the state_info data structure (produced as a result),  
    print all statues in alphabetical order using the string:
    "{}: Population - {:,d}, Electoral Votes: {:d}"
    """
    state = []
    for s in range(len(state_info)):
            state = state_info[s]
            print("{}: Population - {:,d}, Electoral Votes: {:d}".format(state[0], int(state[1]), int(state[2])))
      


def parse_vote_information(filename):
    """
    Opens the vote information file and returns the information 
    in a data structure
    """
    
    voteData = []
    vd = []
    with open(filename) as f:
        #voteData = []
        #vd = []
        for line in f.readlines():
            sl = line.split(":")
            voteData.append([sl[0],sl[1].replace('\n',"")])
    '''
    with open(filename) as f:
        count = 0
        while(True):   
           for s in range(2):
               char = f.read(1)
              
               l = char
               while char != ":" and char!='\n':
                   char = f.read(1)
                   if char!=':' and char!='\n':
                       l += char
               l.strip('\n')
               vd.append(l)
               
           voteData.append(vd)
           vd = []
           count += 1
           if(count==stateCount):
               break 
    '''
    f.close()
    voteData.sort()    
    return voteData
    

def count_electoral_votes(state_info,vote_info):
    """
    Counts and returns the number of electoral votes received by 
    Candidate A in the election.
    """
    candidate_a_electoral_votes = 0
    for v in range(len(vote_info)):
        if(float(vote_info[v][1])/float(state_info[v][1])>=0.50):            
            candidate_a_electoral_votes += int(state_info[v][2])
    
    return candidate_a_electoral_votes


def determine_winner(state_info, candidate_a_electoral_votes):
    """
    Determines whether Candidate A or Candidate B won based upon who
    won the majority of the electoral votes. If there is a tie, return None.
    Returns "A", "B", or None    the last one is the value None
    """
    ttlElecVotes = 0
    for s in range(len(state_info)):
        ttlElecVotes += int(state_info[s][2])
    if(candidate_a_electoral_votes/ttlElecVotes>0.50):
        return 'A'
    elif(candidate_a_electoral_votes/ttlElecVotes<0.50):
        return 'B'
    else:
        return None
        


def print_winner(winner_name, number_of_votes):
    """
    Prints the winner.  If Candidate A or B wins, print
    "Candidate {} wins the election with {:d} votes" using the winner_name
    and number of Electoral Collage.

    If neither won the vote, print "It's a tie in the Electoral Collage."
    """
    if(winner_name=='A' or winner_name=='B'):
        print("Candidate {} wins the election with {:d} votes".format(winner_name, number_of_votes))
    else:
        print('It\'s a tie in the Electoral Collage.')


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
    margin = 0.005
    recount_list = []
    for v in range(len(state_info)):
        if(float(vote_info[v][1])/float(state_info[v][1])<=(0.50+margin) and float(vote_info[v][1])/float(state_info[v][1])>=(0.50-margin)):
              percent = (float(vote_info[v][1])/float(state_info[v][1]))*100
              #print('{} requires a recount (Candidate A has {:.2f}% of the vote)'.format(vote_info[v][0], percent))
              
              recount_list.append('{} requires a recount (Candidate A has {:.2f}% of the vote)'.format(vote_info[v][0], percent))
    return recount_list


def save_recounts(recount_list):
    """
    saves each entry of the list to a file named "recounts.txt".  The
    entries must be printed in alphabetical order.
    """
    with open('recounts.txt', 'w') as f: 
        for line in recount_list: 
            #f.write('%s: %s\n' % (line))
            f.write('%s\n' % (line))
    
    


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
    largest_win = 0.499999999999
    state = ''
    for s in range(len(state_info)):
        if(float(vote_info[s][1]) / float(state_info[s][1]) > largest_win):
            largest_win = float(vote_info[s][1]) / float(state_info[s][1])
            state = state_info[s][0]
            return_string = 'Candidate A won {} with {:.2f}% of the vote'.format(state, largest_win*100)
                                                                                 
    #print(return_string)
    if largest_win==0.499999999999:
        return None
    else:
        return return_string 



def process(argv):      
    """
    Implements the "Several steps exist for this assignment" section
    """
    
    state_info = parse_state_information(argv[1])
    print_state_information(state_info)
    vote_info = parse_vote_information(argv[2])

    candidate_a_electoral_votes = count_electoral_votes(state_info, vote_info)
    winner_name = determine_winner(state_info, candidate_a_electoral_votes)
    
    ttlElecVotes = 0
    for s in range(len(state_info)):
        ttlElecVotes += int(state_info[s][2])
    
    if(winner_name=='A'):        
        number_of_votes = candidate_a_electoral_votes
    else:
        number_of_votes = ttlElecVotes - candidate_a_electoral_votes
    
    print_winner(winner_name, number_of_votes)
    recount_list = determine_recounts(state_info, vote_info)
    save_recounts(recount_list)
    return_string = determine_largest_win(state_info, vote_info)
    print(return_string)
    

if __name__ == "__main__":
    if len(argv) < 3:  # check for correct number of args
        print("Usage: python3 key_value.py file1_name file2_name ...")
        sys.exit(1)
   
    process(argv)


        
        
