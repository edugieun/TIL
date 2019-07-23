## 다른 컴퓨터에서 연결할 때

```bash
git clone <주소>
git push gitlab master ? 
```





## 한 폴더를 여러 웹(github, gitlab)에 동시 연결할 때

```bash
git remote add <원하는 이름> <레포 주소>
git remote -v # 연결됐는지 확인 또는 몇 개 연결되어있는지 확인
git push -u <올리고 싶은 곳> (master) # 최초 연결시 접속 아뒤랑 비번 / master를 추가하면 해당 branch가 master가 됨
# 여러 사이트에 연결되어 있을 경우 -u <올릴 곳>을 지정한 후 push 해야한다.
아니면 한번에 올릴려면
$ git push origin master && git push gitlab master
```

