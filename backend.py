from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the durations for each state for top left and bottom right lights
state_durations_top_left_bottom_right = {
    'green': 4,
    'yellow': 1,
    'red': 5
}

# Define the durations for each state for top right and bottom left lights
state_durations_top_right_bottom_left = {
    'red': 5,
    'green': 4,
    'yellow': 1
}

# Define the initial states and next states for each pair of lights
initial_state_top_left_bottom_right = 'green'
next_states_top_left_bottom_right = ['yellow', 'red', 'red', 'yellow', 'green']

initial_state_top_right_bottom_left = 'red'
next_states_top_right_bottom_left = ['green', 'yellow', 'red', 'red', 'yellow']

@app.route('/color', methods=['GET'])
@cross_origin()
def get_color():
    current_time = time.time()
    elapsed_time = current_time % sum(state_durations_top_left_bottom_right.values())

    # Determine the current state for top left and bottom right lights based on elapsed time
    cumulative_duration = 0
    for state, duration in state_durations_top_left_bottom_right.items():
        cumulative_duration += duration
        if elapsed_time < cumulative_duration:
            current_state_top_left_bottom_right = state
            break

    # Determine the current state for top right and bottom left lights based on elapsed time
    elapsed_time_top_right_bottom_left = current_time % sum(state_durations_top_right_bottom_left.values())
    cumulative_duration = 0
    for state, duration in state_durations_top_right_bottom_left.items():
        cumulative_duration += duration
        if elapsed_time_top_right_bottom_left < cumulative_duration:
            current_state_top_right_bottom_left = state
            break

    # Determine the next state for top left and bottom right lights based on the current state
    current_index = next_states_top_left_bottom_right.index(current_state_top_left_bottom_right)
    next_state_top_left_bottom_right = next_states_top_left_bottom_right[(current_index + 1) % len(next_states_top_left_bottom_right)]

    # Determine the next state for top right and bottom left lights based on the current state
    current_index = next_states_top_right_bottom_left.index(current_state_top_right_bottom_left)
    next_state_top_right_bottom_left = next_states_top_right_bottom_left[(current_index + 1) % len(next_states_top_right_bottom_left)]

    response = make_response(jsonify({
        'topLeftBottomRight': current_state_top_left_bottom_right,
        'topRightBottomLeft': current_state_top_right_bottom_left
    }))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5001)
