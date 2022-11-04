-- Hand Helper
-- updated by:      Chr1Z
-- original by:     -
-- description:     counts cards in your hand (all or unique), can discard a random card
information = {
    version = "1.2",
    last_updated = "11.10.2022"
}

MAT_GUIDS = { "8b081b", "bd0ff4", "383d8b", "0840d5" }

local BUTTON_PARAMETERS          = {}
BUTTON_PARAMETERS.function_owner = self

-- saving "playerColor" and "des"
function onSave() return JSON.encode({ playerColor, des}) end

function onLoad(saved_data)
    -- loading saved data
    local loaded_data = JSON.decode(saved_data)
    playerColor       = loaded_data[1] or Player.getAvailableColors()[1]
    des               = loaded_data[2] or false

    -- index 0: button as hand size label
    BUTTON_PARAMETERS.hover_color    = "White"
    BUTTON_PARAMETERS.click_function = "none"
    BUTTON_PARAMETERS.position       = { 0, 0.1, -0.4 }
    BUTTON_PARAMETERS.height         = 0
    BUTTON_PARAMETERS.width          = 0
    BUTTON_PARAMETERS.font_size      = 500
    BUTTON_PARAMETERS.font_color     = "White"
    self.createButton(BUTTON_PARAMETERS)

    -- index 1: button to toggle "des"
    BUTTON_PARAMETERS.label          = "DES: " .. (des and "✓" or "✗")
    BUTTON_PARAMETERS.click_function = "toggleDES"
    BUTTON_PARAMETERS.position       = { 0.475, 0.1, 0.25 }
    BUTTON_PARAMETERS.height         = 175
    BUTTON_PARAMETERS.width          = 440
    BUTTON_PARAMETERS.font_size      = 90
    BUTTON_PARAMETERS.font_color     = "Black"
    self.createButton(BUTTON_PARAMETERS)

    -- index 2: button to discard a card
    BUTTON_PARAMETERS.label          = "discard random card"
    BUTTON_PARAMETERS.click_function = "discardRandom"
    BUTTON_PARAMETERS.position       = { 0, 0.1, 0.7 }
    BUTTON_PARAMETERS.width          = 900
    self.createButton(BUTTON_PARAMETERS)

    -- index 3: button to select color
    BUTTON_PARAMETERS.label          = playerColor
    BUTTON_PARAMETERS.color          = playerColor
    BUTTON_PARAMETERS.hover_color    = playerColor
    BUTTON_PARAMETERS.click_function = "changeColor"
    BUTTON_PARAMETERS.tooltip        = "change color"
    BUTTON_PARAMETERS.position       = { -0.475, 0.1, 0.25 }
    BUTTON_PARAMETERS.width          = 440
    self.createButton(BUTTON_PARAMETERS)

    -- start loop to update card count
    loopId = Wait.time(||updateValue(), 1, -1)

    -- context menu to quickly bind color
    self.addContextMenuItem("Bind to my color", function(color)
        changeColor(_, _, _, color)
    end)

    -- context menu to display additional information
    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Hand Helper v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("last updated: " .. information["last_updated"], "White")
        printToAll("original by Tikatoy", "White")
        printToAll("Note: 'Hidden' cards can't be randomly discarded.", "Yellow")
        printToAll("Set them aside beforehand!", "Yellow")
    end)

    -- initialize the pseudo random number generator
    math.randomseed(os.time())
end

function onObjectHover(hover_color, obj)
    -- error handling
    if obj == nil then return end

    -- add context menu to "short supply"
    if obj.getName() == "Short Supply" then
        obj.addContextMenuItem("Discard 10 (" .. playerColor .. ")", shortSupply)
    end

    -- only continue if correct player hovers over "self"
    if obj ~= self or hover_color ~= playerColor then return end

    -- stop loop, toggle "des" and displayed value briefly, then start new loop
    Wait.stop(loopId)
    des = not des
    updateValue()
    des = not des
    loopId = Wait.time(||updateValue(), 1, -1)
end

-- toggle "des" and update button label
function toggleDES()
    des = not des
    self.editButton({index = 1, label = "DES: " .. (des and "✓" or "✗")})
    updateValue()
end

-- count cards in hand (by name for DES)
function updateValue()
    if not playerExists(playerColor) then return end

    local hand = Player[playerColor].getHandObjects()
    local size = 0

    if des then
        local cardHash = {}
        for _, obj in pairs(hand) do
            if obj.tag == "Card" then
                local name = obj.getName()
                local title = string.match(name, '(.+)(%s%(%d+%))') or name
                cardHash[title] = obj
            end
        end
        for _, obj in pairs(cardHash) do
            size = size + 1
        end
    else
        for _, obj in pairs(hand) do
            if obj.tag == "Card" then size = size + 1 end
        end
    end
    -- change button label and color
    self.editButton({index = 0, font_color = des and "Green" or "White", label = size})
end

-- get index of current color and move up one step (or down for right-click)
function changeColor(_, _, isRightClick, color)
    if color then
        playerColor = color
    else
        local COLORS = Player.getAvailableColors()
        local pos = indexOf(COLORS, playerColor)

        if isRightClick then
            if pos == nil or pos == 1 then pos = #COLORS
            else pos = pos - 1 end
        else
            if pos == nil or pos == #COLORS then pos = 1
            else pos = pos + 1 end
        end

        -- update playerColor
        playerColor = COLORS[pos]
    end

    -- update "change color" button (note: remove and create instantly updates hover_color)
    BUTTON_PARAMETERS.label          = playerColor
    BUTTON_PARAMETERS.color          = playerColor
    BUTTON_PARAMETERS.hover_color    = playerColor
    self.removeButton(3)
    self.createButton(BUTTON_PARAMETERS)
end

---------------------------------------------------------
-- discards a random card from hand
---------------------------------------------------------
function discardRandom()
    if not playerExists(playerColor) then return end

    -- error handling: hand is empty
    local hand = Player[playerColor].getHandObjects()
    if #hand == 0 then
        broadcastToAll("Cannot discard from empty hand!", "Red")
    else
        local mat = getPlayermat(playerColor)
        if mat == nil then return end

        local discardPos = mat.getTable("DISCARD_PILE_POSITION")
        if discardPos == nil then
            broadcastToAll("Couldn't retrieve discard position from playermat!", "Red")
            return
        end

        local num = math.random(1, #hand)
        hand[num].setPosition(discardPos)
        broadcastToAll(playerColor .. " randomly discarded card " .. num .. "/" .. #hand .. ".", "White")
    end
end

---------------------------------------------------------
-- discards the top 10 cards of your deck
---------------------------------------------------------
function shortSupply(color)
    local mat = getPlayermat(playerColor)
    if mat == nil then return end

    -- get draw deck and discard pile
    mat.call("getDrawDiscardDecks")
    drawDeck = mat.getVar("drawDeck")
    local discardPos = mat.getTable("DISCARD_PILE_POSITION")
    if discardPos == nil then
        broadcastToAll("Couldn't retrieve discard position from playermat!", "Red")
        return
    end

    if drawDeck == nil then
        broadcastToColor("Deck not found!", color, "Yellow")
        return
    elseif drawDeck.tag ~= "Deck" then
        broadcastToColor("Deck only contains a single card!", color, "Yellow")
        return
    end

    -- discard cards
    discardPos[2] = 0.5
    for i = 1, 10 do
        discardPos[2] = discardPos[2] + 0.05 * i
        drawDeck.takeObject({ flip = true; position = discardPos })
    end
end

---------------------------------------------------------
-- helper functions
---------------------------------------------------------

-- helper to search array
function indexOf(array, value)
    for i, v in ipairs(array) do
        if v == value then return i end
    end
end

-- helper to check if player exists
function playerExists(color)
    local COLORS = Player.getAvailableColors()
    return indexOf(COLORS, color) and true or false
end

-- helper to find playermat based on hand position
function getPlayermat(color)       
    local pos = Player[playerColor].getHandTransform().position
    if pos.x < -30 then
        if pos.z > 0 then
            playerNumber = 1
        else
            playerNumber = 2
        end
    else
        if pos.z > 0 then
            playerNumber = 3
        else
            playerNumber = 4
        end
    end

    local mat = getObjectFromGUID(MAT_GUIDS[playerNumber])
    if mat == nil then
        broadcastToAll(playerColor .. " playermat could not be found!", "Yellow")
    end
    return mat
end