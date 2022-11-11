-- Customizable Cards: Pocket Multi Tool
-- by Chr1Z
information = {
    version = "1.7",
    last_updated = "12.10.2022"
}

-- Color information for buttons
boxSize = 40

-- static values
x_1         = -0.933
x_offset    = 0.075
y_visible   = 0.25
y_invisible = -0.5

-- z-values (lines on the sheet)
posZ = {
    -0.892,
    -0.560,
    -0.326,
    -0.092,
    0.142,
    0.376,
    0.610
}

-- box setup (amount of boxes per line and amount of marked boxes in that line)
existingBoxes = { 1, 1, 2, 2, 2, 3, 4 }

inputBoxes = {}

-- override 'marked boxes' for debugging ('all' or 'none')
markDEBUG = ""

-- save state when going into bags / decks
function onDestroy() self.script_state = onSave() end

function onSave() return JSON.encode({ markedBoxes, inputValues }) end

-- Startup procedure
function onLoad(saved_data)
    if saved_data ~= "" and markDEBUG == "" then
        local loaded_data = JSON.decode(saved_data)
        markedBoxes = loaded_data[1]
        inputValues = loaded_data[2]
    else
        markedBoxes = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
        inputValues = { "", "", "", "", "" }
    end

    makeData()
    createButtonsAndBoxes()

    self.addContextMenuItem("Reset Inputs", function() updateState() end)
    self.addContextMenuItem("Scale: normal", function() self.setScale({ 1, 1, 1 }) end)
    self.addContextMenuItem("Scale: double", function() self.setScale({ 2, 1, 2 }) end)
    self.addContextMenuItem("Scale: triple", function() self.setScale({ 3, 1, 3 }) end)
end

function updateState(markedBoxesNew)
    if markedBoxesNew then markedBoxes = markedBoxesNew end
    makeData()
    createButtonsAndBoxes()
end

-- create Data
function makeData()
    Data = {}
    Data.checkbox = {}
    Data.textbox = {}

    -- repeat this for each entry (= line) in existingBoxes
    local totalCount = 0
    for i = 1, #existingBoxes do
        -- repeat this for each checkbox per line
        for j = 1, existingBoxes[i] do
            totalCount                      = totalCount + 1
            Data.checkbox[totalCount]       = {}
            Data.checkbox[totalCount].pos   = {}
            Data.checkbox[totalCount].pos.x = x_1 + j * x_offset
            Data.checkbox[totalCount].pos.z = posZ[i]
            Data.checkbox[totalCount].row   = i

            if (markDEBUG == "all") or (markedBoxes[i] >= j and markDEBUG ~= "none") then
                Data.checkbox[totalCount].pos.y = y_visible
                Data.checkbox[totalCount].state = true
            else
                Data.checkbox[totalCount].pos.y = y_invisible
                Data.checkbox[totalCount].state = false
            end
        end
    end

    -- repeat this for each entry (= line) in inputBoxes
    local totalCount = 0
    for i = 1, #inputBoxes do
        -- repeat this for each textbox per line
        for j = 1, inputBoxes[i] do
            totalCount                     = totalCount + 1
            Data.textbox[totalCount]       = {}
            Data.textbox[totalCount].pos   = inputPos[totalCount]
            Data.textbox[totalCount].width = inputWidth[totalCount]
            Data.textbox[totalCount].value = inputValues[totalCount]
        end
    end
end

-- checks or unchecks the given box
function click_checkbox(tableIndex)
    local row = Data.checkbox[tableIndex].row

    if Data.checkbox[tableIndex].state == true then
        Data.checkbox[tableIndex].pos.y = y_invisible
        Data.checkbox[tableIndex].state = false

        markedBoxes[row] = markedBoxes[row] - 1
    else
        Data.checkbox[tableIndex].pos.y = y_visible
        Data.checkbox[tableIndex].state = true

        markedBoxes[row] = markedBoxes[row] + 1
    end

    self.editButton({
        index = tableIndex - 1,
        position = Data.checkbox[tableIndex].pos
    })
end

-- updates saved value for given text box
function click_textbox(i, value, selected)
    if selected == false then
        inputValues[i] = value
    end
end

function createButtonsAndBoxes()
    self.clearButtons()
    self.clearInputs()

    for i, box_data in ipairs(Data.checkbox) do
        local funcName = "checkbox" .. i
        local func = function() click_checkbox(i) end
        self.setVar(funcName, func)

        self.createButton({
            click_function = funcName,
            function_owner = self,
            position       = box_data.pos,
            height         = boxSize,
            width          = boxSize,
            font_size      = box_data.size,
            scale          = { 1, 1, 1 },
            color          = { 0, 0, 0 },
            font_color     = { 0, 0, 0 }
        })
    end

    for i, box_data in ipairs(Data.textbox) do
        local funcName = "textbox" .. i
        local func = function(_, _, val, sel) click_textbox(i, val, sel) end
        self.setVar(funcName, func)

        self.createInput({
            input_function = funcName,
            function_owner = self,
            label          = "Click to type",
            alignment      = 2,
            position       = box_data.pos,
            scale          = buttonScale,
            width          = box_data.width,
            height         = (inputFontsize * 1) + 24,
            font_size      = inputFontsize,
            color          = "White",
            font_color     = buttonFontColor,
            value          = box_data.value
        })
    end
end
