
# sh sleepsort.sh 3 1 4 1 5 9

f() {
    sleep "$1"
    echo "$1"
}
while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait