curl  -s -X POST -H "content-type:application/json" -d '{"swaggerUrl":"https://raw.githubusercontent.com/tmkasun/me_api/master/me-api.yaml"}' https://generator.swagger.io/api/gen/servers/python-flask | python3 -c "import sys, json; print(json.load(sys.stdin)['url'])"