-- Search Assistant
-- made by:         Chr1Z
-- original by:     Tikatoy
-- description:     search the top X cards of your deck
information = {
    version = "1.3",
    last_updated = "26.09.2022"
}

MAT_GUIDS = { "8b081b", "bd0ff4", "383d8b", "0840d5" }

-- common parameters
local BUTTON_PARAMETERS          = {}
BUTTON_PARAMETERS.function_owner = self
BUTTON_PARAMETERS.font_size      = 125
BUTTON_PARAMETERS.width          = 650
BUTTON_PARAMETERS.height         = 225

local INPUT_PARAMETERS          = {}
INPUT_PARAMETERS.function_owner = self
INPUT_PARAMETERS.input_function = "updateSearchNumber"
INPUT_PARAMETERS.tooltip        = "number of cards to search"
INPUT_PARAMETERS.label          = "#"
INPUT_PARAMETERS.font_size      = 175
INPUT_PARAMETERS.width          = 400
INPUT_PARAMETERS.height         = INPUT_PARAMETERS.font_size + 23
INPUT_PARAMETERS.position       = { 0, 0.1, 0 }
INPUT_PARAMETERS.alignment      = 3
INPUT_PARAMETERS.validation     = 2

function onLoad(save_state)
    if save_state ~= nil then
        local loaded_data = JSON.decode(save_state)
        if loaded_data.playerColor ~= nil then
            playerColor = loaded_data.playerColor
        end
    end

    if playerColor == nil then
        playerColor = Player.getAvailableColors()[1]
    end

    normalView()

    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Search Assistant v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("last updated: " .. information["last_updated"], "White")
        printToAll("original concept by Tikatoy", "White")
    end)
end

function onSave()
    return JSON.encode({ playerColor = playerColor })
end

-- regular view with search box and color switcher
function normalView()
    self.clearButtons()
    self.clearInputs()

    createSearchButton()
    changeColor("initialize")
    self.createInput(INPUT_PARAMETERS)
end

-- view during a search with "done" buttons
function searchView()
    self.clearButtons()
    self.clearInputs()

    createDoneButton(true)
    createDoneButton(false)
end

-- change color (or initialize button)
function changeColor(arg)
    if arg ~= "initialize" then
        -- update table with colors
        COLORS = Player.getAvailableColors()
        table.insert(COLORS, COLORS[1])

        -- get index of current color and move up one step
        local pos = indexOf(COLORS, playerColor)
        if pos == nil then pos = 0 end
        playerColor = COLORS[pos + 1]

        -- remove button and recreate it afterwards
        self.removeButton(1)
    end

    BUTTON_PARAMETERS.click_function = "changeColor"
    BUTTON_PARAMETERS.tooltip        = "change color"
    BUTTON_PARAMETERS.position       = { 0, 0.1, -0.65 }
    BUTTON_PARAMETERS.label          = playerColor
    BUTTON_PARAMETERS.color          = Color.fromString(playerColor)
    BUTTON_PARAMETERS.hover_color    = BUTTON_PARAMETERS.color
    self.createButton(BUTTON_PARAMETERS)
end

-- create the search button
function createSearchButton()
    BUTTON_PARAMETERS.click_function = "startSearch"
    BUTTON_PARAMETERS.tooltip        = "start the search"
    BUTTON_PARAMETERS.position       = { 0, 0.1, 0.65 }
    BUTTON_PARAMETERS.label          = "Search"
    BUTTON_PARAMETERS.color          = Color.fromString("White")
    BUTTON_PARAMETERS.hover_color    = nil
    self.createButton(BUTTON_PARAMETERS)
end

-- create the done buttons (with and without shuffle)
function createDoneButton(arg)
    if arg then
        BUTTON_PARAMETERS.click_function = "endSearch1"
        BUTTON_PARAMETERS.tooltip        = "Done (Shuffle)"
        BUTTON_PARAMETERS.position       = { 0, 0.1, -0.65 }
        BUTTON_PARAMETERS.label          = "Shuffle"
    else
        BUTTON_PARAMETERS.click_function = "endSearch2"
        BUTTON_PARAMETERS.tooltip        = "Done (No Shuffle)"
        BUTTON_PARAMETERS.position       = { 0, 0.1, 0.65 }
        BUTTON_PARAMETERS.label          = "No Shuffle"
    end

    BUTTON_PARAMETERS.color       = Color.fromString("White")
    BUTTON_PARAMETERS.hover_color = nil
    self.createButton(BUTTON_PARAMETERS)
end

-- get the draw deck from the player mat
function getDrawDeck()
    mat.call("getDrawDiscardDecks")
    return mat.getVar("drawDeck")
end

-- input_function to get number of cards to search
function updateSearchNumber(_, _, input)
    INPUT_PARAMETERS.value = tonumber(input)
end

-- start the search (change UI, set hand aside, draw cards)
function startSearch(_, color)
    if INPUT_PARAMETERS.value == nil then
        printToColor("Enter the number of cards to search in the textbox.", color, "Orange")
        return
    end

    local hand_data = Player[playerColor].getHandTransform()

    -- make distinction between players based on hand position
    if hand_data.position.x < -30 then
        if hand_data.position.z > 0 then
            playerNumber = 1
        else
            playerNumber = 2
        end
    else
        if hand_data.position.z > 0 then
            playerNumber = 3
        else
            playerNumber = 4
        end
    end

    mat = getObjectFromGUID(MAT_GUIDS[playerNumber])
    local zoneID = mat.getVar("zoneID")

    drawDeck = getDrawDeck()
    if drawDeck == nil then
        printToColor("Draw pile could not be found!", color, "Red")
        return
    end

    drawDeckPos = drawDeck.getPosition()
    printToColor("Place target(s) of search on set aside hand.", color, "Green")

    -- get position for set aside cards
    local hand = Player[playerColor].getHandObjects()
    deck_rotation = { hand_data.rotation.x, hand_data.rotation.y + 180, 180 }

    -- for left players (p1 and p3) move to the left, for right players (p2 and p4) to the right
    if playerNumber == 1 or playerNumber == 3 then
        set_aside_pos = hand_data.position - 15 * hand_data.right
    else
        set_aside_pos = hand_data.position + 15 * hand_data.right
    end

    for i = #hand, 1, -1 do
        hand[i].setPosition(set_aside_pos - Vector(0, i * 0.3, 0))
        hand[i].setRotation(deck_rotation)
    end

    searchView()

    -- handling for Norman Withers
    for i, object in ipairs(getObjectFromGUID(zoneID).getObjects()) do
        if self.positionToLocal(object.getPosition()).z < 0.5 and object.tag == "Card" and not object.is_face_down then
            object.flip()
            Wait.time(function()
                drawDeck = getDrawDeck()
            end, 1)
            break
        end
    end

    Wait.time(function()
        drawDeck.deal(INPUT_PARAMETERS.value, playerColor)
    end, 1)
end

-- place hand back into deck and optionally shuffle
function endSearch1()
    endSearch("true")
end

function endSearch2()
    endSearch("false")
end

function endSearch(shuffle)
    local hand = Player[playerColor].getHandObjects()

    for i = #hand, 1, -1 do
        hand[i].setPosition(drawDeckPos + Vector(0, 6 - i * 0.3, 0))
        hand[i].setRotation(deck_rotation)
    end

    if shuffle == "true" then
        Wait.time(function()
            local deck = getDrawDeck()
            if deck ~= nil then
                deck.shuffle()
            end
        end, 2)
    end

    -- draw set aside cards (from the ground!)
    local objs = Physics.cast({
        origin = set_aside_pos - Vector(0, 5, 0),
        direction = { x = 0, y = 1, z = 0 },
        type = 3,
        size = { 2, 2, 2 }
    })

    for i, v in ipairs(objs) do
        local obj = v.hit_object
        if obj.tag == "Deck" then
            Wait.time(function()
                obj.deal(#obj.getObjects(), playerColor)
            end, 1)
            break
        end
    end

    normalView()
end

-- helper to search array
function indexOf(array, value)
    for i, v in ipairs(array) do
        if v == value then
            return i
        end
    end
end