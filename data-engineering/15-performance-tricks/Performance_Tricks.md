# ⚡ Data Engineering Performance Tricks — Measure, Reduce, Verify

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Performance Tricks* course material (Rowad Misr Al-Raqmeya).
>
> 📌 *Format Note:* The companion `.py` and `.ipynb` files use only Python's standard library and local in-memory data. They do not require Spark, a database server, or cloud credentials.

---

## 📑 Table of Contents
1. [Measure Before Optimizing](#1-measure-before-optimizing)
2. [Reduce the Data](#2-reduce-the-data)
3. [Make Storage and Queries Work Together](#3-make-storage-and-queries-work-together)
4. [Process in Batches and Streams](#4-process-in-batches-and-streams)
5. [Parallelism Without Surprises](#5-parallelism-without-surprises)
6. [Spark-Specific Tuning](#6-spark-specific-tuning)
7. [A Performance Runbook](#7-a-performance-runbook)

---

## 1) Measure Before Optimizing

Performance is a relationship between workload, latency, throughput, memory, and cost. Establish a baseline with representative data and record:

* wall-clock duration and throughput;
* peak memory and CPU;
* input/output bytes and row counts;
* query plans, shuffle volume, and task skew;
* infrastructure cost and failure/retry count.

Optimize the largest measured bottleneck, then rerun the same benchmark. A faster result that changes row counts or semantics is not an optimization.

### A useful loop

1. Define the service-level target.
2. Capture a reproducible baseline.
3. Form one hypothesis.
4. Change one variable.
5. Compare correctness and resource metrics.
6. Keep or revert the change with evidence.

---

## 2) Reduce the Data

The cheapest row to process is the row never read.

1. **Project early:** Select only required columns.
2. **Filter early:** Apply selective predicates before joins and aggregations.
3. **Use compact types:** Avoid storing numeric IDs as long strings when a bounded integer is sufficient.
4. **Deduplicate intentionally:** Define the business key and keep the correct record by event/version time.
5. **Aggregate at the right grain:** Do not carry raw events through a pipeline when the consumer needs daily totals.
6. **Avoid repeated work:** Cache only expensive, reused results; materialize stable intermediate data when recomputation costs more than storage.

Be careful with premature caching: it consumes memory and can evict useful partitions.

---

## 3) Make Storage and Queries Work Together

### File layout

Columnar formats such as Parquet reduce I/O by reading only required columns and compressing similar values. Partition by common, low-to-medium cardinality filters such as date or region. Avoid partitions that create millions of tiny directories.

Compact small files into target-sized files appropriate for the engine. File size is a workload decision: too small increases scheduling overhead; too large reduces parallelism and makes retries expensive.

### Database layout

Indexes help selective lookups but add write and storage cost. Index columns used in frequent predicates and joins, then inspect the query plan. Composite index order matters: put the most selective and commonly constrained leading columns first for the access patterns you actually run.

Use parameterized SQL, return only required columns, and paginate large results. A query that joins before filtering may create a much larger intermediate relation than one that filters each side first.

---

## 4) Process in Batches and Streams

For large inputs, use bounded memory:

```python
for batch in read_batches(source, size=10_000):
    clean = transform(batch)
    write(clean)
```

Choose batch size from measurements. Too small increases overhead; too large increases memory pressure and retry cost. Make each batch idempotent using a deterministic key or replaceable partition.

Streaming systems need backpressure: when the sink slows down, the consumer must reduce intake or buffer within a bounded limit. Track offsets only after the corresponding output is durable.

---

## 5) Parallelism Without Surprises

Parallel work helps when tasks are independent and the bottleneck is parallelizable. It can hurt through serialization, coordination, contention, or data skew.

* Use threads for I/O-bound Python work and processes for CPU-bound work when the runtime permits.
* Limit concurrency to protect source systems.
* Partition work evenly; one oversized partition can determine total runtime.
* Keep tasks reasonably coarse so scheduling overhead is small.
* Preserve deterministic output ordering when consumers require it.

Never trade correctness for throughput. Test retries, duplicate delivery, partial writes, and out-of-order events.

---

## 6) Spark-Specific Tuning

1. Prefer built-in Spark SQL functions over Python UDFs; they allow query optimization and efficient serialization.
2. Read only required columns and filter at the source.
3. Inspect the physical plan with `explain()`.
4. Broadcast only genuinely small lookup tables.
5. Repartition for a known join or output distribution; avoid arbitrary repartitioning.
6. Watch for skew. Salting or splitting hot keys can prevent one task from becoming a straggler.
7. Tune shuffle partitions from measured data size and cluster parallelism, not a universal number.
8. Cache only reused DataFrames and unpersist them when finished.
9. Compact output files and choose a partition count that avoids tiny files.
10. Enable adaptive query execution where supported, then verify the resulting plan.

---

## 7) A Performance Runbook

- [ ] The benchmark uses realistic data volume, distributions, and cache state.
- [ ] Correctness checks compare counts, keys, aggregates, and null behavior.
- [ ] Input pruning and projected columns are visible in the plan.
- [ ] Memory, CPU, shuffle, file count, and cost are recorded.
- [ ] Skew and the slowest task have been investigated.
- [ ] Retries and partial outputs are safe.
- [ ] The change has a rollback and an owner.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
