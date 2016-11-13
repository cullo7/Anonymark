COUNTER=1
while [ $COUNTER -lt 10 ]; do
	echo "$COUNTER"
	python3 main.py test_suite/$COUNTER.png test_suite/Altered.png
	let COUNTER+=1
done
