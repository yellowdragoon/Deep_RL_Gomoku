# Deep Reinforcement Learning for Gomoku

This project implements a deep reinforcement learning algorithm inspired by AlphaZero to play the game of Gomoku.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Gomoku, also known as Five in a Row, is a strategy board game. This project uses deep reinforcement learning techniques to train an AI agent to play Gomoku at a high level, similar to the AlphaZero algorithm developed by DeepMind.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To start training the model, run:
```bash
python train.py
```

To play against the trained model, run:
```bash
python play.py
```

## Training
The training process involves self-play, where the model plays against itself to improve its performance. The training script saves the model checkpoints and logs the training progress.

## Evaluation
To evaluate the performance of the trained model, you can run evaluation scripts that pit the model against predefined strategies or other AI agents.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
