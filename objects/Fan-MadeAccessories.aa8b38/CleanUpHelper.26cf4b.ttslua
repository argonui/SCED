-- Clean Up Helper
-- made by:         Chr1Z
-- description:     Cleans up the table for the next scenario in a campaign:
--                  - sets counters to default values (resources and doom) or trauma values (health and sanity, if not disabled) from campaign log
--                  - puts everything on playmats and hands into respective trashcans
--                  - use the IGNORE_TAG to exclude objects from tidying (default: "CleanUpHelper_Ignore")
information = {
    version = "2.0",
    last_updated = "10.10.2022"
}

-- enable this for debugging
SHOW_RAYS = false

-- these objects will be ignored
IGNORE_GUIDS = {
    -- big playmat, change image panel and investigator counter
    "b7b45b"; "f182ee"; "721ba2";
    -- bless/curse manager
    "afa06b"; "bd0253"; "5933fb";
    -- stuff on agenda/act playmat
    "85c4c6"; "4a3aa4"; "fea079"; "b015d8"; "11e0cf"; "9f334f"; "70b9f6"; "0a5a29";
    -- doom/location token bag
    "47ffc3"; "170f10";
    -- table
    "4ee1f2"
}

-- objects with this tag will be ignored
IGNORE_TAG = "CleanUpHelper_ignore"

-- colors and order for following tables
COLORS = { "White"; "Orange"; "Green"; "Red"; "Agenda" }

-- counter GUIDS (4x damage, 4x sanity, 4x resource and 1x doom)
TOKEN_GUIDS = {
    "eb08d6"; "e64eec"; "1f5a0a"; "591a45";
    "468e88"; "0257d9"; "7b5729"; "beb964";
    "4406f0"; "816d84"; "cd15ac"; "a4b60d";
    "85c4c6"
}

-- default values (4x damage, 4x horror, 4x resources, 1x doom)
DEFAULT_VALUES = {
    0; 0; 0; 0;
    0; 0; 0; 0;
    5; 5; 5; 5;
    0
}

PLAYERMAT_GUIDS = { "8b081b"; "bd0ff4"; "383d8b"; "0840d5" }
CLUE_GUIDS      = { "d86b7c"; "1769ed"; "032300"; "37be78" }
TRASHCAN_GUIDS  = { "147e80"; "f7b6c8"; "5f896a"; "4b8594"; "70b9f6" }

PLAYMATZONE = getObjectFromGUID("a2f932")

-- values for physics.cast (4 entries for player zones, 5th entry for agenda/act deck, 6th for campaign log)
PHYSICS_POSITION = {
    { x = -54.5, y = 2, z = 21 };
    { x = -54.5, y = 2, z = -21 };
    { x = -25.0, y = 2, z = 26 };
    { x = -25.0, y = 2, z = -26 };
    { x = -02.0, y = 2, z = 10 };
    { x = -00.0, y = 2, z = -27 }
}

PHYSICS_ROTATION = {
    { x = 0, y = 270, z = 0 };
    { x = 0, y = 270, z = 0 };
    { x = 0, y = 000, z = 0 };
    { x = 0, y = 180, z = 0 };
    { x = 0, y = 270, z = 0 };
    { x = 0, y = 000, z = 0 }
}

PHYSICS_SCALE = {
    { x = 36.6, y = 1, z = 14.5 };
    { x = 36.6, y = 1, z = 14.5 };
    { x = 28.0, y = 1, z = 14.5 };
    { x = 28.0, y = 1, z = 14.5 };
    { x = 55.0, y = 1, z = 13.5 };
    { x = 05.0, y = 1, z = 05.0 }
}

local BUTTON_PARAMETERS          = {}
BUTTON_PARAMETERS.function_owner = self

-- saving the options
function onSave() return JSON.encode({ tidy_playermats, import_trauma, reset_resources }) end

function onLoad(saved_data)
    local loaded_data = JSON.decode(saved_data)
    if loaded_data ~= nil then
        tidy_playermats = loaded_data[1]
        import_trauma   = loaded_data[2]
        reset_resources = loaded_data[3]
    else
        tidy_playermats = true
        import_trauma   = true
        reset_resources = true
    end

    self.addContextMenuItem("More Information", function()
        printToAll("------------------------------", "White")
        printToAll("Clean Up Helper v" .. information["version"] .. " by Chr1Z", "Orange")
        printToAll("last updated: " .. information["last_updated"], "White")
        printToAll("ignore tag: " .. IGNORE_TAG, "White")
        printToAll("Player order in the campaign log for trauma import:\nWhite, Orange, Green, Red", "White")
    end)

    -- index 0: button as label
    BUTTON_PARAMETERS.label          = "Clean Up Helper v" .. information["version"]
    BUTTON_PARAMETERS.click_function = "none"
    BUTTON_PARAMETERS.position       = { x = 0, y = 0.1, z = -1.525 }
    BUTTON_PARAMETERS.height         = 0
    BUTTON_PARAMETERS.width          = 0
    BUTTON_PARAMETERS.font_size      = 165
    BUTTON_PARAMETERS.font_color     = "Black"
    self.createButton(BUTTON_PARAMETERS)

    -- index 1: option button for playermats
    BUTTON_PARAMETERS.label          = "Tidy playermats: " .. (tidy_playermats and "✓" or "✗")
    BUTTON_PARAMETERS.color          = { 0, 0, 0, 0.95 }
    BUTTON_PARAMETERS.click_function = "toggle1"
    BUTTON_PARAMETERS.position.z     = -0.8
    BUTTON_PARAMETERS.height         = 275
    BUTTON_PARAMETERS.width          = 1550
    BUTTON_PARAMETERS.font_size      = 165
    BUTTON_PARAMETERS.font_color     = "White"
    self.createButton(BUTTON_PARAMETERS)

    -- index 2: option button for trauma import
    BUTTON_PARAMETERS.label          = "Import trauma: " .. (import_trauma and "✓" or "✗")
    BUTTON_PARAMETERS.click_function = "toggle2"
    BUTTON_PARAMETERS.position.z     = -0.1
    self.createButton(BUTTON_PARAMETERS)

    -- index 3: option button for resources
    BUTTON_PARAMETERS.label          = "Reset resources: " .. (reset_resources and "✓" or "✗")
    BUTTON_PARAMETERS.click_function = "toggle3"
    BUTTON_PARAMETERS.position.z     = 0.6
    self.createButton(BUTTON_PARAMETERS)

    -- index 4: start button
    BUTTON_PARAMETERS.label          = "Start!"
    BUTTON_PARAMETERS.click_function = "cleanUp"
    BUTTON_PARAMETERS.position.z     = 1.3
    BUTTON_PARAMETERS.width          = 775
    self.createButton(BUTTON_PARAMETERS)

    -- create single table for ignoring
    for _, v in ipairs(CLUE_GUIDS) do table.insert(IGNORE_GUIDS, v) end
    for _, v in ipairs(TRASHCAN_GUIDS) do table.insert(IGNORE_GUIDS, v) end
    for _, v in ipairs(PLAYERMAT_GUIDS) do table.insert(IGNORE_GUIDS, v) end
    for _, v in ipairs(TOKEN_GUIDS) do table.insert(IGNORE_GUIDS, v) end
end

---------------------------------------------------------
-- click functions for option buttons
---------------------------------------------------------
function toggle1()
    tidy_playermats = not tidy_playermats
    self.editButton({ index = 1, label = "Tidy playermats: " .. (tidy_playermats and "✓" or "✗") })
end

function toggle2()
    import_trauma = not import_trauma
    self.editButton({ index = 2, label = "Import trauma: " .. (import_trauma and "✓" or "✗") })
end

function toggle3()
    reset_resources = not reset_resources
    self.editButton({ index = 3, label = "Reset resources: " .. (reset_resources and "✓" or "✗") })
end

---------------------------------------------------------
-- main function
---------------------------------------------------------

function cleanUp()
    printToAll("------------------------------", "White")
    printToAll("Clean up started!", "Orange")
    printToAll("Resetting counters...", "White")

    getTrauma()
    resetCounters()

    printToAll("Discarding player hands...", "White")
    discardHands()

    printToAll("Tidying big playmat...", "White")
    startLuaCoroutine(self, "tidyPlaymatCoroutine")
end

---------------------------------------------------------
-- modular functions, called by other functions
---------------------------------------------------------

-- set counters to reset values
function resetCounters()
    for i, guid in ipairs(TOKEN_GUIDS) do
        -- skip this step for resource tokens when option disabled (token number 9-12)
        if reset_resources or (i < 9 or i > 12) then
            local TOKEN = getObjectFromGUID(guid)
            if TOKEN ~= nil then
                TOKEN.setVar("val", RESET_VALUES[i])
                TOKEN.call("updateVal")
                TOKEN.call("updateSave")
            else
                printToAll("Token number " .. i .. " could not be found and was skipped.", "Yellow")
            end
        end
    end
end

-- read values for trauma from campaign log if enabled
function getTrauma()
    -- load default values
    RESET_VALUES = {}
    for k, v in pairs(DEFAULT_VALUES) do
        RESET_VALUES[k] = v
    end

    -- stop here if trauma import is disabled
    if not import_trauma then
        printToAll("Default values for health and sanity loaded.", "Yellow")
        return
    end

    -- get campaign log
    local c_log = findObjects(6)[1]
    if c_log == nil then
        printToAll("Campaign log not found in standard position!", "Yellow")
        printToAll("Default values for health and sanity loaded.", "Yellow")
        return
    end

    -- get data from campaign log if possible
    local counterData = c_log.hit_object.getVar("ref_buttonData")
    if counterData ~= nil then
        printToAll("Trauma values found in campaign log!", "Green")
        for i = 1, 10, 3 do
            RESET_VALUES[1 + (i - 1) / 3] = counterData.counter[i].value
            RESET_VALUES[5 + (i - 1) / 3] = counterData.counter[i + 1].value
        end
    else
        printToAll("Trauma values could not be found in campaign log!", "Yellow")
        printToAll("Default values for health and sanity loaded.", "Yellow")
    end
end

-- discard all hand objects
function discardHands()
    for i = 1, 4 do
        local trashcan = getObjectFromGUID(TRASHCAN_GUIDS[i])
        local hand = Player[COLORS[i]].getHandObjects()
        if trashcan == nil then return end
        for j = #hand, 1, -1 do trashcan.putObject(hand[j]) end
    end
end

-- clean up for big playmat
function tidyPlaymatCoroutine()
    local trashcan = getObjectFromGUID(TRASHCAN_GUIDS[5])

    if PLAYMATZONE == nil then
        printToAll("Scripting zone for big playmat could not be found!", "Red")
    elseif trashcan == nil then
        printToAll("Trashcan for big playmat could not be found!", "Red")
    else
        for _, obj in ipairs(PLAYMATZONE.getObjects()) do
            -- ignore these elements
            if indexOf(IGNORE_GUIDS, obj.getGUID()) == nil and obj.hasTag(IGNORE_TAG) == false then
                coroutine.yield(0)
                trashcan.putObject(obj)
            end
        end
    end
    printToAll("Tidying playermats and agenda mat...", "White")
    startLuaCoroutine(self, "tidyPlayerMatCoroutine")
    return 1
end

-- clean up for the four playermats and the agenda/act playmat
function tidyPlayerMatCoroutine()
    for i = 1, 5 do
        -- skip playermat (1-4) if option disabled
        if tidy_playermats or i == 5 then
            -- delay for animation purpose
            for k = 1, 30 do coroutine.yield(0) end

            -- get respective trashcan
            local trashcan = getObjectFromGUID(TRASHCAN_GUIDS[i])
            if trashcan == nil then
                printToAll("Trashcan for " .. COLORS[i] .. " playmat could not be found!", "Red")
                return
            end

            for _, entry in ipairs(findObjects(i)) do
                local obj = entry.hit_object
                local desc_low = string.lower(obj.getDescription())

                -- ignore these elements
                if indexOf(IGNORE_GUIDS, obj.getGUID()) == nil and
                    obj.hasTag(IGNORE_TAG) == false and
                    desc_low ~= "action token" then
                    coroutine.yield(0)
                    trashcan.putObject(obj)

                    -- flip action tokens back to ready
                elseif desc_low == "action token" and obj.is_face_down then
                    obj.flip()
                end
            end
        end
    end
    printToAll("Clean up completed!", "Green")
    return 1
end

---------------------------------------------------------
-- helper functions
---------------------------------------------------------

-- find objects depending on index (1 to 4 for playermats, 5 for agenda/act playmat, 6 for campaign log)
function findObjects(num)
    return Physics.cast({
        direction    = { 0, 1, 0 },
        max_distance = 2,
        type         = 3,
        size         = PHYSICS_SCALE[num],
        origin       = PHYSICS_POSITION[num],
        orientation  = PHYSICS_ROTATION[num],
        debug        = SHOW_RAYS
    })
end

-- helper to search array
function indexOf(array, value)
    for i, v in ipairs(array) do
        if v == value then
            return i
        end
    end
end