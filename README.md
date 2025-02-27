# Workflow Zoo

A collection of experimental, AI-generated workflow diagrams visualizing various conceptual processes and patterns using Mermaid.js flowcharts. For the lolz mainly just to see what reasoning agent come up with when asked about producing AI workflows similar to specific fields of research.

## Overview

Workflow Zoo is a web-based visualization tool that presents a collection of workflow diagrams covering various domains including:
- Adaptive Learning Systems
- Swarm Intelligence
- Network Resilience
- Dynamic Task Decomposition
- Information Diffusion
- And many more...

Each workflow is defined using Mermaid.js flowchart syntax in `.mmd` files, making them easy to read, modify, and version control.

## ⚠️ AI-Generated Content Notice

All workflows in this collection are generated using artificial intelligence. While they may be interesting or inspiring, they should not be taken as authoritative or proven patterns. These are experimental, conceptual workflows that may or may not reflect real-world best practices.

## Workflow Generation Process

The workflows were generated by first providing several exemplar workflows to the AI model. Then, the model was tasked with creating new workflows independently, following two key constraints:
1. Each workflow must begin with a user input node
2. Each workflow must end with a final solution node
3. The style and structure must follow the provided exemplars

## Features

- **Interactive Visualization**: All workflows are rendered as interactive flowcharts using Mermaid.js

## Directory Structure

```
workflow-zoo/
├── css/
│   └── styles.css          # Custom styling
├── workflows/              # Mermaid flowchart definitions
│   ├── *.mmd              # Individual workflow files
│   └── ...
└── index.html             # Main viewer application
```

## Usage

1. Clone the repository
2. Open `index.html` in a web browser after starting a local server

## Contributing

Feel free to contribute by:
1. Adding new workflow diagrams (as `.mmd` files in the `workflows` directory)
2. Improving existing workflows
3. Enhancing the viewer functionality

## Technical Details

- Built using vanilla JavaScript and CSS
- Uses Mermaid.js for flowchart rendering
- No build process required - works directly in the browser
- Flowcharts are defined using Mermaid's flowchart syntax in `.mmd` files

## License

This project is open source and available under the MIT License.
