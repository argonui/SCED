--On-demand save function, remembers pitch and distance values
function updateSave()
    saved_data = JSON.encode({pitch=pitch, distance=distance})
    self.script_state = saved_data
end

--Startup, loading memory
function onload(saved_data)
    --Loads the tracking for if the game has started yet
    if saved_data ~= "" then
        local loaded_data = JSON.decode(saved_data)
        pitch = loaded_data.pitch
        distance = loaded_data.distance
    else
        pitch = 45
        distance = 30
    end

    createInputs()
    createButtons()
end

--Activated by finishing writing in the input box, updates save info
function input_entered(inputString, stillEditing , typeIndex)
    if stillEditing == false  then
        --Check to avoid empty input strings
        if tonumber(inputString) == nil then inputString = 0 end
        --Update save data
        if typeIndex==0 then
            pitch = inputString
        else
            distance = inputString
        end
        updateSave()
    end
end

--Activated by button, the -5 -1 +1 +5 buttons
function click_modify(amount, typeIndex)
    if typeIndex==0 then
        pitch = pitch + amount
        self.editInput({index=typeIndex, value=pitch})
    else
        distance = distance + amount
        self.editInput({index=typeIndex, value=distance})
    end
    updateSave()
end

--Activated by button, uses the data to move the camera
function click_setCamera(_, color)
    --Check if there is another object to use instead of self
    local targetObj = self
    local nameGUID = string.sub(self.getName(), 1, 6)
    if getObjectFromGUID(nameGUID) ~= nil then
        targetObj = getObjectFromGUID(nameGUID)
    end

    --Check if there is an offset to use instead of 180
    local offsetY = 180
    local offsetString = string.sub(self.getName(), 7)
    if tonumber(string.match(offsetString, "%d+")) ~= nil then
        offsetY = tonumber(string.match(offsetString, "%d+"))
    end

    --Move camera into position around object
    local pos = targetObj.getPosition()
    local rot = targetObj.getRotation()
    rot.y = rot.y + offsetY
    Player[color].lookAt({position=pos, pitch=pitch, yaw=rot.y, distance=distance})

    local objectList = getObjects()
    local AHLCGNavTile = nil

    for i,v in ipairs(objectList) do
        if v.getName() == 'Navigation Overlay Tile' then
            AHLCGNavTile = v
            break
        end
    end

--    local AHLCGNavTile = getObjectFromGUID("0ffbc5")
    if AHLCGNavTile then
        AHLCGNavTile.call('updateEditCamera', {pos, pitch, rot.y, distance})
    end
end




--Button/Input creation



--Text boxes for number input
function createInputs()
    local funcName = "inputFuncNamePitch"
    local func = function(_,_,x,z) input_entered(x,z,0) end
    self.setVar(funcName, func)
    self.createInput({
        input_function=funcName, function_owner=self, label="input",
        alignment=2, position={-3.4,0.35,-0.21}, rotation={0,0,0}, height=420, width=1400,
        font_size=400, color={57/255,46/255,40/255},
        font_color={1,1,1}, value=pitch,
        validation=3  -- int (1 = None, 2 = Integer, 3 = Float, 4 = Alphanumeric, 5 = Username, 6 = Name),
    })
    local funcName = "inputFuncNameDistance"
    local func = function(_,_,x,z) input_entered(x,z,1) end
    self.setVar(funcName, func)
    self.createInput({
        input_function=funcName, function_owner=self, label="input",
        alignment=4, position={3.4,0.35,-0.21}, rotation={0,0,0}, height=420, width=1400,
        font_size=400, color={57/255,46/255,40/255},
        font_color={1,1,1}, value=distance,
        validation=3  -- int (1 = None, 2 = Integer, 3 = Float, 4 = Alphanumeric, 5 = Username, 6 = Name),
    })
end

--Center button and -5 - +5 buttons
function createButtons()
    self.createButton({
        click_function="click_setCamera", function_owner=self,
        position={0,0.4,0}, height=900, width=900, color={1,1,1,0},
        tooltip="Set camera to this angle"
    })

    for i, ref in ipairs(ref_modifyPitchButtons) do
        local funcName = "pitchModifyFunction_"..i
        self.setVar(funcName, ref.func)
        local pos = {-3.4+ref.offset,0.3,0.6}
        self.createButton({
            click_function=funcName, function_owner=self,
            position=pos, height=240, width=320, color={1,1,1,0}
        })
    end

    for i, ref in ipairs(ref_modifyDistanceButtons) do
        local funcName = "distanceModifyFunction_"..i
        self.setVar(funcName, ref.func)
        local pos = {3.4+ref.offset,0.3,0.6}
        self.createButton({
            click_function=funcName, function_owner=self,
            position=pos, height=240, width=320, color={1,1,1,0}
        })
    end
end

--Data tables used in button creation

ref_modifyPitchButtons = {
    {offset=-0.37, func=function() click_modify(-1, 0) end},
    {offset=-1.11, func=function() click_modify(-5, 0) end},
    {offset=0.37, func=function() click_modify(1, 0) end},
    {offset=1.11, func=function() click_modify(5, 0) end},
}

ref_modifyDistanceButtons = {
    {offset=-0.37, func=function() click_modify(-1, 1) end},
    {offset=-1.11, func=function() click_modify(-5, 1) end},
    {offset=0.37, func=function() click_modify(1, 1) end},
    {offset=1.11, func=function() click_modify(5, 1) end},
}