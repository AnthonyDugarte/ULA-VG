#include "src/game_modes/GameHardMode.hpp"
#include "Settings.hpp"
#include "src/game_modes/GameNormalMode.hpp"

void GameHardMode::handle_bird_inputs(const sf::Event &event,
                                      std::shared_ptr<Bird> bird) noexcept
{
    GameNormalMode::handle_bird_inputs(event, bird);

    if (event.type == sf::Event::KeyPressed)
    {
        if (event.key.code == sf::Keyboard::A)
        {
            bird->move_x(-Settings::JUMP_TAKEOFF_SPEED);
        }
        else if (event.key.code == sf::Keyboard::D)
        {
            bird->move_x(Settings::JUMP_TAKEOFF_SPEED);
        }
    }

    if (event.type == sf::Event::KeyReleased &&
        (event.key.code == sf::Keyboard::A ||
         event.key.code == sf::Keyboard::D))
    {
        bird->move_x(0);
    }
}
