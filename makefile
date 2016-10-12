################################################################
## Synchronize web site on the server

MAKEFILE=makefile

help:
	@echo 
	@echo "-Avalaible targets:"
	@perl -ne 'if (/^([a-z]\S+):/){ print "\t$$1\n";  }' ${MAKEFILE}
	@echo
	@echo "-Some examples:"
	@echo "\tmake publish"
	@echo "\tmake checkRCodeInHtml HTMLFILE=/path/to/html/file.html"
	@echo "\tmake extractRCodeFromHtml HTMLFILE=/path/to/html/file.html"
	@echo "\tmake extractBashCodeFromHtml HTMLFILE=/path/to/html/file.html"
	@echo

USER=teacher
HOST=pedagogix-tagc.univ-mrs.fr
WDIR=/homes/teacher/courses/jgb53d-bd-prog


EXCLUDED=--exclude *~ 	\
	--exclude .#*	\
	--exclude .DS_Store \
	--excluse ".*" \
	--excluse #* \
	--exclude makefile

## Directory to synchronize
EXCLUDED=--exclude jobs  \
	--exclude '*~' \
	--exclude '*.old' \
	--exclude '*.log' \
	--exclude '.DS_Store' \
	--exclude annotation_projects
RSYNC=rsync -ruptvl -e ssh -z  ${EXCLUDED} 


################################################################
## Clean temporary files created by emacs
clean:
	@find . -name '*~' -exec rm {} \;
	@find . -name '.#*' -exec rm {} \;
	@find . -name '.DS_Store' -exec rm {} \;

################################################################
## Publish on the web site
TO_SYNC=*
publish: clean
	@echo "Transfering as $(USER) to $(HOST) in wdir=$(WDIR)"
	@rsync -ruptvl ${EXCLUDED} ${OPT} ${TO_SYNC}  $(USER)@$(HOST):$(WDIR)

pushToGit:
	@git pull
	@git add .
	@git commit -m "Added something"
	@git push

pushAndPublish: pushToGit publish


chmoderemote:
	ssh $(USER)@$(HOST) "find $(WDIR) -type d -exec chmod 0755 {} \;" 
	ssh $(USER)@$(HOST) "find $(WDIR) -type f -exec chmod 0644 {} \;"

################################################################
## Browse the Web site
BROWSER=firefox
local:
	open -a ${BROWSER} http://localhost/courses/jgb53d-bd-prog

web:
	open -a ${BROWSER} http://pedagogix-tagc.univ-mrs.fr/courses/jgb53d-bd-prog


################################################################
## Convert iPython3 notebook
TD_NB=09
NOTEBOOK_DIR=practicals/${TD_NB}_python
NOTEBOOK=TD${TD_NB}_solutions
convert_notebook:
	(cd ${NOTEBOOK_DIR} ; \
	ipython3 nbconvert --to html ${NOTEBOOK}.ipynb ; \
	ipython3 nbconvert --to python ${NOTEBOOK}.ipynb ; \
	ipython3 nbconvert --to latex --post pdf ${NOTEBOOK}.ipynb)


################################################################
# Check R Code.
# Note that R code should be embeded in the following markup:
# <pre class="brush:r">  # or <pre class='brush:r'>
#  R code
# </pre>

ifdef MAKECMDGOALS
 ifeq ($(MAKECMDGOALS), checkRCodeInHtml)
  ifeq ($(HTMLFILE),)
   $(error HTMLFILE variable is undefined. Use: "make checkRCodeInHtml HTMLFILE=/path/to/html/file.html")<
  endif
 endif
endif

# This temporary file store the html code from which comments have been disgarded.
TMPFILE:=$(shell mktemp /tmp/check.XXXXXX)

checkRCodeInHtml:
	@perl -ne 'print unless (/<!--/../-->/)' $(HTMLFILE)  > $(TMPFILE)
	@perl -ne 'print if(/<pre\s+class=\s*[\047"]brush:r[\047"]\s*>/../<\/pre>/)' $(TMPFILE) | grep -Ev "<.?pre"  | R --vanilla
	@rm -f $(TMPFILE)

ifdef MAKECMDGOALS
 ifeq ($(MAKECMDGOALS), extractRCodeFromHtml)
  ifeq ($(HTMLFILE),)
   $(error HTMLFILE variable is undefined. Use: "make extractRCodeFromHtml HTMLFILE=/path/to/html/file.html")<
  endif
 endif
endif


extractRCodeFromHtml:
	@perl -ne 'print unless (/<!--/../-->/)' $(HTMLFILE)  > $(TMPFILE)
	@perl -ne 'print if(/<pre\s+class=[\047"]brush:r[\047"]\s*>/../<\/pre>/)' $(TMPFILE) \
		| grep -Ev "<.?pre"


ifdef MAKECMDGOALS
 ifeq ($(MAKECMDGOALS), extractBashCodeFromHtml)
  ifeq ($(HTMLFILE),)
   $(error HTMLFILE variable is undefined. Use: "make extractBashCodeFromHtml HTMLFILE=/path/to/html/file.html")<
  endif
 endif
endif

extractBashCodeFromHtml:
	@perl -ne 'print unless (/<!--/../-->/)' $(HTMLFILE)  > $(TMPFILE)
	@perl -ne 'print if(/<pre\s+class=.*?brush:bash.*?>/../<\/pre>/)' $(TMPFILE)   |  \
	grep -Ev "<.?pre" | perl -npe 's/^\s*//; s/#.*?$$//;' 

