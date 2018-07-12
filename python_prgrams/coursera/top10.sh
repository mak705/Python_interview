for i in $(cat nps)
do
zgrep -a "cr.action" /backup2/analyzeaccesslog/access_log.2015-06-10.tar.gz | grep "npKey=$i" | grep -oP "newsUid=[0-9]*" | cut -d "=" -f2 | sort | uniq -c > /home/makbul.hussain/$i.txt

#cat /home/makbul.hussain/$i | sort -nr | head -10 > /home/makbul.hussain/$i_top10.txt
done
