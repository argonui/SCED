tableHeightOffset =-9
function onSave()
    saved_data = JSON.encode({tid=tableImageData, cd=checkData})
    --saved_data = ""
    return saved_data
end

function onload(saved_data)
    --Loads the tracking for if the game has started yet
    if saved_data ~= "" then
         local loaded_data = JSON.decode(saved_data)
         tableImageData = loaded_data.tid
         checkData = loaded_data.cd
    else
        tableImageData = {}
        checkData = {move=false, scale=false}
    end

    --Disables interactable status of objects with GUID in list
    for _, guid in ipairs(ref_noninteractable) do
        local obj = getObjectFromGUID(guid)
        if obj then obj.interactable = false end
    end

    --Establish references to table parts
    obj_leg1 = getObjectFromGUID("afc863")
    obj_leg2 = getObjectFromGUID("c8edca")
    obj_leg3 = getObjectFromGUID("393bf7")
    obj_leg4 = getObjectFromGUID("12c65e")
    obj_surface = getObjectFromGUID("4ee1f2")
    obj_side_top = getObjectFromGUID("35b95f")
    obj_side_bot = getObjectFromGUID("f938a2")
    obj_side_lef = getObjectFromGUID("9f95fd")
    obj_side_rig = getObjectFromGUID("5af8f2")

    controlActive = true
    createOpenCloseButton()
end



--Activation/deactivation of control panel



--Activated by clicking on
function click_toggleControl(_, color)
    if permissionCheck(color) then
        if not controlActive then
            --Activate control panel
            controlActive = true
            self.clearButtons()
            createOpenCloseButton()
            createSurfaceInput()
            createSurfaceButtons()
            createScaleInput()
            createScaleButtons()
        else
            --Deactivate control panel
            controlActive = false
            self.clearButtons()
            self.clearInputs()
            createOpenCloseButton()

        end
    end
end




--Table surface control



--Changes table surface
function click_applySurface(_, color)
    if permissionCheck(color) then
        updateSurface()
        broadcastToAll("New Table Image Applied", {0.2,0.9,0.2})
    end
end

--Saves table surface
function click_saveSurface(_, color)
    if permissionCheck(color) then
        local nickname = self.getInputs()[1].value
        local url = self.getInputs()[2].value
        if nickname == "" then
            --No nickname
            broadcastToAll("Please supply a nickname for this save.", {0.9,0.2,0.2})
        else
            --Nickname exists

            if findInImageDataIndex(url, nickname) == nil then
                --Save doesn't exist already
                table.insert(tableImageData, {url=url, name=nickname})
                broadcastToAll("Image URL saved to memory.", {0.2,0.9,0.2})
                --Refresh buttons
                self.clearButtons()
                createOpenCloseButton()
                createSurfaceButtons()
                createScaleButtons()
            else
                --Save exists already
                broadcastToAll("Memory already contains a save with this Name or URL. Delete it first.", {0.9,0.2,0.2})
            end
        end
    end
end

--Loads table surface
function click_loadMemory(_, color, index)
    if permissionCheck(color) then
        self.editInput({index=0, value=tableImageData[index].name})
        self.editInput({index=1, value=tableImageData[index].url})
        updateSurface()
        broadcastToAll("Table Image Loaded", {0.2,0.9,0.2})
    end
end

--Deletes table surface
function click_deleteMemory(_, color, index)
    if permissionCheck(color) then
        table.remove(tableImageData, index)
        self.clearButtons()
        createOpenCloseButton()
        createSurfaceButtons()
        createScaleButtons()
        broadcastToAll("Element Removed from Memory", {0.2,0.9,0.2})
    end
end

--Updates surface from the values in the input field
function updateSurface()
    local customInfo = obj_surface.getCustomObject()
    customInfo.diffuse = self.getInputs()[2].value
    obj_surface.setCustomObject(customInfo)
    obj_surface = obj_surface.reload()
end



--Table Scale control



--Applies Scale to table pieces
function click_applyScale(_, color)
    if permissionCheck(color) then
        local newWidth = tonumber(self.getInputs()[3].value)
        local newDepth = tonumber(self.getInputs()[4].value)
        if type(newWidth) ~= "number" then
            broadcastToAll("Invalid Width", {0.9,0.2,0.2})
            return
        elseif type(newDepth) ~= "number" then
            broadcastToAll("Invalid Depth", {0.9,0.2,0.2})
            return
        elseif newWidth<0.1 or newDepth<0.1 then
            broadcastToAll("Scale cannot go below 0.1", {0.9,0.2,0.2})
            return
        elseif newWidth>12 or newDepth>12 then
            broadcastToAll("Scale should not go over 12 (world size limitation)", {0.9,0.2,0.2})
            return
        else
            changeTableScale(math.abs(newWidth), math.abs(newDepth))
            broadcastToAll("Scale applied.", {0.2,0.9,0.2})
        end
    end
end

--Checks/unchecks move box for hands
function click_checkMove(_, color)
    if permissionCheck(color) then
        local find_func = function(o) return o.click_function=="click_checkMove" end
        if checkData.move == true then
            checkData.move = false
            local buttonEntry = findButton(self, find_func)
            self.editButton({index=buttonEntry.index, label=""})
        else
            checkData.move = true
            local buttonEntry = findButton(self, find_func)
            self.editButton({index=buttonEntry.index, label=string.char(10008)})
        end
    end
end

--Checks/unchecks scale box for hands
--This button was disabled for technical reasons
--[[
function click_checkScale(_, color)
    if permissionCheck(color) then
        local find_func = function(o) return o.click_function=="click_checkScale" end
        if checkData.scale == true then
            checkData.scale = false
            local buttonEntry = findButton(self, find_func)
            self.editButton({index=buttonEntry.index, label=""})
        else
            checkData.scale = true
            local buttonEntry = findButton(self, find_func)
            self.editButton({index=buttonEntry.index, label=string.char(10008)})
        end
    end
end
]]

--Alters scale of elements and moves them
function changeTableScale(width, depth)
    --Scaling factors used to translate scale to position offset
    local width2pos = (width-1) * 18
    local depth2pos = (depth-1) * 18

    --Hand zone movement
    if checkData.move == true then
        for _, pc in ipairs(ref_playerColor) do
            if Player[pc].getHandCount() > 0 then
                moveHandZone(Player[pc], width2pos, depth2pos)
            end
        end
    end
    --Hand zone scaling
    --The button to enable this was disabled for technical reasons
    if checkData.scale == true then
        for _, pc in ipairs(ref_playerColor) do
            if Player[pc].getHandCount() > 0 then
                scaleHandZone(Player[pc], width, depth)
            end
        end
    end

    --Resizing table elements
    obj_side_top.setScale({width, 1, 1})
    obj_side_bot.setScale({width, 1, 1})
    obj_side_lef.setScale({depth, 1, 1})
    obj_side_rig.setScale({depth, 1, 1})
    obj_surface.setScale({width, 1, depth})

    --Moving table elements to accomodate new scale
    obj_side_lef.setPosition({-width2pos,tableHeightOffset,0})
    obj_side_rig.setPosition({ width2pos,tableHeightOffset,0})
    obj_side_top.setPosition({0,tableHeightOffset, depth2pos})
    obj_side_bot.setPosition({0,tableHeightOffset,-depth2pos})
    obj_leg1.setPosition({-width2pos,tableHeightOffset,-depth2pos})
    obj_leg2.setPosition({-width2pos,tableHeightOffset, depth2pos})
    obj_leg3.setPosition({ width2pos,tableHeightOffset, depth2pos})
    obj_leg4.setPosition({ width2pos,tableHeightOffset,-depth2pos})
    self.setPosition(obj_leg4.positionToWorld({-22.12, 8.74,-19.16}))
    --Only enabled when changing tableHeightOffset
    --obj_surface.setPosition({0,tableHeightOffset,0})
end

--Move hand zone, p=player reference, facts are scaling factors
function moveHandZone(p, width2pos, depth2pos)
    local widthX = obj_side_rig.getPosition().x
    local depthZ = obj_side_top.getPosition().z
    for i=1, p.getHandCount() do
        local handT = p.getHandTransform()
        local pos = handT.position
        local y = handT.rotation.y

        if y<45 or y>320 or y>135 and y<225 then
            if pos.z > 0 then
                pos.z = pos.z + depth2pos - depthZ
            else
                pos.z = pos.z - depth2pos + depthZ
            end
        else
            if pos.x > 0 then
                pos.x = pos.x + width2pos - widthX
            else
                pos.x = pos.x - width2pos + widthX
            end
        end

        --Only enabled when changing tableHeightOffset
        --pos.y = tableHeightOffset + 14

        handT.position = pos
        p.setHandTransform(handT, i)
    end
end


---Scales hand zones, p=player reference, facts are scaling factors
function scaleHandZone(p, width, depth)
    local widthFact = width / obj_side_top.getScale().x
    local depthFact = depth / obj_side_lef.getScale().x
    for i=1, p.getHandCount() do
        local handT = p.getHandTransform()
        local scale = handT.scale
        local y = handT.rotation.y
        if y<45 or y>320 or y>135 and y<225 then
            scale.x = scale.x * widthFact
        else
            scale.x = scale.x * depthFact
        end
        handT.scale = scale
        p.setHandTransform(handT, i)
    end
end



--Information gathering



--Checks if a color is promoted or host
function permissionCheck(color)
    if Player[color].host==true or Player[color].promoted==true then
        return true
    else
        return false
    end
end

--Locates a string saved within memory file
function findInImageDataIndex(...)
    for _, str in ipairs({...}) do
        for i, v in ipairs(tableImageData) do
            if v.url == str or v.name == str then
                return i
            end
        end
    end
    return nil
end

--Round number (num) to the Nth decimal (dec)
function round(num, dec)
  local mult = 10^(dec or 0)
  return math.floor(num * mult + 0.5) / mult
end

--Locates a button with a helper function
function findButton(obj, func)
    if func==nil then error("No func supplied to findButton") end
    for _, v in ipairs(obj.getButtons()) do
        if func(v) then
            return v
        end
    end
    return nil
end



--Creation of buttons/inputs



function createOpenCloseButton()
    local tooltip = "Open Table Control Panel"
    if controlActive then
        tooltip = "Close Table Control Panel"
    end
    self.createButton({
        click_function="click_toggleControl", function_owner=self,
        position={0,0,0}, rotation={-45,0,0}, height=400, width=400,
        color={1,1,1,0}, tooltip=tooltip
    })
end

function createSurfaceInput()
    local currentURL = obj_surface.getCustomObject().diffuse
    local nickname = ""
    if findInImageDataIndex(currentURL) ~= nil then
        nickname = tableImageData[findInImageDataIndex(currentURL)].name
    end
    self.createInput({
        label="Nickname", input_function="none", function_owner=self,
        alignment=3, position={0,0,2}, height=224, width=4000,
        font_size=200, tooltip="Enter nickname for table image (only used for save)",
        value=nickname
    })
    self.createInput({
        label="URL", input_function="none", function_owner=self,
        alignment=3, position={0,0,3}, height=224, width=4000,
        font_size=200, tooltip="Enter URL for tabletop image",
        value=currentURL
    })
end

function createSurfaceButtons()
    --Label
    self.createButton({
        label="Tabletop Surface Image", click_function="none",
        position={0,0,1}, height=0, width=0, font_size=300, font_color={1,1,1}
    })
    --Functional
    self.createButton({
        label="Apply Image\nTo Table", click_function="click_applySurface",
        function_owner=self, tooltip="Apply URL as table image",
        position={2,0,4}, height=440, width=1400, font_size=200,
    })
    self.createButton({
        label="Save Image\nTo Memory", click_function="click_saveSurface",
        function_owner=self, tooltip="Record URL into memory (requires nickname)",
        position={-2,0,4}, height=440, width=1400, font_size=200,
    })
    --Label
    self.createButton({
        label="Load From Memory", click_function="none",
        position={0,0,5.5}, height=0, width=0, font_size=300, font_color={1,1,1}
    })
    --Saves, created dynamically from memory file
    for i, memoryEntry in ipairs(tableImageData) do
        --Load
        local funcName = i.."loadMemory"
        local func = function(x,y) click_loadMemory(x,y,i) end
        self.setVar(funcName, func)
        self.createButton({
            label=memoryEntry.name, click_function=funcName,
            function_owner=self, tooltip=memoryEntry.url, font_size=200,
            position={-0.6,0,6.5+0.5*(i-1)}, height=240, width=3300,
        })
        --Delete
        local funcName = i.."deleteMemory"
        local func = function(x,y) click_deleteMemory(x,y,i) end
        self.setVar(funcName, func)
        self.createButton({
            label="DELETE", click_function=funcName,
            function_owner=self, tooltip="",
            position={3.6,0,6.5+0.5*(i-1)}, height=240, width=600,
            font_size=160, font_color={1,0,0}, color={0.8,0.8,0.8}
        })
    end
end

function createScaleInput()
    self.createInput({
        label=string.char(8644), input_function="none", function_owner=self,
        alignment=3, position={-8.5,0,2}, height=224, width=400,
        font_size=200, tooltip="Table Width",
        value=round(obj_side_top.getScale().x, 1)
    })
    self.createInput({
        label=string.char(8645), input_function="none", function_owner=self,
        alignment=3, position={-7.5,0,2}, height=224, width=400,
        font_size=200, tooltip="Table Depth",
        value=round(obj_side_lef.getScale().x, 1)
    })
end

function createScaleButtons()
    --Labels
    self.createButton({
        label="Table Scale", click_function="none",
        position={-8,0,1}, height=0, width=0, font_size=300, font_color={1,1,1}
    })
    self.createButton({
        label=string.char(8644).."            "..string.char(8645),
        click_function="none",
        position={-8,0,2}, height=0, width=0, font_size=300, font_color={1,1,1}
    })
    self.createButton({
        label="Move Hands:", click_function="none",
        position={-8.3,0,3}, height=0, width=0, font_size=200, font_color={1,1,1}
    })
    --Disabled due to me removing the feature for technical reasons
    --[[
    self.createButton({
        label="Scale Hands:", click_function="none",
        position={-8.3,0,4}, height=0, width=0, font_size=200, font_color={1,1,1}
    })
    ]]
    --Checkboxes
    local label = ""
    if checkData.move == true then label = string.char(10008) end
    self.createButton({
        label=label, click_function="click_checkMove",
        function_owner=self, tooltip="Check to move hands when table is rescaled",
        position={-6.8,0,3}, height=224, width=224, font_size=200,
    })
    --[[
    local label = ""
    if checkData.scale == true then label = string.char(10008) end
    self.createButton({
        label=label, click_function="click_checkScale",
        function_owner=self, tooltip="Check to scale the width of hands when table is rescaled",
        position={-6.8,0,4}, height=224, width=224, font_size=200,
    })
    ]]
    --Apply button
    self.createButton({
        label="Apply Scale", click_function="click_applyScale",
        function_owner=self, tooltip="Apply width/depth to table",
        position={-8,0,4}, height=440, width=1400, font_size=200,
    })
end





--Data tables




ref_noninteractable = {
    "afc863","c8edca","393bf7","12c65e","f938a2","9f95fd","35b95f",
    "5af8f2","4ee1f2","bd69bd"
}

ref_playerColor = {
    "White", "Brown", "Red", "Orange", "Yellow",
    "Green", "Teal", "Blue", "Purple", "Pink", "Black"
}

--Dummy function, absorbs unwanted triggers
function none() end