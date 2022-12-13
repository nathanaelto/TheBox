# TheBox

## Description :
Secure sandboxing system for untrusted code execution.

It uses [isolate](https://github.com/ioi/isolate) which uses specific functionalities of the Linux kernel.


## Dependencies :
```shell
pip3 install uuid
pip3 install python-dotenv
pip3 install typing
pip3 install typing_extensions
pip3 install zipfile
pip3 install flask
pip3 install dataclasses_json
pip3 install "Flask[async]"
pip3 install httpx
pip3 install asgiref
```

## Docker :
```shell
cd base-install

docker build . -t the-box-base

cd ..

docker build . -t the-box

# discret mode
docker run --privileged -d -p 5002:5002 --restart=always --name runner the-box 

# interactive mode
docker run --privileged -it -p 5002:5002 --name runner the-box 
```

```shell
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
```

## Fonctionnement : in progress:

### Input json :
```json
{
  "steps": [
    {
      "name": "step 1",
      "script": "script1 encoded in base64"
    },
    {
      "name": "step 2",
      "script": "script2 encoded in base64"
    }
  ],
  "settings": {
    "run_time_limit": "5",
    "wall_time_limit": "10",
    "stack_size_limit": "128000",
    "process_count_limit": "120",
    "storage_size_limit": "10240",
    "memory_limit": "512000"
  },
  "files": "files to need for steps zipped and encoded in base64"
}
```

### Output json :
```json
{
  "steps": [
    {
      "name": "step1",
      "status": 0,
      "stdout": "",
      "stderr": "",
      "time": 0.037,
      "time_wall": 0.043,
      "memory_used": 6640
    },
    {
      "name": "step2",
      "status": 0,
      "stdout": "VALUES",
      "stderr": "",
      "time": 0.002,
      "time_wall": 0.007,
      "memory_used": 856
    }
  ]
}
```
