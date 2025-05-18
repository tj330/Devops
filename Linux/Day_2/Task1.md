# Log File Analysis with AWK, Grep & Sed

Logs are crucial in DevOps! You’ll analyze logs using the Linux_2k.log file from [LogHub](https://github.com/logpai/loghub/blob/master/Linux/Linux_2k.log).

Use grep to find all occurrences of the word "error".

    grep -i error Linux_2k.log
Use awk to extract timestamps and log levels.

    awk '{timestamp = $1" "$2" "$3; loglevel = ""; for(i=6;i<=NF;i++) loglevel=loglevel" "$i; print timestamp " |" loglevel}' Linux_2k.log

    // NF is a predefined variable whose value is the number of fields in the current record.

    
Use sed to replace all IP addresses with [REDACTED] for security.

    sed -i 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/[REDACTED]/g' Linux_2k.log

    // -i flag will edit the input file in-place.

Find the most frequent log entry

    head -10 Linux_2k.log
