# CodeScript Demo

This repository contains the demo version for [CodeScript](http://codescript-demo-env.eba-edrru6it.us-east-2.elasticbeanstalk.com/) using an AWS serverless Lambda backend and a static S3-hosted frontend.

For the local version of the app, check out these repositories:

- [codescript-backend](https://github.com/jjpark987/codescript-backend)
- [codescript-frontend](https://github.com/jjpark987/codescript-frontend)

Please read this [Dev article](https://dev.to/jjpark987/building-a-code-problem-solving-assistant-4b71) for more details.

## AWS Lambda

1. Set up .env with AWS credentials

2. Deploy Lambda backend and obtain endpoint url

```zsh
serverless deploy
```

3. Set up frontend/.env using endpoint url from step 2

4. Create a build version for frontend

```zsh
cd frontend
npm install
npm run build
aws s3 sync ../build/ s3://codescript-demo-frontend --delete
```
