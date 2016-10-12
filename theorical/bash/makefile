
pdf:
	rm -f  `ls  | grep -vP "(\.pdf)|(\.jpeg)|(\.jpg)|(\.tex)|(\.ps)|(makefile)"`
	PID=`ps aux | grep acroread | tr -s " " | cut -f2 -d " " ` 
	if [ $$PID ]; then kill -9 $$PID; fi
	PID=`ps aux | grep pdflatex | tr -s " " | cut -f2 -d " " ` 
	if [ $$PID ]; then kill -9 $$PID; fi
	pdflatex  unix_course_dp.tex
	pdflatex  unix_course_dp.tex
	acroread unix_course_dp.pdf
