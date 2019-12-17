# Vue Tip

## npm shrinkwrap

- `pip freeze > requirements.txt`와 같은 역할을 하며, `npm-shrinkwrap.json`이라는 파일을 생성한다.
- `npm install` 명령어 사용시 원래는 `package.json`의 명세를 따라 `node_module`을 설치하지만, `npm-shrinkwrap.json` 파일이 존재하면 `npm-shrinkwrap.json` 파일의 명세를 따라 설치한다.

## Troubleshooting

### npm install Error

- node_moudles 를 설치하기 위해 `npm install` 진행 시 다음과 같은 에러 발생

![image](https://user-images.githubusercontent.com/52814897/70999112-1a2a4480-211c-11ea-8cfc-10b4596e938d.png)

- `npm cache clean --force` 명령어로 캐시를 지운 후 재설치한다.