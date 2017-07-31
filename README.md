README
===========

## build

```bash
docker build -t koduki/example-ml .
```

## run
```bash
docker run -it --rm -v `pwd`/.:/app koduki/example-ml /bin/bash
```