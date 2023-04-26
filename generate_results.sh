#!/bin/bash

traces="cadical-high-60K-1227B.champsimtrace.xz cadical-high-60K-134B.champsimtrace.xz kissat-inc-high-30K-1802B.champsimtrace.xz"
#traces="cadical-high-60K-1227B.champsimtrace.xz"
policies="I N E"
#policies="I"
repl_policies="fifo lfu lru rand"
#repl_policies="fifo"
for repl_polc in $repl_policies
do 
    for policy in $policies
    do 
        ./build_champsim.sh bimodal no no no no ${repl_polc} 1 ${policy}
        for trace in $traces
        do 
            echo ${repl_polc}
            echo ${trace}
            echo ${policy}
            time ./run_champsim.sh bimodal-no-no-no-no-${repl_polc}-1core-${policy} 20 30 ${trace} My
        done
    done
done

