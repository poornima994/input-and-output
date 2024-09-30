'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18

'''
def get_team_details(team_number):
    print(f"Team {team_number}:")
    team_name = input("Team Name:\n").strip()
    score = input("Score:\n").strip()
    overs = input("Overs played:\n").strip()
    return team_name, score, overs


def display_match_details(team1, team2):
    print("Match Details:")
    print(f"Team 1:\nName: {team1[0]}\nScore: {team1[1]}\nOvers played: {team1[2]}")
    print(f"Team 2:\nName: {team2[0]}\nScore: {team2[1]}\nOvers played: {team2[2]}")


if __name__ == "__main__":
    team1_details = get_team_details(1)
    team2_details = get_team_details(2)
    display_match_details(team1_details, team2_details)
