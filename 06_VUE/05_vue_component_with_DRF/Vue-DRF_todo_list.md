# Vue와 DRF를 이용하여 Todo list 만들기

### Vue 개발 환경 설정

- `todo-front`: Vue-CLI로 Vue 개발 환경 생성 `vue create todo-front`
- `todo-back`: `todo-back` 폴더 생성 후 내부에서 Django를 위한 환결 설정
  - 가상환경 생성 / 장고 설치 / 프로젝트 및 앱 생성

### Vue (todo-front)

- `vue ui`에서 현재 폴더 경로가 잘 지정되어 있는지 확인 후, 다르다면 프로젝트 매니저로 경로 재설정
- ` @vue/cli-plugin-router ` 플러그인 설치  후, `history mode` 사용 체크(URL 주소에서 해쉬 뱅(#!)을 사용하지 않는다는 뜻)

## Login Component

### LoginForm component

- 로그인 폼 만들기
- axios로 장고에 요청하기