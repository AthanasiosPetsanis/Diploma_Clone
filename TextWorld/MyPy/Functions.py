import gym
import textworld.gym
from textworld import EnvInfos

# Register a text-based game as a new Gym's environment.


# --- Make random game ---

# options = textworld.GameOptions()
# options.path = "./Random_Games/"
# options.seeds = 432
# game = make_game(options)
# game_file = compile_game(game, options)
# print(game_file)
# -----------------------------


# --- Make random game with quick command ---

# THIS DOES NOT OVERWRITE GAMES WITH EXISTING NAMES!
# !tw-make custom --world-size 2 --nb-objects 5 --theme house --quest-length 4 --quest-breadth 2 --entity-numbering --output "./Created_Games/MDP_Game.ulx" --seed 5 --format ulx

# -------------------------------------

# Load Game
def load_game(game_file, max_steps=100):

    request_infos = EnvInfos(inventory=True, admissible_commands=True, entities=True, won=True, lost=True, intermediate_reward=True,
                             description=True, location=True, objective=True, score=True, moves=True)

    env_id = textworld.gym.register_games([game_file], request_infos, max_episode_steps=max_steps)

    env = gym.make(env_id)  # Start the environment.

    obs, infos = env.reset()# Start new episode.

    print(obs)

    score, moves, done = 0, 0, False
    return env, obs, infos