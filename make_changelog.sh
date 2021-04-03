#!/bin/bash

OUTFILE=changes.txt

echo "Typing to crudely sort the changes"
echo "Features: " > $OUTFILE
hg log --template="- {desc} (r{rev})\n" | grep 'eature' >> $OUTFILE
hg log --template="- {desc} (r{rev})\n" | grep 'Doc' >> $OUTFILE
echo "" >> $OUTFILE
echo "Bug fixes: " >> $OUTFILE
hg log --template="- {desc} (r{rev})\n" | grep 'Fix' >> $OUTFILE
