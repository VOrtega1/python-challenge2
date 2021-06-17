import os
import sys
import csv

# Path to collect data from the Resources folder

election_data = os.path.join('Resources','election_data.csv')

with open(election_data, "r") as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
        

# create column list               
voter_id = data['Voter ID']  
county = data['County']          
candidate = data['Candidate']

#Total vote count
total_votes = len(voter_id)

#define names
names = list(dict.fromkeys(candidate))
print(candidate)

#count each vote per candidate
Khan_Votes = candidate.count('Khan')
CorreyVotes = candidate.count('Correy')
LiVotes = candidate.count('Li')
OTooleyVotes = candidate.count("O'Tooley")

#Verify percentage of votes
khan_perc = '{:.2%}'.format(Khan_Votes / total_votes)
correy_perc = '{:.2%}'.format(CorreyVotes / total_votes)
li_perc = '{:.2%}'.format(LiVotes / total_votes)
otooley_perc = '{:.2%}'.format(OTooleyVotes / total_votes)

#who won?
vote_count = [Khan_Votes, CorreyVotes, LiVotes, OTooleyVotes]
wins = max(vote_count)

if candidate.count('Khan') > candidate.count('Correy') & candidate.count('Li') & candidate.count("O'Tooley"):
    winner = 'Khan'
else:
    if  candidate.count('Correy') > candidate.count('Li') & candidate.count("O'Tooley") & candidate.count('Khan'):
        winner = 'Correy'  
    else:
        if candidate.count('Li') > candidate.count('Correy') & candidate.count("O'Tooley") & candidate.count('Khan'):
            winner = 'Li' 
        else:
            if candidate.count("O'Tooley") > candidate.count('Correy') & candidate.count('Li') & candidate.count('Khan'):
                winner = "O'Tooley" 

print(f'Election Results')
print(f'---------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------')
print(f'{Khan_Votes} {khan_perc} ({Khan_Votes})')
print(f'{CorreyVotes} {correy_perc} ({CorreyVotes})')
print(f'{li_perc} {li_perc} ({LiVotes})')
print(f'{OTooleyVotes} {otooley_perc} ({OTooleyVotes})')
print(f'---------------------------')
print(f'Winner: {winner}')
print(f'---------------------------')    


#Write text file output
final_analysis = open("Results.txt","w")

final_analysis.write(f'Results\n')
final_analysis.write(f'---------------------------\n')
final_analysis.write(f'Total Votes: {total_votes}\n')
final_analysis.write(f'---------------------------\n')
final_analysis.write(f'{Khan_Votes} {khan_perc} ({Khan_Votes})\n')
final_analysis.write(f'{CorreyVotes} {correy_perc} ({CorreyVotes})\n')
final_analysis.write(f'{li_perc} {li_perc} ({LiVotes})\n')
final_analysis.write(f'{OTooleyVotes} {otooley_perc} ({OTooleyVotes})\n')
final_analysis.write(f'---------------------------\n')
final_analysis.write(f'Winner: {winner}\n')
final_analysis.write(f'---------------------------\n')   

final_analysis.close()
