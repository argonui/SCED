function onLoad()
  spawnButton("symbols", "Change Tooltips",
  "Changes tooltip for 'draw chaos token' buttons.", 0, 0.5, 0, 600, 400, 70)
end

function spawnButton( func, text, tool_tip, xPosition, yPosition, zPosition, button_width, button_height, fontsize )
  scale = self.getScale()
  scale = scale[1]
  params = {
    click_function = func,
    function_owner = self,
    label = text,
    position = {scale * xPosition, yPosition, scale * zPosition},
    rotation = {0, 0, 0},
    width = button_width * scale,
    height = button_height * scale,
    font_size = fontsize * scale,
    color = {1, 1, 1},
    font_color = {0, 0, 0},
    tooltip = tool_tip
  }
  self.createButton(params)
end

function symbols()
  local tool = "no scenario selected"
  for _, scenario in ipairs(getObjectFromGUID("fe2ae4").getObjects()) do
    if scenario.getDescription() == "The Gathering" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull] -2. If you fail, after this skill test, search the encounter deck and discard pile for a [[Ghoul]] enemy, and draw it. Shuffle the encounter deck.\n\n[cultist] Reveal another token. If you fail, take 2 horror.\n\n[tablet] -4. If there is a [[Ghoul]] enemy at your location, take 1 damage and 1 horror."
      else
        tool = "Easy / Standard\n\n[skull] -X. X is the number of [[Ghoul]] enemies at your location.\n\n[cultist] -1. If you fail, take 1 horror.\n\n[tablet] -2. If there is a [[Ghoul]] enemy at your location, take 1 damage.\n\n"
      end
    end
    -- midnight masks
    if scenario.getDescription() == "The Midnight Masks" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the total number of doom in play.\n\n[cultist]: -2. Place 1 doom on each [[Cultist]] enemy in play. If there are no [[Cultist]] enemies in play, reveal another token.\n\n[tablet]: -4. If you fail, place all your clues on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the highest number of doom on a [[Cultist]] enemy in play.\n\n[cultist]: -2. Place 1 doom on the nearest [[Cultist]] enemy.\n\n[tablet]: -3. If you fail, place 1 of your clues on your location."
      end
    end
    -- devourer below
    if scenario.getDescription() == "The Devourer Below" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -3. If you fail, after this skill test, search the encounter deck and discard pile for a [[Monster]] enemy, and draw it. Shuffle the encounter deck.\n\n[cultist]: -4. Place 2 doom on the nearest enemy.\n\n[tablet]: -5. If there is a [[Monster]] enemy at your location, take 1 damage and 1 horror.\n\n[elder_thing]: -7. If there is an [[Ancient One]] enemy in play, reveal another token."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of [[Monster]] enemies in play.\n\n[cultist]: -2. Place 1 doom on the nearest enemy.\n\n[tablet]: -3. If there is a [[Monster]] enemy at your location, take 1 damage.\n\n[elder_thing]: -5. If there is an [[Ancient One]] enemy in play, reveal another token."
      end
    end
    -- extracurricular activity symbols
    if scenario.getDescription() == "Extracurricular Activity" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2. If you fail, discard the top 5 cards of your deck.\n\n[cultist]: -1 (-5 instead if there are 10 or more cards in your discard pile).\n\n[elder_thing]: -X. Discard the top 3 cards of your deck. X is the total printed cost of those discarded cards."
      else
        tool = "Easy / Standard\n\n[skull]: -1. If you fail, discard the top 3 cards of your deck.\n\n[cultist]: -1 (-3 instead if there are 10 or more cards in your discard pile).\n\n[elder_thing]: -X. Discard the top 2 cards of your deck. X is the total printed cost of those discarded cards."
      end
    end
    -- The house always wins symbols
    if scenario.getDescription() == "The House Always Wins" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -3. You may spend 3 resources to treat this token as a 0, instead.\n\n[cultist]: -3. If you fail, discard 3 resources.\n\n[tablet]: -2. Discard 3 resources."
      else
        tool = "Easy / Standard\n\n[skull]: -2. You may spend 2 resources to treat this token as a 0, instead.\n\n[cultist]: -3. If you succeed, gain 3 resources.\n\n[tablet]: -2. If you fail, discard 3 resources."
      end
    end
    -- Miskatonic museum symbols
    if scenario.getDescription() == "The Miskatonic Museum" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if Hunting Horror is at your location.)\n\n[cultist]: -3. If you fail, search the encounter deck, discard pile, and the void for Hunting Horror and spawn it at your location, if able.\n\n[tablet]: -4. If Hunting Horror is at your location, it immediately attacks you.\n\n[elder_thing]: -5. If you fail, discard an asset you control."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if Hunting Horror is at your location.)\n\n[cultist]: -1. If you fail, search the encounter deck, discard pile, and the void for Hunting Horror and spawn it at your location, if able.\n\n[tablet]: -2. Return 1 of your clues to your current location.\n\n[elder_thing]: -3. If you fail, discard an asset you control."
      end
    end
    -- essex county express symbols
    if scenario.getDescription() == "The Essex County Express" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 more than the current Agenda #. \n\n[cultist]: Reveal another token. If you fail and it is your turn, lose all remaining actions and end your turn immediately.\n\n[tablet]: -4. Add 1 doom token to each Cultist enemy in play.\n\n[elder_thing]: -3. If you fail, choose and discard a card from your hand for each point you failed by."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the current Agenda #.\n\n[cultist]: -1. If you fail and it is your turn, lose all remaining actions and end your turn immediately.\n\n[tablet]: -2. Add 1 doom token to the nearest Cultist enemy.\n\n[elder_thing]: -3. If you fail, choose and discard a card from your hand."
      end
    end
    --blood on the Altar
    if scenario.getDescription() == "Blood on the Altar" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -1 for each location in play with no encounter card underneath it.\n\n[cultist]: -4. If you fail, add 1 clue from the token pool to your location.\n\n[tablet]: -3. Reveal another token.\n\n[elder_thing]: -3. Place 1 doom on the current agenda."
      else
        tool = "Easy / Standard\n\n[skull]: -1 for each location in play with no encounter card underneath it (max -4).\n\n[cultist]: -2. If you fail, add 1 clue from the token pool to your location.\n\n[tablet]: -2. If you are in the Hidden Chamber, reveal another token.\n\n[elder_thing]: -3. If you fail, place 1 doom on the current agenda."
      end
    end
    --undimensioned and unseen
    if scenario.getDescription() == "Undimensioned and Unseen" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 for each Brood of Yog-Sothoth in play.\n\n[cultist]: Reveal another token. If you fail this test, take 1 horror and 1 damage.\n\n[tablet]: 0. You must either remove all clue tokens from a Brood of Yog-Sothoth in play, or this test automatically fails.\n\n[elder_thing]: -5. If this token is revealed during an attack or evasion attempt against a Brood of Yog-Sothoth, it immediately attacks you."
      else
        tool = "Easy / Standard\n\n[skull]: -1 for each Brood of Yog-Sothoth in play.\n\n[cultist]: Reveal another token. If you fail this test, take 1 horror.\n\n[tablet]: 0. You must either remove all clue tokens from a Brood of Yog-Sothoth in play, or this token's modifier is -4 instead.\n\n[elder_thing]: -3. If this token is revealed during an attack or evasion attempt against a Brood of Yog-Sothoth, it immediately attacks you."
      end
    end
    -- where doom Awaits
    if scenario.getDescription() == "Where Doom Awaits" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-5 instead if you are at an [[Altered]] location).\n\n[cultist]: Reveal another token. Cancel the effects and icons of each skill card committed to this test.\n\n[tablet]: -3. If it is Agenda 2, you automatically fail instead.\n\n[elder_thing]: -X. Discard the top 3 cards of your deck. X is the total printed cost of those discarded cards."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are at an [[Altered]] location).\n\n[cultist]: Reveal another token. Cancel the effects and icons of each skill card committed to this test.\n\n[tablet]: -2 (-4 instead if it is Agenda 2).\n\n[elder_thing]: -X. Discard the top 2 cards of your deck. X is the total printed cost of those discarded cards."
      end
    end
    --lost in time and space
    if scenario.getDescription() == "Lost in Time and Space" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -1 for each [[Extradimensional]] location in play.\n\n[cultist]: Reveal another token. After this skill test, discard cards from the top of the encounter deck until a location is discarded. Put that location into play and move there.\n\n[tablet]: -5. If Yog-Sothoth is in play, it attacks you after this skill test.\n\n[elder_thing]: -X. X is twice the shroud value of your location. If you fail and your location is [[Extradimensional]], discard it."
      else
        tool = "Easy / Standard\n\n[skull]: -1 for each [[Extradimensional]] location in play (max -5).\n\n[cultist]: Reveal another token. If you fail, after this skill test, discard cards from the top of the encounter deck until a location is discarded. Put that location into play and move there.\n\n[tablet]: -3. If Yog-Sothoth is in play, it attacks you after this skill test.\n\n[elder_thing]: -X. X is the shroud value of your location. If you fail and your location is [[Extradimensional]], discard it."
      end
    end
    -- curtain call
    if scenario.getDescription() == "Curtain Call" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X, where X is the amount of horror on you. (If you have no horror on you, X is 1.)\n\n[cultist] [tablet] [elder_thing]: -5. If your location has at least 1 horror on it, take 1 horror <i>(from the token pool)</i>. If your location has no horror on it, place 1 horror on it instead."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you have 3 or more horror on you).\n\n[cultist] [tablet] [elder_thing]: -4. If your location has at least 1 horror on it, take 1 horror <i>(from the token pool)</i>. If your location has no horror on it, place 1 horror on it instead."
      end
    end
    -- Last King
    if scenario.getDescription() == "The Last King" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: Reveal another token. If you fail, place 1 doom on the [[Lunatic]] enemy in play with the most remaining health.\n\n[cultist]: -3. Place 1 of your clues on your location.\n\n[tablet]: -4. Take 1 horror.\n\n[elder_thing]: -X. X is the shroud value of your location. If you fail, take 1 damage."
      else
        tool = "Easy / Standard\n\n[skull]: Reveal another token. If you fail, place 1 doom on a [[Lunatic]] enemy in play.\n\n[cultist]: -2. If you fail, place 1 of your clues on your location.\n\n[tablet]: -4. If you fail, take 1 horror.\n\n[elder_thing]: -X. X is the shroud value of your location."
      end
    end
    -- Echoes Past
    if scenario.getDescription() == "Echoes of the Past" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the total number of doom on enemies in play.\n\n[cultist]: -4. Place 1 doom on the nearest enemy.\n\n[tablet]: -4. Discard a random card from your hand.\n\n[elder_thing]: -4. If there is an enemy at your location, take 1 horror."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the highest number of doom on an enemy in play.\n\n[cultist]: -2. If you fail, place 1 doom on the nearest enemy.\n\n[tablet]: -2. If you fail, discard a random card from your hand.\n\n[elder_thing]: -2. If you fail and there is an enemy at your location, take 1 horror."
      end
    end
    -- Unspeakable Oath
    if scenario.getDescription() == "The Unspeakable Oath" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: Reveal another token. If you fail, randomly choose an enemy from among the set-aside [[Monster]] enemies and place it beneath the act deck without looking at it. (Limit once per test.)\n\n[cultist]: -X. X is the amount of horror on you. If you fail, take 1 horror.\n\n[tablet]: -X. X is the base shroud value of your location. If you fail, take 1 horror.\n\n[elder_thing]: 0. Either randomly choose an enemy from among the set-aside [[Monster]] enemies and place it beneath the act deck without looking at it, or this test automatically fails instead."
      else
        tool = "Easy / Standard\n\n[skull]: -1. If you fail, randomly choose an enemy from among the set-aside [[Monster]] enemies and place it beneath the act deck without looking at it.\n\n[cultist]: -X. X is the amount of horror on you.\n\n[tablet]: -X. X is the base shroud value of your location.\n\n[elder_thing]: 0. Either randomly choose an enemy from among the set-aside [[Monster]] enemies and place it beneath the act deck without looking at it, or this test automatically fails instead."
      end
    end
    -- A Phantom of Truth
    if scenario.getDescription() == "A Phantom of Truth" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the amount of doom in play.\n\n[cultist]: -2. Move each unengaged [[Byakhee]] in play once toward the nearest investigator.\n\n[tablet]: -4. Cancel the effects and icons of each skill card committed to this test.\n\n[elder_thing]: -3. If you fail, lose 1 resource for each point you failed by."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the amount of doom in play (max 5).\n\n[cultist]: -2. If you fail, move each unengaged [[Byakhee]] in play once toward the nearest investigator.\n\n[tablet]: -3. Cancel the effects and icons of each skill card committed to this test.\n\n[elder_thing]: -2. If you fail, lose 1 resource for each point you failed by."
      end
    end
    -- The Pallid Mask
    if scenario.getDescription() == "The Pallid Mask" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the number of locations away from the starting location you are.\n\n[cultist]: -3. If this token is revealed during an attack and this skill test is successful, this attack deals no damage.\n\n[tablet]: -3. If there is a [[Ghoul]] or [[Geist]] enemy at your location, it readies and attacks you (if there is more than one, choose one).\n\n[elder_thing]: -4. If you fail, search the encounter deck and discard pile for a [[Ghoul]] or [[Geist]] enemy and draw it."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of locations away from the starting location you are (max 5).\n\n[cultist]: -2. If this token is revealed during an attack, and this skill test is successful, this attack deals 1 less damage.\n\n[tablet]: -2. If there is a ready [[Ghoul]] or [[Geist]] enemy at your location, it attacks you (if there is more than one, choose one).\n\n[elder_thing]: -3. If you fail, search the encounter deck and discard pile for a [[Ghoul]] or [[Geist]] enemy and draw it."
      end
    end
    -- Dim Carcosa
    if scenario.getDescription() == "Dim Carcosa" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the amount of horror on you.\n\n[cultist]: Reveal another token. If you fail, take 2 horror.\n\n[tablet]: -5. If you fail and Hastur is in play, place 1 clue on your location <i>(from the token bank)</i>.\n\n[elder_thing]: -5. If this token is revealed during an attack or evasion attempt against a [[Monster]] or [[Ancient One]] enemy, lose 1 action."
      else
        tool = "Easy / Standard\n\n[skull]: -2 (-4 instead if you have no sanity remaining).\n\n[cultist]: Reveal another token. If you fail, take 1 horror.\n\n[tablet]: -3. If you fail and Hastur is in play, place 1 clue on your location <i>(from the token bank)</i>.\n\n[elder_thing]: -3. If this token is revealed during an attack or evasion attempt against a [[Monster]] or [[Ancient One]] enemy, lose 1 action."
      end
    end
    if scenario.getDescription() == "Black Stars Rise" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the total amount of doom on agendas in play.\n\n[cultist]: Reveal another token. If there is an enemy with 1 or more doom on it at your location, this test automatically fails instead.\n\n[tablet]: Reveal another token. If you do not succeed by at least 1, place 1 doom on each agenda.\n\n[elder_thing]: -3. If you fail, search the encounter deck and discard pile for a [[Byakhee]] enemy and draw it."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the highest amount of doom on an agenda in play.\n\n[cultist]: Reveal another token. If this token is revealed during an attack or evasion attempt against an enemy with doom on it, this skill test automatically fails instead.\n\n[tablet]: Reveal another token. If you fail, place 1 doom on each agenda.\n\n[elder_thing]: -2. If you fail, search the encounter deck and discard pile for a [[Byakhee]] enemy and draw it."
      end
    end
    -- untamed Wilds
    if scenario.getDescription() == "The Untamed Wilds" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 higher than the number of vengeance points in the victory display.\n\n[cultist]: -X. X is the number of locations in play.\n\n[tablet]: -X. X is the number of cards in the exploration deck (min 3).\n\n[elder_thing]: -3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of vengeance points in the victory display.\n\n[cultist]: -X. X is the number of locations in play (max 5).\n\n[tablet]: -X. X is the number of cards in the exploration deck (max 5).\n\n[elder_thing]: -2. If you are poisoned, this test automatically fails instead."
      end
    end
    --The doom of Eztli
    if scenario.getDescription() == "The Doom of Eztli" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if there is doom on your location).\n\n[cultist] [tablet]: -X. X is the total amount of doom on locations in play.\n\n[elder_thing]: Reveal another chaos token. Place 1 doom on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if there is doom on your location).\n\n[cultist] [tablet]: -X. X is the number of locations with doom on them.\n\n[elder_thing]: Reveal another chaos token. If you fail, place 1 doom on your location."
      end
    end
    --Threads of Fate
    if scenario.getDescription() == "Threads of Fate" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull] : -X. X is the total number of doom in play.\n\n[cultist]: -2. If you do not succeed by at least 2, take 1 direct damage.\n\n[tablet]: -2. If you do not succeed by at least 2, place 1 doom on each [[cultist]] enemy.\n\n[elder_thing]: -3. If you fail, lose 1 of your clues."
      else
        tool = "Easy / Standard\n\n[skull] : -X. X is the highest number of doom on a [[cultist]] enemy.\n\n[cultist]: -2. If you do not succeed by at least 1, take 1 damage.\n\n[tablet]: -2. If you do not succeed by at least 1, place 1 doom on the nearest [[cultist]] enemy.\n\n[elder_thing]: -2. If you fail, lose 1 of your clues."
      end
    end
    --The boundary beyond
    if scenario.getDescription() == "The Boundary Beyond" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if you are at an [[Ancient]] location).\n\n[cultist]: Reveal another token. If you fail, place 1 doom on each [[Cultist]] enemy.\n\n[tablet]: Reveal another token. If you fail, each [[Serpent]] enemy at your location attacks you.\n\n[elder_thing]: -4. Place 1 clue <i>(from the token pool)</i> on the nearest [[Ancient]] location."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are at an [[Ancient]] location).\n\n[cultist]: Reveal another token. If you fail, place 1 doom on a [[Cultist]] enemy.\n\n[tablet]: Reveal another token. If you fail and there is a [[Serpent]] enemy at your location, it attacks you.\n\n[elder_thing]: -4. If you fail, place 1 clue <i>(from the token pool)</i> on the nearest [[Ancient]] location."
      end
    end
    --Heart of the elders p1
    if scenario.getDescription() == "Heart of the Elders" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if you are in a [[Cave]] location).\n\n[cultist]: -3. If you fail, place 1 doom on your location.\n\n[tablet]: -3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area.\n\n[elder_thing]: -4. If you fail, take 1 horror."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are in a [[Cave]] location).\n\n[cultist]: -2. If you fail, place 1 doom on your location.\n\n[tablet]: -2. If you are poisoned, this test automatically fails instead.\n\n[elder_thing]: -3. If you fail, take 1 horror."
      end
    end
    -- City of Archives
    if scenario.getDescription() == "The City of Archives" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (if you have 5 or more cards in your hand, you automatically fail instead).\n\n[cultist] or [elder_thing]: -2. Place 1 of your clues on your location.\n\n[tablet]: -3. For each point you fail by, discard 1 random card from your hand."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you have 5 or more cards in your hand).\n\n[cultist] or [elder_thing]: -2. If you fail, place 1 of your clues on your location.\n\n[tablet]: -3. If you fail, discard 1 random card from your hand."
      end
    end
    --Depths of Yoth
    if scenario.getName() == "Scenario - Easy/Standard" then
      tool = "Easy / Standard\n\n[skull]: -X. X is the current depth level.\n\n[cultist]: Reveal another token. If you fail, each [[Serpent]] enemy at your location or a connecting location heals 2 damage.\n\n[tablet]: Reveal another token. If you fail, place 1 clue on your location <i>(from the token pool)</i>.\n\n[elder_thing]: -2. If there are 3 or more vengeance points in the victory display, you automatically fail this test, instead."
    end
    --hard
    if scenario.getName() == "Scenario - Hard/Expert" then
      tool = "Hard / Expert\n\n[skull]: -X. X is the current depth level. If you fail, take 1 horror.\n\n[cultist]: Reveal another token. If you fail, each [[Serpent]] enemy at your location or a connecting location heals 2 damage.\n\n[tablet]: Reveal another token. If you fail, place 1 clue on your location <i>(from the token pool)</i>.\n\n[elder_thing]: -4. If there are 3 or more vengeance points in the victory display, you automatically fail this test, instead."
    end
    --Shattered Aeons
    if scenario.getDescription() == "Shattered Aeons" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -3 (-5 instead if the Relic of Ages is at your location).\n\n[cultist]: -3. If you do not succeed by at least 1, place 1 doom on each [[Cultist]] enemy.\n\n[tablet]: -3. If you are poisoned, this test automatically fails instead. If you are not poisoned and you fail, put a set-aside Poisoned weakness into play in your threat area.\n\n[elder_thing]: -3. Shuffle the topmost [[Hex]] treachery in the encounter discard pile into the exploration deck."
      else
        tool = "Easy / Standard\n\n[skull]: -2 (-4 instead if the Relic of Ages is at your location).\n\n[cultist]: -2. If you do not succeed by at least 1, place 1 doom on the nearest [[Cultist]] enemy.\n\n[tablet]: -2. If you are poisoned, this test automatically fails instead.\n\n[elder_thing]: -2. If you fail, shuffle the topmost [[Hex]] treachery in the encounter discard pile into the exploration deck."
      end
    end
    --secret scenario
    if scenario.getDescription() == "Turn Back Time" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X . X is the total amount of doom on locations.\n\n[elder_thing]: -6. Place 1 doom on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -X . X is the number of locations with doom on them.\n\n[elder_thing]: -4. If you fail, place 1 doom on your location."
      end
    end
    --Dissappearance Twilight
    if scenario.getDescription() == "Disappearance at the Twilight Estate" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -5. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -3. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location."
      end
    end
    --Witching Hour
    if scenario.getDescription() == "The Witching Hour" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2. Discard cards from the top of the encounter deck equal to this test's difficulty.\n\n[tablet]: -2. If you fail, after this test resolves, draw the bottommost treachery in the encounter discard pile.\n\n[elder_thing]: -4. If you fail, ready each [[Witch]] enemy at your location and at each connecting location. Heal all damage from each of those enemies."
      else
        tool = "Easy / Standard\n\n[skull]: -1. For each point you fail by, discard the top card of the encounter deck.\n\n[tablet]: -1. If you fail, after this test resolves, draw the bottommost treachery in the encounter discard pile.\n\n[elder_thing]: -3. If you fail, choose an exhausted or damaged [[Witch]] enemy at your location or at a connecting location. Ready that enemy and heal all damage from it."
      end
    end
    --Death's Doorstep
    if scenario.getDescription() == "At Death's Doorstep" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if your location is haunted).\n\n[tablet]: -3. If this is an attack or evasion attempt, resolve each haunted ability on your location.\n\n[elder_thing]: -4. If there is a [[Spectral]] enemy at your location, take 1 damage and 1 horror."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if your location is haunted).\n\n[tablet]: -2. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location.\n\n[elder_thing]: -2. If there is a [[Spectral]] enemy at your location, take 1 damage."
      end
    end
    --Secret Name
    if scenario.getDescription() == "The Secret Name" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if you are at an [[Extradimensional]] location).\n\n[cultist]: Reveal another chaos token. If you fail, discard the top 5 cards of the encounter deck.\n\n[tablet]: -3. If you fail and Nahab is in play, she attacks you <i>(regardless of her current location)</i>.\n\n[elder_thing]: -4. Resolve the hunter keyword on each enemy in play."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are at an [[Extradimensional]] location).\n\n[cultist]: Reveal another chaos token. If you fail, discard the top 3 cards of the encounter deck.\n\n[tablet]: -2. If you fail and Nahab is at your location, she attacks you.\n\n[elder_thing]: -3. If you fail, resolve the hunter keyword on each enemy in play."
      end
    end
    --Wages of Sin
    if scenario.getDescription() == "The Wages of Sin" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the number of copies of Unfinished Business in the victory display. Reveal another token.\n\n[cultist]: -4. Until the end of the rount, each Heretic enemy in play gets +1 fight and +1 evade.\n\n[tablet]: -4. If you fail, trigger the forced ability on a copy of Unfinished Business in your threat area as if it were the end of the round.\n\n[elder_thing]: -2. If this is an attack or evasion attempt, resolve each haunted ability on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is 1 higher than the number of copies of Unfinished Business in the victory display.\n\n[cultist]: -3. Until the end of the round, each Heretic enemy in play gets +1 fight and +1 evade.\n\n[tablet]: -3. If you fail, trigger the forced ability on a copy of Unfinished Business in yout threat area as if it were the end of the round.\n\n[elder_thing]: -2. If you fail and this is an attack or evasion attempt, resolve each haunted ability on your location."
      end
    end
    -- For The Greater Good
    if scenario.getDescription() == "For the Greater Good" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the total number of doom among [[Cultist]] enemies in play.\n\n[cultist]: -2. Reveal another token.\n\n[tablet]: -3. If you fail, place 1 doom on each [[Cultist]] enemy in play. If there are no [[Cultist]] enemies in play, reveal another token.\n\n[elder_thing]: -3. If you fail, move all doom from the [[Cultist]] enemy with the most doom on it to the current agenda. If no [[Cultist]] enemies in play have doom on them, reveal another&nbsp;token."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the highest number of doom on a [[Cultist]] enemy in play.\n\n[cultist]: -2. Reveal another token.\n\n[tablet]: -3. If you fail, place 1 doom on the nearest [[Cultist]] enemy.\n\n[elder_thing]: -3. If you fail, move 1 doom from the nearest [[Cultist]] enemy to the current agenda."
      end
    end
    --Union and Disillusion
    if scenario.getDescription() == "Union and Disillusion" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -3. If this is a skill test during a <b>circle</b> action, reveal another token.\n\n[cultist]: -4. If you have no damage on you, take 1 damage. If you have no horror on you, take 1 horror.\n\n[tablet]: -4. If you fail, a [[Spectral]] enemy at your location attacks you <i>(even if it is exhausted).</i>\n\n[elder_thing]: -4. If this is a skill test during a <b>circle</b> action and you fail, resolve each haunted ability on your location."
      else
        tool = "Easy / Standard\n\n[skull]: -2. If this is a skill test during a <b>circle</b> action, reveal another token.\n\n[cultist]: -3. If you have no damage on you, take 1 damage. If you have no horror on you, take 1 horror.\n\n[tablet]: -3. If you fail, a [[Spectral]] enemy at your location attacks you <i>(even if it is exhausted).</i>\n\n[elder_thing]: -3. If this is a skill test during a <b>circle</b> action and you fail, resolve each haunted ability on your location."
      end
    end
    --Clutches of Chaos
    if scenario.getDescription() == "In the Clutches of Chaos" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 higher than the total amount of doom and breaches on your location.\n\n[cultist]: Reveal another token. If there are fewer than 3 breaches on your location, place 1 breach on your location.\n\n[tablet]: -3. For each point you fail by, remove 1 breach from the current act.\n\n[elder_thing]: -4. If you fail, place 1 breach on a random location."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the total amount of doom and breaches on your location.\n\n[cultist]: Reveal another token. If there are fewer than 3 breaches on your location, place 1 breach on your location.\n\n[tablet]: -2. For each point you fail by, remove 1 breach from the current act.\n\n[elder_thing]: -3. If you fail, place 1 breach on a random location."
      end
    end
    --Before the Black Throne
    if scenario.getDescription() == "Before the Black Throne" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the amount of doom on Azathoth, to a minimum of 2.\n\n[cultist]: Reveal another token. If you fail, search the encounter deck and discard pile for a [[Cultist]] enemy and draw it. Shuffle the encounter deck.\n\n[tablet]: -3. If you fail, Azathoth attacks you.\n\n[elder_thing]: -6. If your modified skill value for this test is 0, place 1 doom on Azathoth."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is half of the doom on Azathoth (rounded up), to a minimum of 2.\n\n[cultist]: Reveal another token. If you fail, search the encounter deck and discard pile for a [[Cultist]] enemy and draw it. Shuffle the encounter deck.\n\n[tablet]: -2. If you fail, Azathoth attacks you.\n\n[elder_thing]: -4. If your modified skill value for this test is 0, place 1 doom on Azathoth."
      end
    end
    --Beyond the gates of sleep
    if scenario.getDescription() == "Beyond the Gates of Sleep" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull] : -X. X is the number of cards in your hand.\n\n[cultist]: -X. X is the number of revealed [[Woods]] locations.\n\n[tablet]: -2. If this is an attack or evasion attempt against a swarming enemy, add 1 swarm card to it."
      else
        tool = "Easy / Standard\n\n[skull] : -X. X is half the number of cards in your hand (rounded up).\n\n[cultist]: -X. X is the number of revealed Enchanted Woods locations.\n\n[tablet]: -2. If you fail and this is an attack or evasion attempt against a swarming enemy, add 1 swarm card to it."
      end
    end
    --Waking Nightmare
    if scenario.getDescription() == "Waking Nightmare" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if you are engaged with a [[Staff]] enemy).\n\n[cultist]: Reveal another chaos token. If it is agenda 2 or 3, make an infestation test.\n\n[elder_thing]: -X. X is 1 higher than the number of infested locations."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are engaged with a [[Staff]] enemy).\n\n[cultist]: Reveal another chaos token. If you fail and it is agenda 2 or 3, make an infestation test.\n\n[elder_thing]: -X. X is the number of infested locations."
      end
    end
    --The search for kadath
    if scenario.getDescription() == "The Search for Kadath" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 more than the number of Signs of the Gods the investigators have uncovered.\n\n[cultist]: Reveal another token. If this token is revealed during an investigation and this skill test fails, increase that location's shroud by 2 for the remainder of the round.\n\n[tablet]: -3. If you fail, either take 1 damage and 1 horror, or place 1 doom on the current agenda.\n\n[elder_thing]: +1. The black cat points you in the right direction. If this token is revealed during an investigation and you succeed, discover 1 additional clue."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of Signs of the Gods the investigators have uncovered.\n\n[cultist]: Reveal another token. If this token is revealed during an investigation and this skill test fails, increase that location's shroud by 1 for the remainder of the round.\n\n[tablet]: -2. If you fail, either take 1 damage and 1 horror, or place 1 doom on the current agenda.\n\n[elder_thing]: +2. The black cat points you in the right direction. If this token is revealed during an investigation and you succeed, discover 1 additional clue."
      end
    end
    --A thousand shapes of horror
    if scenario.getDescription() == "A Thousand Shapes of Horror" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if you are at a [[Graveyard]] location).\n\n[cultist]: Reveal another token. If you fail and The Unnamable is in play, it attacks you (regardless of its current location).\n\n[tablet]: +1. The black cat causes a distraction. If this test is successful, choose and evade an enemy at any location with a fight value of X or lower, where X is the amount you succeeded by.\n\n[elder_thing]: -3. If you fail, you must either place 1 of your clues on your location or take 1 damage."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if you are at a [[Graveyard]] location).\n\n[cultist]: Reveal another token. If you fail and The Unnamable is in play, it attacks you (regardless of its current location).\n\n[tablet]: +2. The black cat causes a distraction. If this test is successful, choose and evade an enemy at any location with a fight value of X or lower, where X is the amount you succeeded by.\n\n[elder_thing]: -2. If you fail, you must either place 1 of your clues on your location or take 1 damage."
      end
    end
    --Dark Side of the moon
    if scenario.getDescription() == "Dark Side of the Moon" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is your alarm level.\n\n[cultist]: Reveal another token. If you fail and your alarm level is higher than your modified skill value, after this skill test ends, draw the top card of the encounter deck.\n\n[tablet]: -2. If you fail, raise your alarm level by 1.\n\n[elder_thing]: 0. The black cat summons several other cats to help. If this token is revealed during an evasion attempt and you succeed, deal 2 damage to the evaded enemy."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is half your alarm level (rounded up).\n\n[cultist]: Reveal another token. If you fail and your alarm level is higher than your modified skill value, after this skill test ends, draw the top card of the encounter deck.\n\n[tablet]: -1. If you fail, raise your alarm level by 1.\n\n[elder_thing]: +1. The black cat summons several other cats to help. If this token is revealed during an evasion attempt and you succeed, deal 2 damage to the evaded enemy."
      end
    end
    --point of no return
    if scenario.getDescription() == "Point of No Return" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 more than the amount of damage on this card.\n\n[cultist]: Reveal another token. If you fail, after this skill test ends, draw the top card of the encounter deck.\n\n[tablet]: 0. The black cat helps you navigate through the death-fire. If this token is revealed during an investigation and you succeed, draw 1 card.\n\n[elder_thing]: -4. If you fail by 2 or more, choose a ready enemy at your location or a connecting location. That enemy moves to your location, engages you, and makes an immediate attack."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the amount of damage on this card.\n\n[cultist]: Reveal another token. If you fail, after this skill test ends, draw the top card of the encounter deck.\n\n[tablet]: +1. The black cat helps you navigate through the death-fire. If this token is revealed during an investigation and you succeed, draw 1 card.\n\n[elder_thing]: -3. If you fail by 2 or more, choose a ready enemy at your location or a connecting location. That enemy moves to your location, engages you, and makes an immediate attack."
      end
    end
    --where the gods dwell
    if scenario.getDescription() == "Where the Gods Dwell" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the number of the current act plus the number of the current agenda.\n\n[cultist]: Reveal another token. If you fail, place 1 doom on the current agenda. This effect may cause the current agenda to advance.\n\n[tablet]: -6. If you fail, choose and reveal a copy of Nyarlathotep in your hand. It attacks you and is shuffled into the encounter deck.\n\n[elder_thing]: -1. The black cat reminds you that it's all a dream."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of the current act.\n\n[cultist]: Reveal another token. If you fail, place 1 doom on the current agenda.\n\n[tablet]: -4. If you fail, choose and reveal a copy of Nyarlathotep in your hand. It attacks you and is shuffled into the encounter deck.\n\n[elder_thing]: 0. The black cat reminds you that it's all a dream."
      end
    end
    --weaver of the cosmos
    if scenario.getDescription() == "Weaver of the Cosmos" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is the amount of doom on locations in play.\n\n[cultist]: Reveal another token. If you fail, and there is an [[Ancient One]] enemy at your location, it attacks you.\n\n[tablet]: -1. The black cat tears at the web with its claws. If you succeed by 2 or more, remove 1 doom from your location.\n\n[elder_thing]: -4. If this skill test fails during an attack against a [[Spider]] enemy, place 1 doom on that enemy's location."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the highest amount of doom on a location in play.\n\n[cultist]: Reveal another token. If you fail, and there is an [[Ancient One]] enemy at your location, it attacks you.\n\n[tablet]: 0. The black cat tears at the web with its claws. If you succeed by 2 or more, remove 1 doom from your location.\n\n[elder_thing]: -3. If this skill test fails during an attack against a [[Spider]] enemy, place 1 doom on that enemy's location."
      end
    end
    --pit of despair
    if scenario.getDescription() == "The Pit of Despair" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-3 instead if your location is partially flooded; -4 instead if your location is fully flooded).\n\n[cultist]: -2. If your location is flooded, take 1 damage.\n\n[tablet]: -2. If you control a key, take 1 horror.\n\n[elder_thing]: -3. If The Amalgam is in the depths, put it into play engaged with you."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-2 instead if your location is partially flooded; -3 instead if your location is fully flooded).\n\n[cultist]: -2. If you fail and your location is flooded, take 1 damage.\n\n[tablet]: -2. If you fail and you control a key, take 1 horror.\n\n[elder_thing]: -3. If you fail and The Amalgam is in the depths, put it into play engaged with you."
      end
    end
    --vanishing of elena harper
    if scenario.getDescription() == "The Vanishing of Elina Harper" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 more than the current agenda number.\n\n[cultist]: -2. Place 1 doom on the nearest enemy (2 doom instead if you failed).\n\n[tablet]: -3. Take 1 horror (1 horror and 1 damage instead if you failed).\n\n[elder_thing]: -4. Place 1 of your clues on your location (2 clues instead if you failed)."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the current agenda number.\n\n[cultist]: -2. If you fail, place 1 doom on the nearest enemy.\n\n[tablet]: -3. If you fail, take 1 horror.\n\n[elder_thing]: -4. If you fail, place 1 of your clues on your location."
      end
    end
    --in too deep
    if scenario.getDescription() == "In Too Deep" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 for each location to the east of your location (on the same row).\n\n[cultist]: -4. If you fail, move to the connecting location to the east, ignoring all barriers.\n\n[tablet]: -5. If you fail, choose a connecting location with no barriers between it and your location. Place 1 barrier between the two locations.\n\n[elder_thing]: -X. X is twice the number of barriers between your location and all connecting locations."
      else
        tool = "Easy / Standard\n\n[skull]: -1 for each location to the east of your location (on the same row).\n\n[cultist]: -2. If you fail, move to the connecting location to the east, ignoring all barriers.\n\n[tablet]: -3. If you fail, choose a connecting location with no barriers between it and your location. Place 1 barrier between the two locations.\n\n[elder_thing]: -X. X is the number of barriers between your location and all connecting locations."
      end
    end
    --devil reef
    if scenario.getDescription() == "Devil Reef" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -X. X is 1 more than the number of keys the investigators control.\n\n[cultist]: -3. If this is an attack or evasion attempt against a [[Deep One]] enemy, it engages you. (If it is already engaged with you, it disengages first, then re-engages you.)\n\n[tablet]: -4. If you are not in a vehicle, take 1 damage.\n\n[elder_thing]: -5. If your location has a key on it, take 1 horror."
      else
        tool = "Easy / Standard\n\n[skull]: -X. X is the number of keys the investigators control.\n\n[cultist]: -2. If you fail and this is an attack or evasion attempt against a [[Deep One]] enemy, it engages you. (If it is already engaged with you, it disengages first, then re-engages you.)\n\n[tablet]: -3. If you fail and you are not in a vehicle, take 1 damage.\n\n[elder_thing]: -4. If you fail and your location has a key on it, take 1 horror."
      end
    end
    --horror in high gear
    if scenario.getDescription() == "Horror in High Gear" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if there are 6 or fewer locations remaining in the Road deck).\n\n[cultist]: -2. For each point you fail by, an investigator in your vehicle places 1 of their clues on your location.\n\n[tablet]: -3. For each point you fail by, an investigator in your vehicle loses 1 resource.\n\n[elder_thing]: -4. Resolve the hunter keyword on each enemy in play."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if there are 6 or fewer locations remaining in the Road deck).\n\n[cultist]: -1. For each point you fail by, an investigator in your vehicle places 1 of their clues on your location.\n\n[tablet]: -2. For each point you fail by, an investigator in your vehicle loses 1 resource.\n\n[elder_thing]: -4. If you fail, resolve the hunter keyword on each enemy in play."
      end
    end
    --light in the fog
    if scenario.getDescription() == "A Light in the Fog" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2. If your location is flooded, reveal an additional chaos token.\n\n[cultist]: -2. If you fail, after this test ends, increase the flood level of your location (if you cannot, take 1 horror instead).\n\n[tablet]: -3. If you fail this test and your location is flooded, take 2 damage.\n\n[elder_thing]: -4. Move the nearest unengaged enemy once toward your location. It loses aloof during this movement."
      else
        tool = "Easy / Standard\n\n[skull]: -1. If your location is flooded, reveal an additional chaos token.\n\n[cultist]: -2. If you fail, after this test ends, increase the flood level of your location.\n\n[tablet]: -3. If you fail this test and your location is flooded, take 1 damage.\n\n[elder_thing]: -4. If you fail, move the nearest ready unengaged enemy once toward your location. It loses aloof during this movement."
      end
    end
    --lair of dagon
    if scenario.getDescription() == "The Lair of Dagon" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 for each key on this card.\n\n[cultist]: -2. Reveal an additional chaos token. If you reveal 1 or more [curse] tokens during this test, you automatically fail.\n\n[tablet]: -3. Place each key you control on your location and take 1 damage.\n\n[elder_thing]: -4. Add 2 [curse] tokens to the chaos bag."
      else
        tool = "Easy / Standard\n\n[skull]: -1 for each key on this card.\n\n[cultist]: 0. Reveal an additional chaos token. If you reveal 1 or more [curse] tokens during this test, you automatically fail.\n\n[tablet]: -3. If you fail, place each key you control on your location.\n\n[elder_thing]: -4. If you fail, add 1 [curse] token to the chaos bag."
      end
    end
    --into the maelstrom
    if scenario.getDescription() == "Into the Maelstrom" then
      if scenario.is_face_down == true then
        tool = "Hard / Expert\n\n[skull]: -2 (-4 instead if there are 4 or more unflooded [[Y'ha-nthlei]] locations in play).\n\n[cultist]: -4. If you fail, place 1 doom on the current agenda (this may cause the current agenda to advance).\n\n[tablet]: -5. If you fail, you must either increase the flood level of your location or take 1 damage.\n\n[elder_thing]: -6. If you fail and there is a key on your location, take 1 horror."
      else
        tool = "Easy / Standard\n\n[skull]: -1 (-3 instead if there are 4 or more unflooded [[Y'ha-nthlei]] locations in play).\n\n[cultist]: -3. If you fail, place 1 doom on the current agenda (this may cause the current agenda to advance).\n\n[tablet]: -4. If you fail, you must either increase the flood level of your location or take 1 damage.\n\n[elder_thing]: -5. If you fail and there is a key on your location, take 1 horror."
      end
    end
  end
  getObjectFromGUID("8b081b").editButton({index = 6, tooltip = tool})
  getObjectFromGUID("bd0ff4").editButton({index = 6, tooltip = tool})
  getObjectFromGUID("383d8b").editButton({index = 6, tooltip = tool})
  getObjectFromGUID("0840d5").editButton({index = 6, tooltip = tool})
end
