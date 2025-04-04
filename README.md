# CodeScript Demo

This repository contains the demo version for [CodeScript](http://codescript-demo-env.eba-edrru6it.us-east-2.elasticbeanstalk.com/) using AWS Elastic Beanstalk.

For the local version of the app, check out these repositories:

- [codescript-backend](https://github.com/jjpark987/codescript-backend)
- [codescript-frontend](https://github.com/jjpark987/codescript-frontend)

Please read this [Dev article](https://dev.to/jjpark987/building-a-code-problem-solving-assistant-4b71) for more details.

## AWS Elastic Beanstalk

1. Initialize Elastic Beanstalk

```zsh
eb init
```

2. Create an environment

```zsh
eb create codescript-demo-env
```

3. Deploy application

```zsh
eb deploy --verbose
```
