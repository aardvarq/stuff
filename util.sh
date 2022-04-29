if [[ ! $2 ]]; then
  ./util.py
  exit
fi 

git checkout master 1>/dev/null 2>&1

echo "Fetching record list..."
git pull origin  1>/dev/null 2>&1

./util.py $1 $2

if [[ $1 == add || $1 == remove ]] ; then
  echo "Updating record list..."
  git add records.json 1>/dev/null 2>&1
  git commit -m "update records.json" 1>/dev/null 2>&1
  git push origin master 1>/dev/null 2>&1
  echo Done.
fi
