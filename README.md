1. Always pull latest main
- git checkout main
- git pull
2. create a branch 
- git checkout -b feature/branchname
3. add commits to branch
- git add filename.txt (add src/ in case of working in subfolder)
- git commit -m "commit message"
4. when ready push branch to github
- git push
5. open PR into main (on github)
6. review PR
7. make changes on branch if needed then push changes
8. merge branch
9. delete branch

if you accidentaly added commits to your local main, ```git checkout main``` , then run this command ```git reset --hard origin/main```