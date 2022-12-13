from flask import Flask, jsonify, request

from src.core.Isolate import Isolate
from src.dto.RequestRunDTO import RequestRunDTO
from src.utils.EnvironmentVariable import EnvironmentVariables

app = Flask(__name__)
isolate = Isolate()


def load_env():
    EnvironmentVariables()


@app.route('/run', methods=['POST'])
async def post_run():
    body = request.get_data()
    request_run_dto = RequestRunDTO.from_json(body)
    box_id = await isolate.init_box(request=request_run_dto)
    # res = await isolate.run_steps(box_id=box_id, steps=request_run_dto.steps)
    # await isolate.delete_box(box_id=box_id)
    # return jsonify(res)
    return {}

if __name__ == '__main__':

    load_env()
    app.run(host='0.0.0.0', port=5002)
