from flask import Flask, jsonify, request
from flask_talisman import Talisman

import ssl

from src.core.Isolate import Isolate
from src.dto.RequestRunDTO import RequestRunDTO
from src.utils.EnvironmentVariable import EnvironmentVariables

app = Flask(__name__)
Talisman(app, content_security_policy=None)
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.load_cert_chain("/etc/letsencrypt/live/thebox.nathabox.fr/fullchain.pem", "/etc/letsencrypt/live/thebox.nathabox.fr/privkey.pem")

isolate = Isolate()


def load_env():
    EnvironmentVariables()


@app.get('/')
def default():
    return jsonify({'message': 'TheBox API'})


@app.route('/run', methods=['POST'])
async def post_run():
    body = request.get_data()
    request_run_dto = RequestRunDTO.from_json(body)
    box_id = await isolate.init_box(request=request_run_dto)
    res = await isolate.run_steps(box_id=box_id, steps=request_run_dto.steps)
    await isolate.delete_box(box_id=box_id)
    return jsonify(res)


if __name__ == '__main__':
    load_env()
    app.run(host='0.0.0.0', ssl_context=ctx)
