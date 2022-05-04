import asyncio

from flask import Flask, jsonify, request

from src.core.Isolate import Isolate
from src.dto.RequestRunDTO import RequestRunDTO
from src.dto.RequestRunSettingsDTO import RequestRunSettingsDTO
from src.dto.RequestRunStepDTO import RequestRunStepDTO
from src.utils.EnvironmentVariable import EnvironmentVariables

app = Flask(__name__)
isolate = Isolate()

file = 'UEsDBBQAAAAAAAGEoVQAAAAAAAAAAAAAAAAFACAAY29kZS9VVA0AB' \
       '+OZbmLjmW5i45luYnV4CwABBPUBAAAEFAAAAFBLAwQUAAgACABkS6' \
       'FUAAAAAAAAAABzAQAADAAgAGNvZGUvbWFpbi5weVVUDQAHTTZuYuS' \
       'ZbmLjmW5idXgLAAEE9QEAAAQUAAAAjY+xDoMwDER3f0WkLkFCDIyV' \
       'GPmF7ikxUiriRE7a8vk1ASQGkJrJucu9nEcOXmWc85dNVM7HwFk5s' \
       'kgZxsXr6bPLMjoO5MV7GDbuOWF9JvY0BIsMW+yVAgGAxVF540hXd1' \
       'ByUMDdWVxXxY/sKGt5tV5vm3D9n64aLFMJHSFLg8a+fUyLVW/7dW2' \
       'thil110SBlNoJh0D2ULz9r3kreVh3hp0B8ANQSwcIKyc0gKQAAABz' \
       'AQAAUEsBAhQDFAAAAAAAAYShVAAAAAAAAAAAAAAAAAUAIAAAAAAAA' \
       'AAAAO1BAAAAAGNvZGUvVVQNAAfjmW5i45luYuOZbmJ1eAsAAQT1AQ' \
       'AABBQAAABQSwECFAMUAAgACABkS6FUKyc0gKQAAABzAQAADAAgAAA' \
       'AAAAAAAAApIFDAAAAY29kZS9tYWluLnB5VVQNAAdNNm5i5JluYuOZ' \
       'bmJ1eAsAAQT1AQAABBQAAABQSwUGAAAAAAIAAgCtAAAAQQEAAAAA '

request_test = RequestRunDTO(
    "234567765",
    [
        RequestRunStepDTO(
            "Run",
            "ZWNobyAiUsOpc3VsdGF0IGRlIG1vbiBzY2lycHQi"
        )
    ],
    RequestRunSettingsDTO(),
    file
)


def load_env():
    EnvironmentVariables()


async def main():
    load_env()

    # box = Box.init_box("", "")
    # box.default_exec_settings()
    # print(box.exec_settings)

    box_id = await isolate.init_box(request_test)
    await isolate.run_steps(box_id, request_test.steps)
    await asyncio.sleep(10)
    await isolate.delete_box(box_id=box_id)


@app.route('/run', methods=['POST'])
async def post_run():
    body = request.get_data()
    request_run_dto = RequestRunDTO.from_json(body)
    # return 'ok'
    box_id = await isolate.init_box(request=request_run_dto)
    res = await isolate.run_steps(box_id=box_id, steps=request_run_dto.steps)
    await isolate.delete_box(box_id=box_id)
    return jsonify(res)


if __name__ == '__main__':
    # asyncio.run(main())
    app.run(host='0.0.0.0', port=5002)