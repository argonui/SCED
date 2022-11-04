PLAYER_CARD_DATA_JSON = [[
{
  "Flashlight (3)": {
    "tokenType": "resource",
    "tokenCount": 4
  }
}
]]

PLAYER_CARD_DATA = JSON.decode(PLAYER_CARD_DATA_JSON)

function onload(save_state)
  local playerMatWhite = getObjectFromGUID('8b081b')
  playerMatWhite.call("updatePlayerCards", {self.getGUID()})
  local playerMatOrange = getObjectFromGUID('bd0ff4')
  playerMatOrange.call("updatePlayerCards", {self.getGUID()})
  local playerMatGreen = getObjectFromGUID('383d8b')
  playerMatGreen.call("updatePlayerCards", {self.getGUID()})
  local playerMatRed = getObjectFromGUID('0840d5')
  playerMatRed.call("updatePlayerCards", {self.getGUID()})
end
