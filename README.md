README
===========

## build

```bash
$ docker build -t koduki/example-ml .
```

## run
```bash
$ docker run -it --rm -v `pwd`/.:/app -p 8080:8080 koduki/example-ml /bin/bash
root@1d10c93c7d38: jupyter notebook --ip=127.0.0.1 --port=8080 --allow-root
```
