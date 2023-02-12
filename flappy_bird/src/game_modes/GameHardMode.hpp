/*
    ISPPJ1 2023
    Study Case: Flappy Bird

    Author: Alejandro Mujica
    alejandro.j.mujic4@gmail.com

    This file contains the declaration of the class GameHardMode.
*/

#pragma once

#include "src/game_modes/GameNormalMode.hpp"
#include <SFML/Graphics.hpp>
#include <Settings.hpp>
#include <memory>

class GameHardMode : public GameNormalMode
{
  public:
    GameHardMode() : GameNormalMode{} {};

    void handle_bird_inputs(const sf::Event &event,
                            std::shared_ptr<Bird> bird) noexcept override;

  protected:
};
