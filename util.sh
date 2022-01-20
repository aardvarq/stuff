git checkout master 1>/dev/null 2>&1
git pull  1>/dev/null 2>&1
./util.py $1 $2

echo "Updating source of record"
git add records.json 1>/dev/null 2>&1
git commit -m "update records.json" 1>/dev/null 2>&1
git push origin master 1>/dev/null 2>&1
echo Done.
