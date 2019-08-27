# Git

## 기본명령어

1. git init 저장소 초기화
2. `git add`
3. `git commit`
4. `git push` 

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






