from flask import Flask, request

from controller.rest_controller import RestController
from repo.grid_repo import GridRepo
from repo.input_command_repo import SnekCommandRepo
from usecase.next_frame import NextFrameUseCase
from usecase.set_snek_direction import SetSnekDirectionUseCase
from view.grid_view import GridView

app = Flask(__name__)

snek_command_repo = SnekCommandRepo()

rest_controller = RestController(
    SetSnekDirectionUseCase(
        snek_command_repo,
    ),
    NextFrameUseCase(
        GridRepo(),
        snek_command_repo
    ),
    GridView()
)


@app.route("/snek/join", methods=['PUT'])
def join():
    return rest_controller.join_game()


@app.route("/snek/set-direction", methods=['PUT'])
def set_direction():
    return rest_controller.set_direction(request)

