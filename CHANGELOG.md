# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.2.2](https://github.com/AnthonyDugarte/ULA-VG/compare/v0.2.1...v0.2.2) (2023-02-17)

### Features

- **flappy_bird:** Allow game to handle keyrelease inputs to simplify bird handling of x-axis movement stop condition ([64a0cd5](https://github.com/AnthonyDugarte/ULA-VG/commit/64a0cd56344a8dd85536abc635a2d73992c54386))
- **flappy_bird:** Delegate bird input handling to game mode when playing ([c61fc3c](https://github.com/AnthonyDugarte/ULA-VG/commit/c61fc3c172ce365418c07af9d3157c38cf9ff368))
- **flappy_bird:** Add interface to bird class in order to move it in the x-axis ([64a06cc](https://github.com/AnthonyDugarte/ULA-VG/commit/64a06cc7be9b29074bbb2f60018522ff6102e68a))
- **flappy_bird:** Add current game mode to state machine ([b509ca9](https://github.com/AnthonyDugarte/ULA-VG/commit/b509ca90577fed6f960af2beb2f085e2ab311589))
- **flappy_bird:** Add game modes build config ([231b93c](https://github.com/AnthonyDugarte/ULA-VG/commit/231b93c415d9d5fddec37cb237977da7c9204808))
- **flappy_bird:** Add hard game mode for x-axis movement of bird ([eee4edd](https://github.com/AnthonyDugarte/ULA-VG/commit/eee4eddc8df4bc372ae454691b8c989d45debc75))
- **flappy_bird:** Add normal game mod for x-axis movement of bird ([8f6be3a](https://github.com/AnthonyDugarte/ULA-VG/commit/8f6be3aa7728c7a321ce8ea771887faa2fb8382b))
- **flappy_bird:** Restore score from world when going back to playing status, after pausing the game ([9e451b3](https://github.com/AnthonyDugarte/ULA-VG/commit/9e451b3bc26414318cafe9078e96807a747a6afa))
- **flappy_bird:** Add Pause state make config ([13b1519](https://github.com/AnthonyDugarte/ULA-VG/commit/13b151915d04096c9296192be1b55f06ad3fd6df))
- **flappy_bird:** Add pause state to state machine ([7052b08](https://github.com/AnthonyDugarte/ULA-VG/commit/7052b08fbecb9f146a7c760d4f479dff3081d1ec))
- **flappy_bird:** while on playing state, handle P keyboard keypress and transition to the pause state ([b4e3b6a](https://github.com/AnthonyDugarte/ULA-VG/commit/b4e3b6afd2aec248f02219ca05b6aa3f61cf367b))
- **flappy_bird:** Add simple pause state binded to the P keyboard key ([ab2e694](https://github.com/AnthonyDugarte/ULA-VG/commit/ab2e694f2c15eb4cba8a099c1ba763637fa26b23))
- **flappy_bird:** Add space as a jump handler ([b035bfb](https://github.com/AnthonyDugarte/ULA-VG/commit/b035bfbe7ee0cd9e11da40e8d0eb6b3c0027b061))
- **flappy_bird:** Add .gitignore ([593b603](https://github.com/AnthonyDugarte/ULA-VG/commit/593b603d8d3061552ba9f32d91262e9bf1dc4f3d))
- **flappy_bird:** init ([f843aee](https://github.com/AnthonyDugarte/ULA-VG/commit/f843aee5c9138135dd9483272ddbd259c150b7fa))

### Bug Fixes

- **flappy_bird:** Change state cleanup bug ([d69ee9b](https://github.com/AnthonyDugarte/ULA-VG/commit/d69ee9b6b7e60446def2888f4c8ddc3dfb0c6a0a))
- **flappy_bird:** Add sfml lib + include headers ([8b6dcbd](https://github.com/AnthonyDugarte/ULA-VG/commit/8b6dcbdce91ac79837f4408064546fe00fd600db))

### 0.2.1 (2023-01-29)

### Features

- **pong:** Connect the AI controlled paddles to the update_pong method ([d88938f](https://github.com/AnthonyDugarte/ULA-VG/commit/d88938f310acb75df4eb7e601729fbb90a16ee9e))
- **pong:** Add AI controlled paddle update logic ([d1debd2](https://github.com/AnthonyDugarte/ULA-VG/commit/d1debd236a6578d7c4ad7f561a18e1685f14f935))
- **pong:** remove up/down keymaps for AI controlled paddles ([058f083](https://github.com/AnthonyDugarte/ULA-VG/commit/058f08362677ebdb8753edf9cce6f4a409adf751))
- **pong:** add is_ai_driven flag to paddles ([a48c236](https://github.com/AnthonyDugarte/ULA-VG/commit/a48c23696d3e951cfe96e5b5eb8f7b3b6fae0849))
- **pong:** init ([ac4113e](https://github.com/AnthonyDugarte/ULA-VG/commit/ac4113ec131ef5cf4543634f137d08fe39308790))
- init conventional commits ([2546973](https://github.com/AnthonyDugarte/ULA-VG/commit/2546973845a8212b4cb1c7abaf6eff03058d024b))

### Bug Fixes

- **pong:** Improve render_pong performance ([09d2db6](https://github.com/AnthonyDugarte/ULA-VG/commit/09d2db6cc312beeff7606a82d7b96f17e29b3b99))
- **pong:** reduce paddle speed to 100 ([9fa957c](https://github.com/AnthonyDugarte/ULA-VG/commit/9fa957c4c4cfe873a45756248a98cb87286b9887))
