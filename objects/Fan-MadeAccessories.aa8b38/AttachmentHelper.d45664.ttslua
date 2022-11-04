-- Attachment Helper
-- updated by:      Chr1Z
-- original by:     -
-- description:     displays cards in it with cost/skill icons
information = {
    version = "1.4",
    last_updated = "10.10.2022"
}

-- save state and options to restore onLoad
function onSave() return JSON.encode({ cardsInBag, showCost, showIcons }) end

-- load variables and create context menu
function onload(saved_data)
    if saved_data ~= "" and saved_data ~= nil then
        local loaded_data = JSON.decode(saved_data)
        cardsInBag        = loaded_data[1]
        showCost          = loaded_data[2]
        showIcons         = loaded_data[3]
    else
        cardsInBag = {}
        showCost   = true
        showIcons  = true
    end

    recreateButtons()

    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Attachment Helper v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("original by: bankey", "White")
        printToAll("last updated: " .. information["last_updated"], "White")
    end)

    self.addContextMenuItem("Toggle cost", function(color)
        showCost = not showCost
        printToColor("Show cost of cards: " .. tostring(showCost), color, "White")
        refresh()
    end)

    self.addContextMenuItem("Toggle skill icons", function(color)
        showIcons = not showIcons
        printToColor("Show skill icons of cards: " .. tostring(showIcons), color, "White")
        refresh()
    end)
end

-- called for every card that enters
function onObjectEnterContainer(container, object)
    if container == self then
        findCard(object.getGUID(), object.getName(), object.getGMNotes())
        recreateButtons()
    end
end

-- removes leaving cards from the "cardInBag" table
function onObjectLeaveContainer(container, object)
    if container == self then
        local guid = object.getGUID()
        for i, card in ipairs(cardsInBag) do
            if card.id == guid then table.remove(cardsInBag, i) end
        end
        recreateButtons()
    end
end

-- refreshes displayed buttons based on contained cards
function refresh()
    cardsInBag = {}
    for _, object in ipairs(self.getObjects()) do
        findCard(object.guid, object.name, object.gm_notes)
    end
    recreateButtons()
end

-- gets cost and icons for a card
function findCard(guid, name, GMNotes)
    local cost = ""
    local icons = {}
    local metadata = {}

    if name == nil or name == "" then name = "unnamed" end

    if showCost or showIcons then
        metadata = JSON.decode(GMNotes)
    end

    if showCost then
        if GMNotes ~= "" then cost = metadata.cost end
        if cost == nil or cost == "" then cost = "–" end
        name = "[" .. cost .. "] " .. name
    end

    if showIcons then
        if GMNotes ~= "" then
            icons[1] = metadata.wildIcons
            icons[2] = metadata.willpowerIcons
            icons[3] = metadata.intellectIcons
            icons[4] = metadata.fightIcons
            icons[5] = metadata.agilityIcons
        end

        local IconTypes = { "Wild", "Willpower", "Intellect", "Fight", "Agility" }
        local found = false
        for i = 1, 5 do
            if icons[i] ~= nil and icons[i] ~= "" then
                if found == false then
                    name = name .. "\n" .. IconTypes[i] .. ": " .. icons[i]
                    found = true
                else
                    name = name .. " " .. IconTypes[i] .. ": " .. icons[i]
                end
            end
        end
    end

    table.insert(cardsInBag, { name = name, id = guid })
end

-- recreates buttons with up-to-date labels
function recreateButtons()
    self.clearButtons()
    local verticalPosition = 1.65

    for _, card in ipairs(cardsInBag) do
        if _G['removeCard' .. card.id] == nil then
            _G['removeCard' .. card.id] = function()
                removeCard(card.id)
            end
        end

        self.createButton({
            label          = card.name,
            click_function = "removeCard" .. card.id,
            function_owner = self,
            position       = { 0, 0, verticalPosition },
            height         = 200,
            width          = 1200,
            font_size      = string.len(card.name) > 20 and 75 or 100
        })

        verticalPosition = verticalPosition - 0.5
    end

    local countLabel = '\nAttachment\nHelper\nv' .. information["version"]
    if #cardsInBag ~= 0 then countLabel = #cardsInBag end

    self.createButton({
        label          = countLabel,
        click_function = 'none',
        function_owner = self,
        position       = { 0, 0, -1.35 },
        height         = 0,
        width          = 0,
        font_size      = 225,
        font_color     = { 1, 1, 1 }
    })
end

-- click-function for buttons to take a card out of the bag
function removeCard(cardGUID)
    self.takeObject({
        guid = cardGUID,
        rotation = self.getRotation(),
        position = self.getPosition() + Vector(0, 0.25, 0),
        callback_function = function(obj) obj.resting = true end
    })
end