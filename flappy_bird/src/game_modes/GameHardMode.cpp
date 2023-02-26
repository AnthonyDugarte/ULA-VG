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
            bird->toggle_move_l(true);
        }
        else if (event.key.code == sf::Keyboard::D)
        {
            bird->toggle_move_r(true);
        }
    }

    if (event.type == sf::Event::KeyReleased)
    {
        if (event.key.code == sf::Keyboard::A)
        {
            bird->toggle_move_l(false);
        }

        if (event.key.code == sf::Keyboard::D)
        {
            bird->toggle_move_r(false);
        }
    }
}
