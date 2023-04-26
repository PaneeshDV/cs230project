rm a.txt
grep 'CPU 0 cumulative IPC:' < "$1" | awk '{printf $5 ", "}' >> a.txt
grep 'LLC TOTAL     ACCESS: ' < "$1" | awk '{print $6 ", " $8}' >> a.txt