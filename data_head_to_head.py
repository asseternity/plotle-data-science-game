import pandas as pd
from team import Team

def head_to_head_stats(team1: Team, team2: Team):
    # collect matches where the two faced each other
    head_to_head_matches = []
    for match in team1.season_match_history:
        if match.team1.name == team2.name or match.team2.name == team2.name:
            head_to_head_matches.append(match)

    data_matches = []

    for index, match in enumerate(head_to_head_matches, start=1):
        data_matches.append({
            "Match #": index,
            "Winner": match.winner.name if match.winner else None,
            "Duration (min)": match.duration_in_minutes,
            "Team1": match.team1.name,
            "Team2": match.team2.name,
            "Team1 Kills": match.team1report.total_kills(),
            "Team1 Deaths": match.team1report.total_deaths(),
            "Team1 Assists": match.team1report.total_assists(),
            "Team1 PlayerReports": match.team1report.player_stats,
            "Team2 Kills": match.team2report.total_kills(),
            "Team2 Deaths": match.team2report.total_deaths(),
            "Team2 Assists": match.team2report.total_assists(),
            "Team2 PlayerReports": match.team2report.player_stats
        })

    df_matches = pd.DataFrame(data_matches)

    team1_wins = (df_matches["Winner"] == team1.name).sum()
    team1_kills = df_matches["Team1 Kills"].sum()
    team1_deaths = df_matches["Team1 Deaths"].sum()
    team1_assists = df_matches["Team1 Assists"].sum()
    
    team2_wins = (df_matches["Winner"] == team2.name).sum()
    team2_kills = df_matches["Team2 Kills"].sum()
    team2_deaths = df_matches["Team2 Deaths"].sum()
    team2_assists = df_matches["Team2 Assists"].sum()

    df_team_stats = pd.DataFrame({
        "Team": [ team1.name, team2.name ],
        "Wins": [ team1_wins, team2_wins ],
        "Kills": [ team1_kills, team2_kills ],
        "Deaths": [ team1_deaths, team2_deaths ],
        "Assists": [ team1_assists, team2_assists ],
    })

    df_player_stats = pd.DataFrame(columns=[
        "Username", "Real Name", "Team",
        "Total Kills", "Total Deaths", "Total Assists",
        "Average Kills", "Average Deaths", "Average Assists"
    ])

    for prs in df_matches["Team1 PlayerReports"] + df_matches["Team2 PlayerReports"]:
        for pr in prs:
            username = pr.player.username
            real_name = pr.player.real_name
            team_name = pr.player.team.name
            if username not in df_player_stats["Username"].values:
                df_player_stats.loc[len(df_player_stats)] = {
                    "Username": username,
                    "Real Name": real_name,
                    "Team": team_name,
                    "Total Kills": pr.kills,
                    "Total Deaths": pr.deaths,
                    "Total Assists": pr.assists,
                    "Average Kills": 0,
                    "Average Deaths": 0,
                    "Average Assists": 0,
                }
            else:
                # Find the index of the first row in df_player_stats where the Username column matches this specific username
                index = df_player_stats.index[df_player_stats["Username"] == username][0]
                df_player_stats.at[index, "Total Kills"] += pr.kills
                df_player_stats.at[index, "Total Assists"] += pr.deaths
                df_player_stats.at[index, "Total Deaths"] += pr.assists

    # fill the player averages
    df_player_stats["Average Kills"] = df_player_stats["Total Kills"] / len(head_to_head_matches)
    df_player_stats["Average Deaths"] = df_player_stats["Total Deaths"] / len(head_to_head_matches)
    df_player_stats["Average Assists"] = df_player_stats["Total Assists"] / len(head_to_head_matches)

    return { "team_stats": df_team_stats, "player_stats": df_player_stats }