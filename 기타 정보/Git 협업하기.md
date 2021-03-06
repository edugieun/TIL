# 협업 및 Branch 작업하기

## branch 작업 시 발생할 수 있는 상황

### 1.fast-forward

1. feature/test branch 이동

   ```bash
   $ git checkout -b feature/test
   $ (feature/test)
   ```

2. 작업 완료 후 commit

   ```bash
   touch test.md
   git add .
   git commit -m "Complete test.md"
   ```

3. master 이동

   ```bash
   git checkout master
   $ (master)
   ```

4. master에 병합

   ```bash
   git merge feature/test
   ```

5. 결과

   - 단순히 HEAD 가 최신 COMMIT 으로 이동
   - feature/test branch 생성 이후 master branch 의 이력에 변화가 없었기 때문

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```

---

### 2. merge commit 

1. feature/login branch 이동

   ```bash
   $ git checkout -b feature/login 
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch login.md
   $ git add .
   $ git commit -m "complete login.md"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 생성

   ```bash
   $ touch master.md
   $ git add .
   $ git commit -m "fix master.md"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/login
   ```

6. 자동으로 merge commit 발생

   ```bash
   Merge branch 'feature/login'
   
   # Please enter a commit ...
   ...
   ```

   - Vim 에디터로 열림
   - 메세지를 수정하고자하면 `i` 로 편집 모드로 바꾼다음에 COMMIT 을 수정하고
   - `esc` + `:wq` 를 통해 저장 및 종료

7. commit 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   ```

   ```bash
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/login
   ```

---

### 3. merge conflict

1. feature/article branch 생성 및 이동

   ``` bash
   $ git checkout -b feature/article
   ```

2. 작업 완료 후  commit

   ```bash
   # 충돌을 만들어 낼 파일에 코드를 작성
   $ git add .
   $ git commit -m "fixed minor update"
   ```

3. master 로 이동

   ```bash
   $ git checkout master
   ```

4. master 에 추가 commit 만들기

   ```bash
   # feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
   $ git add .
   $ git commit -m "fixed master update"
   ```

5. master 에 병합

   ```bash
   $ git merge feature/article
   ```

6. merge confict 발생

   ```bash
   $ git merge feature/article
   Auto-merging a.txt
   CONFLICT ...
   Automatic merge faild; fix conflicts and then commit result.
   ```

7. 충돌 확인 및 해결

   ```bash
   # 충돌이 일어난 파일 열기
   # 그럼 아래와 같은 내용이 있다.
   
   <<<<<<<< HEAD
   master 에서 작성한 내용
   ========
   feature/article 에서 작성한 내용
   >>>>>>>> feature/article
   
   # 원하는 코드로 수정
   ```

8. merge commit 진행

   ```bash
   $ git add .
   $ git commit
   ```

   - commit 메세지는 미리 작성되어 있음

9. commit 그래프 확인

   ```bash
   $ git log --oneline --graph
   *   7238aa2 (HEAD -> master) Merge branch 'feature/article'
   |\
   | * 8e84920 (feature/article) fix a.txt
   * | 28faf63 fix a.txt in master
   |/
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

10. branch 삭제

    ```bash
    $ git branch -d feature/article
    ```

    

## 협업 하기

### 1. feature branch workflow

- Pull request

- 기능 개발을 끝내고 master 에 바로 병합시키는게 아니라, 브랜치를 중앙 원격 저장소에 올리고(push), master 에 병합을 요청(merge)

주의사항

- 중앙에서 병합을 했다면, 다른 팀원들은 master 브랜치를 pull 받아야 한다.

---

### 2. forking workflow

- 권장하는 협업 방법
- 중앙 원격 저장소를 fork한 후, fork한 내 레포지토리를 clone한다.
- clone한 저장소에 중앙 원격 저장소를 추가한다.

```bash
$ git remote add upstream [중앙 원격 저장소 주소]
$ git remote -v
```

- 개발을 할 시 branch를 나눠 기능별로 작업한다.

```bash
$ git checkout -b feature/login
```

- 개발 완료 후 내 레포지토리로 개발 완료한 branch를 push 한다

```bash
$ git add .
$ git commit -m 'feature/login 개발완료'
$ git push origin feature/login
```

- 내 레포지토리로 들어가서 `pull request`를 요청한 후, 중앙 원격 저장소에서 `merge`를 승인하고 완료하면, master branch에서 upstream을 pull 받아 동기화한다.

```bash
$ git checkout master
$ git pull upstream master
```

------

## 명령어

- 생성 및 이동 : git checkout -b <branch>
- 이동 : git checkout <branch>
- 삭제 : git branch -d <branch>
- 푸시 : git push origin <branch>
- 머지 후 버전 맞추기
  - 다시 master로 돌아온 후에
  - git pull upstream master
- branch 머지하기
  - git merge <branch>
- 강제로 중앙 저장소(upstream) 동기화

```bash
$ git fetch --all
$ git reset --hard upstream/master
$ git pull upstream master
```

- 원하는 커밋 으로 돌아가기


```bash
$ git reset --hard <commit 버전>
$ git reset --hard a261df78acd53f8b93dff20098d1397a51caea55

reset 전에 추가된 파일이나, reset해도 지워지지 않는 파일이 있으므로
이를 삭제.
단, venv, .env 파일 또한 삭제되므로 주의.
$ git clean -dfx
```

