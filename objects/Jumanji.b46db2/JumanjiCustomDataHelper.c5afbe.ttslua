-- set true to enable debug logging
DEBUG = false

function log(message)
  if DEBUG then
    print(message)
  end
end

--[[
Known locations and clues. We check this to determine if we should
atttempt to spawn clues, first we look for <LOCATION_NAME>_<GUID> and if
we find nothing we look for <LOCATION_NAME>
format is [location_guid -> clueCount]
]]
LOCATIONS_DATA_JSON = [[
{
  "San Francisco": {"type": "fixed", "value": 1, "clueSide": "back"},
  "	Arkham": {"type": "perPlayer", "value": 1, "clueSide": "back"},
  "Buenos Aires": {"type": "fixed", "value": 2, "clueSide": "back"},
  "	London": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Rome": {"type": "perPlayer", "value": 3, "clueSide": "front"},
  "Istanbul": {"type": "perPlayer", "value": 4, "clueSide": "front"},
  "Tokyo_123abc": {"type": "perPlayer", "value": 0, "clueSide": "back"},
  "Tokyo_456efg": {"type": "perPlayer", "value": 4, "clueSide": "back"},
  "Tokyo": {"type": "fixed", "value": 2, "clueSide": "back"},
  "Shanghai_123": {"type": "fixed", "value": 12, "clueSide": "front"},
  "Sydney": {"type": "fixed", "value": 0, "clueSide": "front"},
  "Side Yard": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Backyard": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Entry Hall": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Living Room": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Dining Room": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Kitchen": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Bathroom": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Study": {"type": "perPlayer", "value": 3, "clueSide": "front"},
  "Whittle Residence": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Smitty's Diner": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Whittle Residence": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Brantford Police Station": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Brantford City Hall": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Telephone Dispatch Office": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Municipal Hospital": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Chronicle Archives": {"type": "perPlayer", "value": 3, "clueSide": "front"},
  "St. Simon's Church": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Municipal Mental Ward": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Boorstein Clinic": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Howell Asylum": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Parlor": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Foyer": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Veranda": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Reception Room": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Spiral Staircase": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Master Bedroom": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Abandoned Room": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Attic": {"type": "perPlayer", "value": 3, "clueSide": "front"},
  "Rampant Jungle": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Overgrown Streets": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Tangled Neighborhood": {"type": "perPlayer", "value": 2, "clueSide": "front"},
  "Shrouded Clearing": {"type": "perPlayer", "value": 1, "clueSide": "front"},
  "Dense Thicket": {"type": "perPlayer", "value": 1, "clueSide": "front"}
}
]]


PLAYER_CARD_DATA_JSON = [[
{
  "Tool Belt (0)": {
    "tokenType": "resource",
    "tokenCount": 2
  },
  "Tool Belt (3)": {
    "tokenType": "resource",
    "tokenCount": 4
  },
  "Yithian Rifle": {
    "tokenType": "resource",
    "tokenCount": 3
  },
  "xxx": {
    "tokenType": "resource",
    "tokenCount": 3
  }
}
]]

HIDDEN_CARD_DATA = {
  "Unpleasant Card (Doom)",
  "Unpleasant Card (Gloom)",
  "The Case of the Scarlet DOOOOOM!"
}

LOCATIONS_DATA = JSON.decode(LOCATIONS_DATA_JSON)
PLAYER_CARD_DATA = JSON.decode(PLAYER_CARD_DATA_JSON)

function onload(save_state)
  local playArea = getObjectFromGUID('721ba2')
  playArea.call("updateLocations", {self.getGUID()})
  local playerMatWhite = getObjectFromGUID('8b081b')
  playerMatWhite.call("updatePlayerCards", {self.getGUID()})
  local playerMatOrange = getObjectFromGUID('bd0ff4')
  playerMatOrange.call("updatePlayerCards", {self.getGUID()})
  local playerMatGreen = getObjectFromGUID('383d8b')
  playerMatGreen.call("updatePlayerCards", {self.getGUID()})
  local playerMatRed = getObjectFromGUID('0840d5')
  playerMatRed.call("updatePlayerCards", {self.getGUID()})
  local dataHelper = getObjectFromGUID('708279')
  dataHelper.call("updateHiddenCards", {self.getGUID()})
end