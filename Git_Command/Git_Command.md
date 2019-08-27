## Git

Git Command 정리 

Git = (분산)버전관리 시스템

코드의 이력(history)를 관리하는 도구

개발된 과정의 역사를 볼 수 있고, 특정 시점으로 복구 가능

```

```

### Command 정리

 1.git init =깃 초기화

2.git init입력하기전에 (master가 있는지 꼭 확인)

point! 저장소안에는 또다른 저장소가 있지 않게끔 해줘야함

3.gitignore.io =특정 파일만 git이관리하지 않게끔 설정함.



## Git 되돌리기

1.commit 메시지 수정 = git 커밋 내용 수정

```bash
$git commit --amend 
```

​	git bash에서 vim편집기가 실행된다

​	편집모드(i)눌러서 수정후 ese + :wq로 저장 및 종료!

​	<push 전에만 해야함>

​	되돌리때는 , push,즉, 원격 저장소에 올린 이후에는 진행하면 

​	충돌이 무조건 발생하니 항상 조심해야한다!

​	why? 커밋을 다시 하게 되면 해시값이 변경되기 때문!

​	(즉 이력 자체가 변경이 되서 안됨)



#### Git commit전후 HASH값 비교!

$ git commit --amend
[master afab70f] 백준 - 기본문제 1001
 Date: Tue Aug 27 10:27:49 2019 +0900
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.py

##### 해쉬값이 변경된다 [master afab70f ->3bc42d8]

$ git commit --amend
[master 3bc42d8] 백준 - 기본문제 1001 !
 Date: Tue Aug 27 10:27:49 2019 +0900
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.py



git log시

$ git log
commit 3bc42d854b2f3166db47973a7993b42b8578bf7b (HEAD -> master)
Author: IlsanJerry <superpcw1080@naver.com>
Date:   Tue Aug 27 10:27:49 2019 +0900

```bash
백준 - 기본문제 1001 !
```

git log = git log전체 

git log --oneline =git log간편히보기

##### 2-1. git reset HEAD a.py <---폴더명 or파일명

git add . 한거에서 add취소하려면 이렇게 수정가능.

##### 2-2.git Staging area(INDEX)에서 취소하기

```bash
$ git reset HEAD 파일명
student@M13045 MINGW64 ~/Desktop/Git_command/백준알고리즘 (master)
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   a.py


student@M13045 MINGW64 ~/Desktop/Git_command/백준알고리즘 (master)
$ git reset HEAD a.py
Unstaged changes after reset:
M       a.py

student@M13045 MINGW64 ~/Desktop/Git_command/백준알고리즘 (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   a.py

no changes added to commit (use "git add" and/or "git commit -a")


```

#### 	특정파일을 Git 이력에서 더이상 관리하지 않게끔 설정

실제로는 삭제안하고 git관리에서만 추방

```bash
$git rm --cached 파일명
```

​	한번도 커밋된 이력이 없을 때에는 staging area에서 취소와 동일함

​	다만,커민에 포함된 적있는 경우에는 삭제 커밋이 됨.

​	(실제 파일은 삭제되지않음.)



#### Git에 1,2,3번파일중에 1,2번 파일만 커밋만됫을때

#### 그 상황에서 3번 파일을 넣고 싶을떄!

-git add하고 다시 commit (ammend) 로 할때!

```bash
$git add a.py 
$git commit -m 'a.txt,b.txt추가'
이 상황에서 b.py도 추가 하고 싶을떄
$git add b.py
$git commit --amend
(이러면 b.py까지 같이 추가됨)
```

commit 메시지를 수정하기전에 staging area에 변경을 해주면,

해당 파일까지 포함하여 다시 커밋을 



### 5.현재 작업 내역 커밋 시점으로 되돌리기

예를들어, 특정파일을 삭제하였거나, 혹은 코드 수정과정에서

오류가 많이 발생하여 직전 커밋 시점상태로 돌아가고 싶을때 사용이 가능함

(커밋만 일단 해놓으면 혹시 실수로 변경 및

삭제해도 그 상태로 돌아가는건 쉽다)

(커밋이 안된 상태에서의 복구는 절대 불가.)

```bash
$git checkout -- 파일명
```



## git reset vs revert

이력자체를 초기화 시켜버리는 내용

...?안되는데요?



# Git

## 기본명령어

1. 저장소 초기화
2. `git add`
3. `git commit`

## Git 되돌리기

1. commit 메시지 수정

   ```
   $ git commit --amend
   ```

   - git bash에서 vim이 실행된다.
   - 편집모드(`i`) 상태에서 수정후 esc+`:wq`
   - `push` , 즉, 원격저장소에 올린 이후에는 진행하면 충돌이 무조건 발생한다.
   - 커밋을 다시 하게 되면 해시값이 변경되기 때문!

2. Staging area(INDEX)에서 취소하기

   ```
   $ git reset HEAD programmers/
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           modified:   "백준알고리즘/1001.py"
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           programmers/
   ```

3. git 이력에서 특정 파일 삭제 커밋

   ```
   $ git rm --cached 파일명
   ```

   - 한번도 커밋된 이력이 없을 때에는 staging area에서 취소와 동일함.
   - 다만, 커밋에 포함된 적 있는 경우에는 삭제 커밋이 됨. (실제 파일은 삭제되지 않음!)

4. 특정 파일 포함해서 다시 커밋

   ```
   $ git add a.py
   $ git commit -m 'a, b 추가'
   $ git add b.py
   $ git commit --amend
   ```

   - commit 메시지를 수정하기전에 staging area에 변경을 해주면, 해당 파일까지 포함하여 다시 커밋을 진행함.

5. 현재 작업 내역 커밋 시점으로 되돌리기

   예를 들어, 특정 파일을 삭제하였거나 혹은 코드 수정과정에서 오류가 많이 발생하여 직전 커밋 시점 상태로 돌아고 싶을 때 사용이 가능함.

   ```
   $ git checkout -- 파일명
   ```






  