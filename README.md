<p align="center">
  <h1 align="center"> Memory/Cache hierarchy optimizations for SAT solvers </h1>
  
  <p> In this project we evaluated different cache hierarchies (different sizes of L1, L2, LLC,inclusive/non-inclusive/Exclusive) and cache replacement policies, compared with a baseline cache hierarchy, and tried to improve the cache performance. 
 </p>
</p>

# Clone the repository
```
git clone https://github.com/PaneeshDV/cs230project.git
```


# Compile

ChampSim takes eight parameters: Branch predictor, L1I prefetcher, L1D prefetcher, L2C prefetcher, LLC prefetcher, LLC replacement policy, number of cores, and the inclusion policy
For example, `./build_champsim.sh bimodal no no no next_line lru 1 I` builds a single-core processor with bimodal branch predictor, no L1 instruction prefetcher, no L1/L2 data prefetchers, ip-stride LLC prefetcher, baseline LRU replacement policy for the LLC, and Inclusive cache policy.
```
$ ./build_champsim.sh bimodal no no no next_line lru 1 I

$ ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} ${Inclusion policy}
```

# Run simulation

Execute `run_champsim.sh` with proper input arguments. The default `TRACE_DIR` in `run_champsim.sh` is set to `$PWD/dpc3_traces`. <br>

* Single-core simulation: Run simulation with `run_champsim.sh` script.

```
Usage: ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
$ ./run_champsim.sh bimodal-no-no-no-next_line-lru-1core-I 20 30 cadical-high-60K-1227B.champsimtrace.xz

${BINARY}: ChampSim binary compiled by "build_champsim.sh" (bimodal-no-no-no-next_line-lru-1core-I)
${N_WARM}: number of instructions for warmup (20 million)
${N_SIM}:  number of instructinos for detailed simulation (30 million)
${TRACE}: trace name (cadical-high-60K-1227B.champsimtrace.xz)
${OPTION}: extra option for "-low_bandwidth" (src/main.cc)
```
Simulation results will be stored under "results_${N_SIM}M" as a form of "${TRACE}-${BINARY}-${OPTION}.txt".<br> 


# Files added
**Added cache_inclusion_policies folder**
* I.cc (Inclusive Policy)
* E.cc (Exclusive Policy)
* N.cc (Non-inclusive-non-exclusive policy)

**In prefetcher folder**
* best_offset.l2c_pref

**In replacement folder**
* fifo.llc_repl
* lfu.llc_repl
* rand.llc_repl

**SAT solver traces in dpc3_traces**
* cadical-high-60K-1227B.champsimtrace.xz
* cadical-high-60K-134B.champsimtrace.xz
* kissat-inc-high-30K-1802B.champsimtrace.xz

**For generating results and plots**
* generate_results.sh (collects results by evaluating with different Cache inclusive and Cache replacement policies for all three traces)
* run.sh (script to extract ipc value, hit rate, miss rate from the generated results)
* data.csv (contains the extracted values)
* test.ipynb (Used to generate plots from the results generated)
* test.py (same as above but a python script)

**Results**
* These folders are the results generated when 20 million instruction for warmup and 30 million for simulation are used for all inclusion and replacement policies for the three traces.
  * results_30M_a ( When LLC_SET = NUM_CPUS*2048, LLC_WAY = 16)
  * results_30M_b ( When LLC_SET = NUM_CPUS*8192, LLC_WAY = 16)
  * results_30M_c ( When LLC_SET = NUM_CPUS*16384, LLC_WAY = 32)
  * results_30M_d ( When LLC_SET = NUM_CPUS*65536, LLC_WAY = 32)
  
**Presentation**
* Slides : [Presentation Slides](https://iitbacin-my.sharepoint.com/:p:/g/personal/210050096_iitb_ac_in/Edq1l_KecGZMszam3BCRpScBD9BzUPDo4o7Jg7Dbh_DzNA?e=wAheVV)
* Youtube link : [Presentation Video](https://youtu.be/4C5m3V3TlLg)
