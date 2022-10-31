-- Token Arranger
-- created by:      Chr1Z
-- original by:     Whimsical
-- description:     displays the content of the chaos bag
information = {
    version = "1.6",
    last_updated = "10.10.2022"
}

-- names of tokens in order
token_names = {
    "Elder Sign",
    "Skull",
    "Cultist",
    "Tablet",
    "Elder Thing",
    "Auto-fail",
    "Bless",
    "Curse",
    "Frost",
    ""
}

-- common parameters
local BUTTON_PARAMETERS          = {}
BUTTON_PARAMETERS.function_owner = self
BUTTON_PARAMETERS.label          = ""
BUTTON_PARAMETERS.tooltip        = "Add / Remove"
BUTTON_PARAMETERS.color          = { 0, 0, 0, 0 }
BUTTON_PARAMETERS.width          = 325
BUTTON_PARAMETERS.height         = 325

local INPUT_PARAMETERS          = {}
INPUT_PARAMETERS.function_owner = self
INPUT_PARAMETERS.font_size      = 100
INPUT_PARAMETERS.width          = 250
INPUT_PARAMETERS.height         = INPUT_PARAMETERS.font_size + 23
INPUT_PARAMETERS.alignment      = 3
INPUT_PARAMETERS.validation     = 2
INPUT_PARAMETERS.tab            = 2

-- tag for cloned tokens
TO_DELETE_TAG = "to_be_deleted"

function onSave() return JSON.encode(token_precedence) end

function onload(save_state)
    if save_state ~= nil then
        token_precedence = JSON.decode(save_state)
    else
        -- token modifiers for sorting (and order for same modifier)
        -- order starts at 2 because there is a "+1" token
        token_precedence = {
            ["Elder Sign"]  = { 100, 2 },
            ["Skull"]       = { -1, 3 },
            ["Cultist"]     = { -2, 4 },
            ["Tablet"]      = { -3, 5 },
            ["Elder Thing"] = { -4, 6 },
            ["Auto-fail"]   = { -100, 7 },
            ["Bless"]       = { 101, 8 },
            ["Curse"]       = { -101, 9 },
            ["Frost"]       = { -99, 10 },
            [""]            = { 0, 11 }
        }
    end

    updating = false

    -- create UI
    local offset = 0.725
    local pos = {
        x = { -1.067, 0.377 },
        z = -2.175
    }

    -- button and inputs index 1-10
    for i = 1, 10 do
        if i < 6 then
            BUTTON_PARAMETERS.position = { pos.x[1], 0, pos.z + i * offset }
            INPUT_PARAMETERS.position  = { pos.x[1] + offset, 0.1, pos.z + i * offset }
        else
            BUTTON_PARAMETERS.position = { pos.x[2], 0, pos.z + (i - 5) * offset }
            INPUT_PARAMETERS.position  = { pos.x[2] + offset, 0.1, pos.z + (i - 5) * offset }
        end

        BUTTON_PARAMETERS.click_function = attachIndex("tokenClick", i)
        INPUT_PARAMETERS.input_function  = attachIndex2("tokenInput", i)
        INPUT_PARAMETERS.value           = token_precedence[token_names[i]][1]

        self.createButton(BUTTON_PARAMETERS)
        self.createInput(INPUT_PARAMETERS)
    end

    -- index 11: "Update / Hide" button
    BUTTON_PARAMETERS.label          = "Update / Hide"
    BUTTON_PARAMETERS.click_function = "layout"
    BUTTON_PARAMETERS.tooltip        = "Left-Click: Update!\nRight-Click: Hide Tokens!"
    BUTTON_PARAMETERS.position       = { 0.725, 0.1, 2.025 }
    BUTTON_PARAMETERS.color          = { 1, 1, 1 }
    BUTTON_PARAMETERS.width          = 675
    BUTTON_PARAMETERS.height         = 175
    self.createButton(BUTTON_PARAMETERS)

    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Token Arranger v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("last updated: " .. information["last_updated"], "White")
        printToAll("original concept by Whimsical", "White")
    end)
end

-- helper functions to carry index
function attachIndex(click_function, index)
    local fn_name = click_function .. index
    _G[fn_name] = function(obj, player_color, alt_click)
        _G[click_function](obj, player_color, alt_click, index)
    end
    return fn_name
end

function attachIndex2(input_function, index)
    local fn_name = input_function .. index
    _G[fn_name] = function(obj, player_color, input, selected)
        _G[input_function](obj, player_color, input, selected, index)
    end
    return fn_name
end

-- click_function for buttons on chaos tokens
function tokenClick(obj, player_color, alt_click, index)
    if not updating then
        updating = true
        if alt_click then
            token_precedence[token_names[index]][1] = token_precedence[token_names[index]][1] - 1
        else
            token_precedence[token_names[index]][1] = token_precedence[token_names[index]][1] + 1
        end
        self.editInput({ index = index - 1, value = token_precedence[token_names[index]][1] })
        layout()
    end
end

-- input_function for input_boxes
function tokenInput(obj, player_color, input, selected, index)
    if selected == false and not updating then
        updating = true
        local num = tonumber(input)
        if num ~= nil then
            token_precedence[token_names[index]][1] = num
        end
        layout()
    end
end

-- order function for data sorting
function token_value_comparator(left, right)
    if left.value > right.value then return true
    elseif right.value > left.value then return false
    elseif left.order < right.order then return true
    elseif right.order < left.order then return false
    else return left.token.getGUID() > right.token.getGUID()
    end
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

-- main function (delete old tokens, clone chaos bag content, sort it and position it)
function layout(_, _, isRightClick)
    -- delete previously pulled out tokens
    for _, token in ipairs(getObjectsWithTag(TO_DELETE_TAG)) do token.destruct() end

    -- stop here if right-clicked
    if isRightClick then return end

    local chaos_bag = getChaosBag()
    local chaos_bag_objects = chaos_bag.getObjects()

    -- take each token out and clone it
    for _, data in ipairs(chaos_bag_objects) do
        chaos_bag.takeObject {
            guid = data.guid,
            smooth = false,
            callback_function = function(tok)
                chaos_bag.putObject(tok.clone())
                tok.addTag(TO_DELETE_TAG)
            end
        }
    end

    -- wait until all tokens have finished spawning
    Wait.condition(function() do_position() end,
        function() return #chaos_bag_objects == #getObjectsWithTag(TO_DELETE_TAG) end)
end

-- position tokens sorted by value
function do_position()
    local data = {}

    -- create table with tokens
    for i, token in ipairs(getObjectsWithTag(TO_DELETE_TAG)) do
        local name = token.getName()
        local value = tonumber(name)
        local precedence = token_precedence[name]

        data[i] = {
            token = token,
            value = value or precedence[1]
        }

        if precedence ~= nil then
            data[i].order = precedence[2]
        else
            data[i].order = value
        end
    end

    -- sort table by value (symbols last if same value)
    table.sort(data, token_value_comparator)

    -- laying out the tokens
    local pos           = self.getPosition() + Vector(3.55, -0.05, -3.95)
    local location      = { x = pos.x, y = pos.y, z = pos.z }
    local current_value = data[1].value

    for _, item in ipairs(data) do
        if item.value ~= current_value then
            location.x = location.x - 1.75
            location.z = pos.z
            current_value = item.value
        end
        item.token.setPosition(location)
        item.token.setRotation(self.getRotation())
        location.z = location.z - 1.75
    end
    updating = false
end