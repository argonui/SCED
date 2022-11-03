-- Chaos Bag Manager
-- made by:         Chr1Z
-- based on:        Bless/Curse Manager
-- description:     for easier managing of the chaos bag (adding / removing tokens)
information = {
    version = "1.3",
    last_updated = "10.10.2022"
}

local TOKEN_URL = {
    ElderSign  = "https://i.imgur.com/nEmqjmj.png",
    plusOne    = "https://i.imgur.com/uIx8jbY.png",
    Zero       = "https://i.imgur.com/btEtVfd.png",
    minusOne   = "https://i.imgur.com/w3XbrCC.png",
    minusTwo   = "https://i.imgur.com/bfTg2hb.png",
    minusThree = "https://i.imgur.com/yfs8gHq.png",
    minusFour  = "https://i.imgur.com/qrgGQRD.png",
    minusFive  = "https://i.imgur.com/3Ym1IeG.png",
    minusSix   = "https://i.imgur.com/c9qdSzS.png",
    minusSeven = "https://i.imgur.com/4WRD42n.png",
    minusEight = "https://i.imgur.com/9t3rPTQ.png",
    Skull      = "https://i.imgur.com/stbBxtx.png",
    Cultist    = "https://i.imgur.com/VzhJJaH.png",
    Tablet     = "https://i.imgur.com/1plY463.png",
    ElderThing = "https://i.imgur.com/ttnspKt.png",
    AutoFail   = "https://i.imgur.com/lns4fhz.png",
    Frost      = "http://cloud-3.steamusercontent.com/ugc/1858293462583104677/195F93C063A8881B805CE2FD4767A9718B27B6AE/"
}

local TOKEN_NAMES = {
    -- first row
    "plusOne", "Zero", "minusOne", "minusTwo", "minusThree", "minusFour",
    -- second row
    "minusFive", "minusSix", "minusSeven", "minusEight", "Frost",
    -- third row
    "ElderSign", "Skull", "Cultist", "Tablet", "ElderThing", "AutoFail"
}

local BUTTON_TOOLTIP = {
    -- first row
    "+1", "0", "-1", "-2", "-3", "-4",
    -- second row
    "-5", "-6", "-7", "-8", "Frost",
    -- third row
    "Elder Sign", "Skull", "Cultist", "Tablet", "Elder Thing", "Auto-fail"
}

y0 = 0
z1 = -0.778
z2 = 0
z3 = 0.75

local BUTTON_POSITION = {
    -- first row
    { -1.90, y0, z1 },
    { -1.14, y0, z1 },
    { -0.38, y0, z1 },
    { 0.38, y0, z1 },
    { 1.14, y0, z1 },
    { 1.90, y0, z1 },
    -- second row
    { -1.90, y0, z2 },
    { -1.14, y0, z2 },
    { -0.38, y0, z2 },
    { 0.38, y0, z2 },
    { 1.90, y0, z2 },
    -- third row
    { -1.90, y0, z3 },
    { -1.14, y0, z3 },
    { -0.38, y0, z3 },
    { 0.38, y0, z3 },
    { 1.14, y0, z3 },
    { 1.90, y0, z3 },
}

-- common button parameters
local BUTTON_PARAMETERS          = {}
BUTTON_PARAMETERS.function_owner = self
BUTTON_PARAMETERS.color          = { 0, 0, 0, 0 }
BUTTON_PARAMETERS.width          = 300
BUTTON_PARAMETERS.height         = 300

function onload()
    -- create buttons for tokens
    for i = 1, #BUTTON_POSITION do
        BUTTON_PARAMETERS.position       = BUTTON_POSITION[i]
        BUTTON_PARAMETERS.click_function = attachIndex("button_click", i)
        BUTTON_PARAMETERS.tooltip        = BUTTON_TOOLTIP[i]
        self.createButton(BUTTON_PARAMETERS)
    end

    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Chaos Bag Manager v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("last updated: " .. information["last_updated"], "White")
    end)
end

-- get chaos bag from scripting zone and description
function getChaosBag()
    local chaosbag = nil
    local chaosbag_zone = getObjectFromGUID("83ef06")

    -- error handling: scripting zone not found
    if chaosbag_zone == nil then
        printToAll("Zone for chaos bag detection couldn't be found.", "Red")
        return nil
    end

    for _, v in ipairs(chaosbag_zone.getObjects()) do
        if v.getDescription() == "Chaos Bag" then
            chaosbag = getObjectFromGUID(v.getGUID())
            break
        end
    end

    -- error handling: chaos bag not found
    if chaosbag == nil then
        printToAll("Chaos bag couldn't be found.", "Red")
    end
    return chaosbag
end

-- helper function to carry index
function attachIndex(click_function, index)
    local fn_name = click_function .. index
    _G[fn_name] = function(obj, player_color, alt_click)
        _G[click_function](obj, player_color, alt_click, index)
    end
    return fn_name
end

-- click function for buttons
function button_click(obj, player_color, alt_click, index)
    chaosbag = getChaosBag()

    -- error handling: chaos bag not found
    if chaosbag == nil then return end

    name = BUTTON_TOOLTIP[index]
    tokens = {}
    for i, v in ipairs(chaosbag.getObjects()) do
        if v.name == name then table.insert(tokens, v.guid) end
    end

    token = TOKEN_NAMES[index]
    if alt_click then
        -- error handling: no matching token found
        if #tokens == 0 then
            printToAll("No " .. name .. " tokens in the chaos bag.", "Yellow")
            return
        end

        -- remove token
        chaosbag.takeObject({
            guid = tokens[1],
            position = self.getPosition(),
            smooth = false,
            callback_function = remove_callback
        })
    else
        -- spawn token (only 8 frost tokens allowed)
        if token == "Frost" and #tokens == 8 then
            printToAll("The maximum of 8 Frost tokens is already in the bag.", "Yellow")
            return
        end

        local obj = spawnObject({
            type = 'Custom_Tile',
            position = chaosbag.getPosition() + Vector(0, 1, 0),
            rotation = { x = 0, y = 260, z = 0 },
            callback_function = spawn_callback
        })
        obj.setCustomObject({
            type = 2,
            image = TOKEN_URL[token],
            thickness = 0.10
        })
    end
end

function remove_callback(obj)
    printToAll("Removing " .. name .. " token (in bag: " .. #tokens - 1 .. ")", "White")
    obj.destruct()
end

function spawn_callback(obj)
    obj.scale { 0.81, 1, 0.81 }
    obj.setName(name)
    printToAll("Adding " .. name .. " token (in bag: " .. #tokens + 1 .. ")", "White")
end