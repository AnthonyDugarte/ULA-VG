#include "src/game_modes/GameNormalMode.hpp"

void GameNormalMode::handle_bird_inputs(const sf::Event &event,
                                        std::shared_ptr<Bird> bird) noexcept
{
    if (event.type == sf::Event::MouseButtonPressed &&
            event.mouseButton.button == sf::Mouse::Left
        // Add space as a jump alias
        || event.type == sf::Event::KeyPressed &&
               event.key.code == sf::Keyboard::Space)
    {
        bird->jump();
    }
}
