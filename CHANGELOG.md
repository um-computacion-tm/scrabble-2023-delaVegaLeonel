# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.6] - 2023-08-29

###  Changed

- Added new attribute to the class "Scrabble" named "gameid". The "gameid" is a id with the objetive to, in the future, view past game for very motives you want
- Finally added the joker tile, but still is not work how is intendeed because still don't program the interface.

## [0.0.5] - 2023-08-28

###  Changed

- The method "get_tiles" now work differently because is only one bag for game and not for player
- The method "exchange_tiles" now work differently because is only one bag for game and not for player. Besides now the player select the tile they wanted and receive one tile random

## [0.0.4] - 2023-08-28

###  Changed

- The method "initial_tiles" of the class "Player" now is in the class "BagTiles" this is because in the game only is one bag and not every player have one bag

### Removed

- The attribute "name" of the class "Player" is remove because is unnecessary
 
## [0.0.3] - 2023-08-27

### Added

- Added new 2 methods for "player" and yours tests
- The new 2 methods are: "get_tiles" and "exchange_tiles". In the class "get_tiles" the player recive random tiles for you bag and "exchange_tiles" eliminate the oldest tile of the bag of the player a recive a new random tile

## [0.0.2] - 2023-08-27

### Added

- Added new methods, attribute and tests a the class "player".
- The new optional attribute is "name" and is self explanatory
- The 2 methods are: "change_name" and "initial_tiles". The method "change_name" is self explanatory and "initial_tiles" this is going to send to the player all 98 tiles (for now not exist the joker tile) to be able to begin of the game

## [0.0.1] - 2023-08-27

### Added

- For now is grouped in two module: "Game" and "Tests"
- Definition of the class "Tile" and your tests
- Definition of the class "BagTiles" and your tests
- BagTiles have 2 metods: "take" and "put". Take will retire tiles in the bag and put will input tiles in the bag
- Definition of the class "Player" and your tests
- Player have 2 attributes for now: name and tiles. "Name" is the identificator of the player and "tiles" is the amount of tiles for the player
- Player have 1 method: "initial_tiles". This is going to send all of the 98 initial tiles for the beginnig of the game
- Definition of the class "board" and yours tests
- Definition of the class "cell" and yours tests
- Definition of the class "scrabble" and yours tests
- "cell" have 2 methods: "add_letter" and "calculate_value". "add_letter" is self explaining and "calculate_value" is the calculation of the value and the multiplication of the cell.