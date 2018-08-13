cd /Users/jiangmingjie/Desktop/leetcode/shell
mkdir tempdir
cd tempdir
top -n 1 >> tmpfile1.txt
grep ‘Tasks:*’ tmpfile1.txt >> tmpfile2.txt
grep ‘Cpu(s):*‘ tmpfile1.txt >> tmpfile2.txt
grep ‘Mem:*’ tmpfile1.txt >> tmpfile2.txt
grep ‘Swap:*’ tmpfile1.txt >> tmpfile2.txt
rm -f tmpfile1.txt
mv tmpfile2.txt top_short.txt
echo top_short.txt
rm -rf tempdir
echo farewell
 

