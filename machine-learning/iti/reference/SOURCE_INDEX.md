# Source index and mapping

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## Preserved root materials

| Original file | Normalized location | Use |
|---|---|---|
| `Topics.pdf` | `source-materials/Topics.pdf` | Curriculum outline |
| `Project General Steps.pdf` | `source-materials/Project General Steps.pdf` | Project workflow |
| `Overfitting.pdf` | `source-materials/Overfitting.pdf` | Bias, variance, and regularization |
| `Lec2 Linear regression with one variable.pptx` | `source-materials/…` | One-variable regression |
| `Lec3 linear regression with multiple vars.pptx` | `source-materials/…` | Multiple regression |
| `Lec4 logistic regression.pptx` | `source-materials/…` | Logistic classification |
| `Confution Matrix.pptx` | `source-materials/…` | Confusion-matrix measures (original spelling retained) |
| `Codes/**/*.doc` | The matching normalized topic directory | Lesson notes |
| `Codes/SkLearn_Codes.rar` | `source-materials/SkLearn_Codes.rar` | Original archive |


## Code mapping

| Original code directory | Normalized directory |
|---|---|
| `1.1 Data` | `foundations/data-loading` |
| `1.2 Data Cleaning` | `foundations/preprocessing/data-cleaning` |
| `1.3 Metrics Module` | `evaluation/metrics` |
| `1.4_Feature_Selection` | `foundations/preprocessing/feature-selection` |
| `1.5_Data_Scaling` | `foundations/preprocessing/scaling` |
| `1.6_Data_Split` | `foundations/preprocessing/splitting` |
| `2.1_Linear_Regression` | `supervised/linear-regression` |
| `2.2_Logistic_Regression` | `supervised/logistic-regression` |
| `2.3_NN` | `supervised/neural-networks` |
| `3.1_Model_Check` | `evaluation/model-check` |
| `3.2_Grid_Search` | `evaluation/grid-search` |
| `3.3_Pipeline` | `evaluation/pipelines` |
| `3.4_Model_Save` | `evaluation/model-persistence` |

The five useful CSV files are copied unchanged to `data/raw/`: `houses.csv`,
`satf.csv`, `heart.csv`, `Dataset_spine.csv`, and `train.csv`. The `examples/`
directory contains corrected runnable companions; the copied numbered snippets
remain available for comparison and provenance.

## How to navigate the archive

Start with `source-materials/Topics.pdf` for the original high-level sequence, then
read the normalized guide for the stage you are studying. Use the matching numbered
directory when you want to compare a teaching fragment with its surrounding notes.
The runnable Python files under `examples/python/` are the preferred executable
reference because they define imports, data, splits, and outputs explicitly. The
notebooks under `examples/notebooks/` provide the same ideas with inspection cells.

| Learning question | Guide to read first | Preserved source |
|---|---|---|
| How should a table be inspected? | `foundations/data-loading/guide.md` | `1.1 Data` |
| How can preprocessing leak? | `foundations/preprocessing/README.md` | `1.2`, `1.4`–`1.6` |
| Which model fits a numeric target? | `supervised/linear-regression/guide.md` | `2.1_Linear_Regression`, Lec2/Lec3 |
| How do thresholds and errors work? | `supervised/logistic-regression/guide.md` | `2.2_Logistic_Regression`, Lec4, `Confution Matrix.pptx` |
| How do I compare and save models? | `evaluation/model-selection/guide.md` | `3.1`, `3.2`, `3.3`, `3.4` |

## Provenance and correction policy

Names and original spellings are retained so a citation can find the source bytes.
The normalized documents are explanatory additions, not replacements for those
copies. ⚠️ Treat undefined variables, obsolete estimator arguments, test-as-
validation examples, and scorer sign conventions as teaching issues called out by
the guides. Do not edit the preserved PDFs, PPTX, DOC, RAR, source code, or copied
CSV files to make a correction; update a guide or a runnable companion instead.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
