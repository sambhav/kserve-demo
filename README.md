# kserve-demo

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/samj1912/kserve-demo)

1. Click the Open in Gitpod link
2. Run `pack build myapp`
3. Run `docker run -it -p 8080:8080 myapp`
4. Run `curl localhost:8080/v1/models/custom-model:predict -d @./input.json`
