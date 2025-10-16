from setuptools import setup, find_packages
#python setup.py install

setup(
    name='Ride Pricing Precision - Dynamic Pricing with Machine Learning',
    version='1.0.0',
    description='This project implements a dynamic pricing model for ride-sharing services, leveraging machine learning algorithms to optimize pricing strategies in real-time. The model aims to maximize revenue, enhance customer satisfaction, improve operational efficiency, and maintain competitiveness in the market.',
    author='Shivani Gattigorla',
    author_email='shivanigattigorla2001@email.com',
    packages=find_packages(),
    install_requires=[
        'joblib==1.1.0',
        'matplotlib==3.4.3',
        'numpy==1.21.2',
        'pandas==1.3.3',
        'plotly==5.3.1',
        'scikit-learn==0.24.2',
        'scipy==1.7.1',
        'seaborn==0.11.2',
        'streamlit==0.89.0',
    ],
)
