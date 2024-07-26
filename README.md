# Semantic Image and Text Alignment: Automated Storyboard Synthesis for Digital Advertising

## Table of Contents
- [Introduction](#introduction)
- [Business Objective](#business-objective)
- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Methodology](#methodology)
- [Results](#results)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction
This project focuses on leveraging recent advancements in machine learning, natural language processing, and computer vision, alongside the development of Large Language Models (LLMs), to transform textual descriptions of advertisement concepts and assets into detailed storyboards. This process aims to visually depict the narrative flow and user interaction within advertisements, making the conceptualization of digital campaigns both more intuitive and impactful.

## Business Objective
Adludio specializes in creating interactive ads that resonate with viewers through dynamic content such as mini-games, videos, texts, and images. To streamline and enhance the ad creation process, Adludio aims to automate the end-to-end process of advertising production. This automation will expedite the ideation and execution phases, enabling clients to swiftly launch their campaigns with minimal expenditure of time and resources. A key component of this automation involves generating potential creative concepts based on the client's brief, significantly reducing the traditional turnaround time from over a week to mere days.

## Project Overview
This project is divided into four key tasks:
1. **EDA & Workflow Strategy**: Exploring and understanding the provided data, and preparing the environment for asset analysis.
2. **Critic/Grading Agent Asset Analysis and Automatic Asset Editing with AutoGen**: Analyzing and manipulating creative assets using AutoGen agents, and providing feedback for the image composition process.
3. **Image Composition Agent**: Organizing and composing assets into advertisement frames that are aesthetically pleasing and effectively convey the intended message.
4. **Building the Storyboard**: Synthesizing individual frames into a single storyboard image that represents the user flow through the advertisement.

## Data Description
The dataset used in this project includes:
- **Images**: A collection of advertisement images with associated metadata.
- **Text**: Descriptions and concepts related to the advertisement images.
- **JSON Files**: Detailed breakdowns of advertisement concepts, including visual representations and explanations for each segment.

## Methodology
1. **Exploratory Data Analysis (EDA)**
   - Analysis of the dataset to understand the distribution and characteristics of the data.
   - Identification of key features for aligning images and text.

2. **Feature Engineering**
   - Extraction of relevant features from both images and text.
   - Transformation and normalization of features for model training.

3. **Model Training**
   - Training machine learning models to align images with corresponding textual descriptions.
   - Fine-tuning the models for optimal performance.

4. **Storyboard Generation**
   - Using the trained models to generate detailed storyboards from textual descriptions.
   - Ensuring the generated storyboards are coherent and align with the intended advertisement concepts.

5. **Evaluation**
   - Assessing the quality and accuracy of the generated storyboards.
   - Making necessary adjustments to improve the results.

## Results
The project successfully demonstrated the ability to synthesize automated storyboards by semantically aligning images and text. The generated storyboards were evaluated for their coherence and relevance to the advertisement concepts, leading to valuable insights and improvements in the digital advertising process.

## Usage
To use this project, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/MoraaOntita/Semantic-Image-and-Text-Alignment.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```   
3. Run the main script to generate storyboards

## Contributions
Contributions are welcome! If you have any improvements or new features to add, feel free to open a pull request or create an issue.

Happy Coding!
