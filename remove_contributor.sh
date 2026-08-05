#!/bin/sh
# This script removes the contributor "Dm9582" from git history
# It replaces the git author/committer with "Akshata Yadav"

export OLD_NAME="Dm9582"
export NEW_NAME="Akshata Yadav"
export OLD_EMAIL="dhruv95682@gmail.com"
export NEW_EMAIL="akshata-yadav-20@example.com"

git filter-branch -rq --env-filter '
if [ "$GIT_COMMITTER_NAME" = "Dm9582" ] || [ "$GIT_AUTHOR_NAME" = "Dm9582" ]; then
    export GIT_COMMITTER_NAME="Akshata Yadav"
    export GIT_COMMITTER_EMAIL="akshata-yadav-20@example.com"
    export GIT_AUTHOR_NAME="Akshata Yadav"
    export GIT_AUTHOR_EMAIL="akshata-yadav-20@example.com"
fi
' HEAD