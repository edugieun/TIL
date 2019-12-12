# Vue Tip

## npm shrinkwrap

- `pip freeze > requirements.txt`와 같은 역할을 하며, `npm-shrinkwrap.json`이라는 파일을 생성한다.
- `npm install` 명령어 사용시 원래는 `package.json`의 명세를 따라 `node_module`을 설치하지만, `npm-shrinkwrap.json` 파일이 존재하면 `npm-shrinkwrap.json` 파일의 명세를 따라 설치한다.

