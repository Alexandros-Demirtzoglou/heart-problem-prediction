# Heart Problem Prediction Algorithm

![GitHub last commit](https://img.shields.io/github/last-commit/alexdemirtzoglou/heart-problem-prediction)
![GitHub issues](https://img.shields.io/github/issues/alexdemirtzoglou/heart-problem-prediction)
![GitHub license](https://img.shields.io/github/license/alexdemirtzoglou/heart-problem-prediction)

## 🫀 Project Overview

This project explores the application of the Knowledge Discovery in Databases (KDD) process to predict heart problems based on an individual's habits and health indicators. It's a semester project for the Biomedical Technology class at the University of West Attica. The goal is to develop a model that can predict the likelihood of heart problems by analyzing various factors related to a person's lifestyle and health metrics.

## ✨ Key Features

- Implementation of the KDD process for heart problem prediction
- Data preprocessing and transformation of BRFSS 2015 dataset
- K-means clustering for health indicators visualization
- Decision Tree classification for heart disease prediction

## 🛠️ Technologies Used

- Python
- Scikit-learn library
- Pandas DataFrame
- K-means clustering
- Decision Tree classification

## 📁 Repository Structure

```
.
├── Code/
│   ├── 1. All Data Preprocessing & Transformation.py
│   ├── 2. K-Means Clustering.py
│   └── 3. Data Mining with Classification.py
├── Documentation/
│   ├── BRFSS 2015 Codebook Report.pdf
│   ├── Biomedical Technology Assignment.pdf
│   └── heart_disease_health_indicators_BRFSS2015 (Cleaned Data Spreadsheet).csv
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 KDD Process Application

This project follows the Knowledge Discovery in Databases (KDD) process:

1. **Data Collection**: Utilizing the BRFSS 2015 dataset
2. **Data Preprocessing**: Cleaning and preparing the dataset
3. **Data Transformation**: Applying necessary transformations for analysis
4. **Data Mining**: Implementing K-means clustering and Decision Tree classification
5. **Interpretation/Evaluation**: Analyzing results and drawing conclusions

Each step is implemented and documented in the corresponding Python files and documentation.

## 📊 Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/alexdemirtzoglou/heart-problem-prediction.git
   ```
2. Navigate to the `Code/` directory
3. Run the Python scripts in order:
   ```sh
   python "1. All Data Preprocessing & Transformation.py"
   python "2. K-Means Clustering.py"
   python "3. Data Mining with Classification.py"
   ```
4. Refer to the documentation for detailed analysis and results

## 🤝 Contributing

As this is a university project, it is not open for external contributions. However, feedback and suggestions are welcome for academic purposes.

## 📝 License

This project is not licensed for distribution or use outside of academic evaluation.

## 👤 Author

Alexandros Demirtzoglou
- GitHub: [@alexdemirtzoglou](https://github.com/alexdemirtzoglou)

## 🙏 Acknowledgements

- Athanasios Kiourtis for guidance and support
- Scikit-learn library developers
- Pandas library developers
- BRFSS 2015 dataset creators

## 📚 References

1. Behavioral Risk Factor Surveillance System (BRFSS) 2015 Codebook Report
2. Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
3. McKinney, W., "Data Structures for Statistical Computing in Python," Proceedings of the 9th Python in Science Conference, 2010.
