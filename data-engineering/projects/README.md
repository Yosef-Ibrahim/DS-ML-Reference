# Data Engineering Projects

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

This suite turns the concepts in the surrounding Data Engineering notes into
three small, reproducible projects. Every example is safe to run locally:
there are no embedded credentials, paid services, network calls, or required
cloud accounts.

## Projects

| Project | Main ideas | Starting point |
|---|---|---|
| [01-ecommerce-batch-etl](./01-ecommerce-batch-etl/) | Idempotent batch ingestion, validation, dimensional analytics | [README](./01-ecommerce-batch-etl/README.md) |
| [02-realtime-fraud-detection](./02-realtime-fraud-detection/) | Event streams, watermarks, feature windows, Spark Structured Streaming | [README](./02-realtime-fraud-detection/README.md) |
| [03-cloud-lakehouse-medallion](./03-cloud-lakehouse-medallion/) | Bronze/silver/gold layers, orchestration, cloud-ready paths | [README](./03-cloud-lakehouse-medallion/README.md) |

## Suggested study order

1. Complete the batch ETL project with Python and SQL.
2. Read the streaming design, then run the credential-free producer. Add
   PySpark only when you are ready to use a Spark runtime.
3. Use the medallion project to compare local files with object-storage
   prefixes and Airflow task dependencies.

Each project README includes prerequisites, a learning checklist, an
architecture diagram, commands, expected outputs, and production extensions.
The Python scripts are also useful as readable reference implementations.

## Contributing

Keep examples deterministic, local-first, and free of secrets. Explain any
optional service or dependency in the relevant project README and preserve the
same public interfaces when extending an example.

📬 **Contributing:** Questions and improvements are welcome via
[GitHub](https://github.com/Yosef-Ibrahim).
