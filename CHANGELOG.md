# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.2.5](https://github.com/AnthonyDugarte/ULA-VG/compare/v0.2.4...v0.2.5) (2023-04-12)


### Features

* **match-3:** Add drag and drop logic ([994893d](https://github.com/AnthonyDugarte/ULA-VG/commit/994893df4a00c146cc9502c61f7f1bc42ff3e9f0))
* **match-3:** add mouse motion input handlers ([15e9829](https://github.com/AnthonyDugarte/ULA-VG/commit/15e9829247ef6ef27e3913e00b8b8b33aca6a6d2))
* **match-3:** Add mouse movement handling ([585fcfb](https://github.com/AnthonyDugarte/ULA-VG/commit/585fcfb41a6c0b1cdab79a0f14b81d007c9b6a28))
* **match-3:** Add possible matches verification ([59b5f1b](https://github.com/AnthonyDugarte/ULA-VG/commit/59b5f1b980942cabe4055a44fd2d07271a87eacb))
* **match-3:** add virtual position utility from a window specific position ([f615247](https://github.com/AnthonyDugarte/ULA-VG/commit/f615247e0300d748b75a03679efb9c837cf9e95b))
* **match-3:** allow movement only on matches ([ad24994](https://github.com/AnthonyDugarte/ULA-VG/commit/ad24994167e8e5650592e4bf938b6f1b4acc977e))
* **match-3:** init ([33ce5ae](https://github.com/AnthonyDugarte/ULA-VG/commit/33ce5ae2b99b5f0adabba5b7a6f912b67c748734))
* **match-3:** re-generate world if necessary when there are now new possible matches after a movement ([322426a](https://github.com/AnthonyDugarte/ULA-VG/commit/322426aa6c62fa633309d55e1fbb8e154ef56ea1))
* **match-3:** render dragged title at last so it shows up on top ([c14283a](https://github.com/AnthonyDugarte/ULA-VG/commit/c14283aa00485654fb8554c0af922fbcead3dc0d))
* **match-3:** render hihgligh on the tile behind the dragged tile ([1308c6c](https://github.com/AnthonyDugarte/ULA-VG/commit/1308c6ca281816a6140db3991c980f26b6bf7bb2))
* **match-e:** add tile default pos getter ([91caf80](https://github.com/AnthonyDugarte/ULA-VG/commit/91caf80676545a9d91927403d8c639de1739c705))


### Bug Fixes

* **match-3:** Fix range issue on tiles ([5d99e7f](https://github.com/AnthonyDugarte/ULA-VG/commit/5d99e7f672170b6ce60bd09b17f59aa7f31cb374))
* **match-3:** when initiallizing tales, verify there are possible matches, if not, initialize again ([9526422](https://github.com/AnthonyDugarte/ULA-VG/commit/952642242d037c2a54ae4281d94688bd1c550992))

### [0.2.4](https://github.com/AnthonyDugarte/ULA-VG/compare/v0.2.3...v0.2.4) (2023-02-26)


### Bug Fixes

* **flappy_bird:** improve x-axis movement logic by storing which side is being pressed and computate the speed taking preference for right side movement ([ea93333](https://github.com/AnthonyDugarte/ULA-VG/commit/ea933333875e2c24c788762a57427a7650843a32))

### [0.2.3](https://github.com/AnthonyDugarte/ULA-VG/compare/v0.2.1...v0.2.3) (2023-02-19)


### Features

* **breakout:** Add ball assign rand velocity to center where this logic is placed ([402550e](https://github.com/AnthonyDugarte/ULA-VG/commit/402550ea6474949b179cefbcc7010622fc1ed47b))
* **breakout:** Add fire input handling to sticky balls powerup ([27e1cb4](https://github.com/AnthonyDugarte/ULA-VG/commit/27e1cb4d2be42815764717e6068b23819c2c55c9))
* **breakout:** Add formatting + linting packages ([7ea1588](https://github.com/AnthonyDugarte/ULA-VG/commit/7ea15887625c903393d46d8904ecca72728ac53d))
* **breakout:** Add inpout handling to powerups ([1fec702](https://github.com/AnthonyDugarte/ULA-VG/commit/1fec702c4dae7b4f03e9c9fe44ec106d4fe3d529))
* **breakout:** Add play_state to PowerUp update method ([a6b8e76](https://github.com/AnthonyDugarte/ULA-VG/commit/a6b8e760ca408ad172ad2e142d74614f14eca5a3))
* **breakout:** Add sticked to paddle + paddled in update checks to Ball ([6a42886](https://github.com/AnthonyDugarte/ULA-VG/commit/6a42886e802974a5f5c84e691de7d21d4daaa8fc))
* **breakout:** Add sticky balls powerup ([63b5d7b](https://github.com/AnthonyDugarte/ULA-VG/commit/63b5d7bb67787f3d897eff59904dba1517735ea3))
* **breakout:** Add sticky balls powerup creation on playstate ([6e1c5da](https://github.com/AnthonyDugarte/ULA-VG/commit/6e1c5dab18ad16e7ac20e49ad50508df5e3a9169))
* **breakout:** cannons wip ([cc35b9c](https://github.com/AnthonyDugarte/ULA-VG/commit/cc35b9c48b332052288dc092c9161fe0f05c54c5))
* **breakout:** Init ([4ed8192](https://github.com/AnthonyDugarte/ULA-VG/commit/4ed8192440553e1c78ba3693ec92775a4b663336))
* **breakout:** remap pause key to p, and use space as fire input ([bd42f4f](https://github.com/AnthonyDugarte/ULA-VG/commit/bd42f4f1f753cf711a169b2d3d95ebd318f25bcf))
* **breakout:** Store paddle dx from update ([066a124](https://github.com/AnthonyDugarte/ULA-VG/commit/066a124bd70bd68471b87581e14a9f6ac9e02935))
* **flappy_bird:** Add .gitignore ([593b603](https://github.com/AnthonyDugarte/ULA-VG/commit/593b603d8d3061552ba9f32d91262e9bf1dc4f3d))
* **flappy_bird:** Add current game mode to state machine ([b509ca9](https://github.com/AnthonyDugarte/ULA-VG/commit/b509ca90577fed6f960af2beb2f085e2ab311589))
* **flappy_bird:** Add game modes build config ([231b93c](https://github.com/AnthonyDugarte/ULA-VG/commit/231b93c415d9d5fddec37cb237977da7c9204808))
* **flappy_bird:** Add hard game mode for x-axis movement of bird ([eee4edd](https://github.com/AnthonyDugarte/ULA-VG/commit/eee4eddc8df4bc372ae454691b8c989d45debc75))
* **flappy_bird:** Add interface to bird class in order to move it in the x-axis ([64a06cc](https://github.com/AnthonyDugarte/ULA-VG/commit/64a06cc7be9b29074bbb2f60018522ff6102e68a))
* **flappy_bird:** Add normal game mod for x-axis movement of bird ([8f6be3a](https://github.com/AnthonyDugarte/ULA-VG/commit/8f6be3aa7728c7a321ce8ea771887faa2fb8382b))
* **flappy_bird:** Add Pause state make config ([13b1519](https://github.com/AnthonyDugarte/ULA-VG/commit/13b151915d04096c9296192be1b55f06ad3fd6df))
* **flappy_bird:** Add pause state to state machine ([7052b08](https://github.com/AnthonyDugarte/ULA-VG/commit/7052b08fbecb9f146a7c760d4f479dff3081d1ec))
* **flappy_bird:** Add simple pause state binded to the P keyboard key ([ab2e694](https://github.com/AnthonyDugarte/ULA-VG/commit/ab2e694f2c15eb4cba8a099c1ba763637fa26b23))
* **flappy_bird:** Add space as a jump handler ([b035bfb](https://github.com/AnthonyDugarte/ULA-VG/commit/b035bfbe7ee0cd9e11da40e8d0eb6b3c0027b061))
* **flappy_bird:** Allow game to handle keyrelease inputs to simplify bird handling of x-axis movement stop condition ([64a0cd5](https://github.com/AnthonyDugarte/ULA-VG/commit/64a0cd56344a8dd85536abc635a2d73992c54386))
* **flappy_bird:** Delegate bird input handling to game mode when playing ([c61fc3c](https://github.com/AnthonyDugarte/ULA-VG/commit/c61fc3c172ce365418c07af9d3157c38cf9ff368))
* **flappy_bird:** init ([f843aee](https://github.com/AnthonyDugarte/ULA-VG/commit/f843aee5c9138135dd9483272ddbd259c150b7fa))
* **flappy_bird:** Restore score from world when going back to playing status, after pausing the game ([9e451b3](https://github.com/AnthonyDugarte/ULA-VG/commit/9e451b3bc26414318cafe9078e96807a747a6afa))
* **flappy_bird:** while on playing state, handle P keyboard keypress and transition to the pause state ([b4e3b6a](https://github.com/AnthonyDugarte/ULA-VG/commit/b4e3b6afd2aec248f02219ca05b6aa3f61cf367b))


### Bug Fixes

* **flappy_bird:** Add sfml lib + include headers ([8b6dcbd](https://github.com/AnthonyDugarte/ULA-VG/commit/8b6dcbdce91ac79837f4408064546fe00fd600db))
* **flappy_bird:** Change state cleanup bug ([d69ee9b](https://github.com/AnthonyDugarte/ULA-VG/commit/d69ee9b6b7e60446def2888f4c8ddc3dfb0c6a0a))

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
