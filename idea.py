# --- PLOTLE ---
# - browser
# - logic game 
# - daily/weekly 
# - uses Pandas / data science

# Idea: 
# A fake videogame esports tournament just happened
# On the left, you see probabilities of events happening from the game code
# On the right, you see player stats, how many times things have happened across playtime
# By identifying statistically improbable stats of a player, you have to finalize your list of cheaters and non-cheaters
# There's tons of stats everywhere
# Statistics differ based on player's "role" on the team, making just looking at the numbers harder
# By picking players and particular stats and the type of graph, you can generate the plot in the central window (PLOTLE!)
# You are given bonus points if you highlight which stats gave away the cheater
# Negative points for mistakes on stats or cheaters
# The faster you do - the more points
# Weekly leaderboards, with week's winners recorded forever

# Workflow:

# Iterate: make a simple prototype first with:
# - random seed
# - random team names
# - random usernames
# - 3 players per team
# - 2 teams
# - 2 possible roles
# - 5 stats per player

# !!! UPDATED: half data mystery, half management sim !!!

# 1) Do the backend first
# [v] make one team's total deaths equal total kills of the opposition
# [v] add game elements that are chance/timing based --- something has a chance to happen once per in game minute
# at first: just runes spawning and neutral monsters being killed
# add to the player's stats 
# [v] incorporate runes and neutrals into how the game determines player stats and, therefore, the winners!
# [v] add cheaters

# 2) PIVOT: make it an actual game: esports manager
# [v] have player objects where their skills affect the outcome
# [v] IGL: gives +% or -% to other players' performances (not themselves) based on leadership stat | can be assigned and changed in Team class
# [v] incorporate pandas: generate a DF from the match report 
# [v] create a system that will run 100 simulations and give me W-L to tell me balance
# [v] separate engine from console logs
# [v] player generator (for recruitment)
# [v] create a gameplay loop (console-based) 
# - separate engine with console logs!!!
# - management gameplay, recruitment, switching players between roles, subs, igl appoint
# [_] add season_ending and post season shuffle [WATCH THE SPLIT OF CONCERNS!!!]
# [_] cheater spotting with high score and timing / data science gameplay | based on data for rewards and penalties on timing and accuracy
# [_] expand static data sciences
# - Pandas layer – THE “ENGINE under the hood for the interactive portion. Each match can export a .csv or .pkl for reproducibility.

# 3) EXPAND and POLISH
# [_] add heroes and show specific heroes on the match report and hero descriptions on the game lore and mechanics info cards
# [_] more timing and chance based mechanics for ultimate data science
# [_] create a game mechanics / chances print with lore and explanations
# [_] make sure the below ALL are stored in the engine parts, not the console/frontend parts!!!
# [v] add league standings
# [_] add skill growth
# [_] add pick and ban heroes
# [_] tweak cheating numbers
# [_] Cheater realism – Instead of just scaling kills/assists, occasionally break correlations 
# - e.g., high kills but no runes taken, or extreme KDA inconsistency with team averages
# - that makes detection more subtle
# [_] Data storytelling – Add post-match “press report” text generated from outliers 
# - “Fans are questioning how ylari_x secured 47 kills with only 2 rune pickups…”

# 4) REACT FRONTEND
# [_] make repo
# [_] create manager / between matches UI
# [_] create post-match cheaters finding UI: 
# [LEFT]  Expected probabilities / baselines  
# [CENTER]  interactive / changeable visualizations (tweak numbers / players / type of graph)  
# [RIGHT]  Player data / filters / suspected cheaters

# 5) Local savegame files
# 6) Third window - dots fighting match simulation
# 7) Plotle mode - just detect cheaters based on a randomly generated match timing-wise. 
# - Three difficulties - cheating numbers adjusted - total time / errors / accuracy counted for high score