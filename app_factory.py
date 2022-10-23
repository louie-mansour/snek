from flask import Flask, request

from controller.rest_controller import RestController
from repo.grid_repo import GridRepo
from repo.input_command_repo import SnekCommandRepo
from usecase.use_cases import UseCases
from view.grid_view import GridView

app = Flask(__name__)

use_cases = UseCases(GridRepo(), SnekCommandRepo())
rest_controller = RestController(
    UseCases(
        GridRepo(),
        SnekCommandRepo()
    ),
    GridView()
)


@app.route("/snek/join", methods=['PUT'])
def join():
    return rest_controller.join_game()


@app.route("/snek/set-direction", methods=['PUT'])
def set_direction():
    return rest_controller.set_direction(request)

