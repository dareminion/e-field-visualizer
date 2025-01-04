# Electric Field Visualizer

## Contributors

* Ibrahim Mira
* John Fanourakis
* Darren Kuo

## Basic Description of Program

This a relatively simple Python Based program that utilizes MatPlotLib to generate graphs that depict a simple electic point charge's electric field. The repository contains three primary folders,`tests`, `docs`, and `src`. Below are simple descriptions of each.

### Docs

An attempt at using Sphinx as a documentation tool to document all the various files contained within this repository. Due to lack of knowledge on Sphnix between the team members and a deadline that was closing in, this was our third and best attempt at creating something resembling actual documentation.

### Tests

This project was completed through an attempt at Test Driven Development (TDD). This involved writing many various test cases for different portions of the project. Using [`test_fields.py`](https://github.com/dareminion/e-field-visualizer/blob/main/tests/test_fields.py) as an example, there are nine test cases present. Each test is clearly defined as the function definition and test various aspects of the `Fields` Class of this program. This class is designed as a wrapper around *NumPy* arrays and tests both scalar and vector field implementations.

All these various tests help contribute to our design process as these tests would involve us writing a test for an expected output, then write the actual code until the tests pass and then refine the code. Oftentimes our tests would have errors among themselves, but we would not have discovered solutions to these problems if not for following a TDD structure.

### Source Files

The `src` folder contains all the various python files that make up this program. Split into various subsections:

* `Domain` - 'Playing Field' upon with the electrostatic sources exist
* `Factories` - How the electrostatic sources are generated
* `Math` - Wrapper code for *NumPy* which allows for calculations to be performed 
* `Physics` - Outline for how a Electrostatic Source would be created
* `Visuals` - How a plot can be generated through MatPlotLib

These subsections were arrived upon through refining UML diagrams between the team and our professor that provided significant guidance throughout the project. This layout meant that this would be expandable in the future without having to rework a significant amount of the original code.

Contained alongside these folder are two demo files that provide a demo on two slightly different point charges. These demo files contain comments alongside each line of code that explains the function of each line. The entire process goes through the various aspects of the project and this results in a final plot that can be shown.