-- Utility memory bag by Directsun
-- Version 2.5.2
-- Fork of Memory Bag 2.0 by MrStump

function updateSave()
    local data_to_save = {["ml"]=memoryList}
    saved_data = JSON.encode(data_to_save)
    self.script_state = saved_data
end

function combineMemoryFromBagsWithin()
  local bagObjList = self.getObjects()
  for _, bagObj in ipairs(bagObjList) do
    local data = bagObj.lua_script_state
      if data ~= nil then
        local j = JSON.decode(data)
        if j ~= nil and j.ml ~= nil then
          for guid, entry in pairs(j.ml) do
            memoryList[guid] = entry
          end
        end
      end
    end
end

function updateMemoryWithMoves()
    memoryList = memoryListBackup
    --get the first transposed object's coordinates
    local obj = getObjectFromGUID(moveGuid)

    -- p1 is where needs to go, p2 is where it was
    local refObjPos = memoryList[moveGuid].pos
    local deltaPos = findOffsetDistance(obj.getPosition(), refObjPos, nil)
    local movedRotation = obj.getRotation()
    for guid, entry in pairs(memoryList) do
        memoryList[guid].pos.x = entry.pos.x - deltaPos.x
        memoryList[guid].pos.y = entry.pos.y - deltaPos.y
        memoryList[guid].pos.z = entry.pos.z - deltaPos.z
        -- memoryList[guid].rot.x = movedRotation.x
        -- memoryList[guid].rot.y = movedRotation.y
        -- memoryList[guid].rot.z = movedRotation.z
    end

    --theList[obj.getGUID()] = {
    --    pos={x=round(pos.x,4), y=round(pos.y,4), z=round(pos.z,4)},
    --    rot={x=round(rot.x,4), y=round(rot.y,4), z=round(rot.z,4)},
    --    lock=obj.getLock()
    --}
    moveList = {}
end

function onload(saved_data)
    fresh = true
    if saved_data ~= "" then
        local loaded_data = JSON.decode(saved_data)
        --Set up information off of loaded_data
        memoryList = loaded_data.ml
    else
        --Set up information for if there is no saved saved data
        memoryList = {}
    end

    moveList = {}
    moveGuid = nil

    if next(memoryList) == nil then
        createSetupButton()
    else
        fresh = false
        createMemoryActionButtons()
    end
end


--Beginning Setup


--Make setup button
function createSetupButton()
    self.createButton({
        label="Setup", click_function="buttonClick_setup", function_owner=self,
        position={0,0.1,-2.1}, rotation={0,0,0}, height=220, width=500,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })
end

--Triggered by Transpose button
function buttonClick_transpose()
    moveGuid = nil
    broadcastToAll("Select one object and move it- all objects will move relative to the new location", {0.75, 0.75, 1})
    memoryListBackup = duplicateTable(memoryList)
    memoryList = {}
    moveList = {}
    self.clearButtons()
    createButtonsOnAllObjects(true)
    createSetupActionButtons(true)
end

--Triggered by setup button,
function buttonClick_setup()
    memoryListBackup = duplicateTable(memoryList)
    memoryList = {}
    self.clearButtons()
    createButtonsOnAllObjects(false)
    createSetupActionButtons(false)
end

function getAllObjectsInMemory()
  local objTable = {}
  local curObj = {}

  for guid in pairs(memoryListBackup) do
    curObj = getObjectFromGUID(guid)
    table.insert(objTable, curObj)
  end

  return objTable
  -- return getAllObjects()
end

--Creates selection buttons on objects
function createButtonsOnAllObjects(move)
    local howManyButtons = 0

    local objsToHaveButtons = {}
    if move == true then
      objsToHaveButtons = getAllObjectsInMemory()
    else
      objsToHaveButtons = getAllObjects()
    end

    for _, obj in ipairs(objsToHaveButtons) do
        if obj ~= self then
            local dummyIndex = howManyButtons
            --On a normal bag, the button positions aren't the same size as the bag.
            globalScaleFactor = 1 * 1/self.getScale().x
            --Super sweet math to set button positions
            local selfPos = self.getPosition()
            local objPos = obj.getPosition()
            local deltaPos = findOffsetDistance(selfPos, objPos, obj)
            local objPos = rotateLocalCoordinates(deltaPos, self)
            objPos.x = -objPos.x * globalScaleFactor
            objPos.y = objPos.y * globalScaleFactor + 2
            objPos.z = objPos.z * globalScaleFactor * 0.9
            --Offset rotation of bag
            local rot = self.getRotation()
            rot.y = -rot.y + 180
            --Create function
            local funcName = "selectButton_" .. howManyButtons
            local func = function() buttonClick_selection(dummyIndex, obj, move) end
            local color = {0.75,0.25,0.25,0.6}
            local colorMove = {0,0,1,0.6}
            if move == true then
              color = colorMove
            end
            self.setVar(funcName, func)
            self.createButton({
                click_function=funcName, function_owner=self,
                position=objPos, rotation=rot, height=500, width=500,
                color=color,
            })
            howManyButtons = howManyButtons + 1
        end
    end
end

--Creates submit and cancel buttons
function createSetupActionButtons(move)
    self.createButton({
        label="Cancel", click_function="buttonClick_cancel", function_owner=self,
      position={-0.6,0.1,-2.1}, rotation={0,0,0}, height=220, width=550,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })

    self.createButton({
        label="Submit", click_function="buttonClick_submit", function_owner=self,
        position={-0.6,0.3,-2.5}, rotation={0,0,0}, height=220, width=550,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })

    if move == false then
      self.createButton({
          label="Add", click_function="buttonClick_add", function_owner=self,
          position={0.6,0.3,-2.1}, rotation={0,0,0}, height=220, width=550,
          font_size=130, color={0,0,0}, font_color={0.25,1,0.25}
      })

        if fresh == false then
            self.createButton({
                label="Set New", click_function="buttonClick_setNew", function_owner=self,
                position={0.6,0.3,-2.9}, rotation={0,0,0}, height=220, width=550,
                font_size=130, color={0,0,0}, font_color={0.75,0.75,1}
            })
            self.createButton({
                label="Remove", click_function="buttonClick_remove", function_owner=self,
                position={0.6,0.3,-2.5}, rotation={0,0,0}, height=220, width=550,
                font_size=130, color={0,0,0}, font_color={1,0.25,0.25}
            })
        end
    end

    self.createButton({
        label="Reset", click_function="buttonClick_reset", function_owner=self,
        position={-0.6,0.3,-2.9}, rotation={0,0,0}, height=220, width=550,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })
end


--During Setup


--Checks or unchecks buttons
function buttonClick_selection(index, obj, move)
    local colorMove = {0,0,1,0.6}
    local color = {0,1,0,0.6}

    previousGuid = selectedGuid
    selectedGuid = obj.getGUID()

    theList = memoryList
    if move == true then
       theList = moveList
       if previousGuid ~= nil and previousGuid ~= selectedGuid then
         local prevObj = getObjectFromGUID(previousGuid)
         prevObj.highlightOff()
         self.editButton({index=previousIndex, color=colorMove})
         theList[previousGuid] = nil
       end
       previousIndex = index
    end

    if theList[selectedGuid] == nil then
        self.editButton({index=index, color=color})
        --Adding pos/rot to memory table
        local pos, rot = obj.getPosition(), obj.getRotation()
        --I need to add it like this or it won't save due to indexing issue
        theList[obj.getGUID()] = {
            pos={x=round(pos.x,4), y=round(pos.y,4), z=round(pos.z,4)},
            rot={x=round(rot.x,4), y=round(rot.y,4), z=round(rot.z,4)},
            lock=obj.getLock()
        }
        obj.highlightOn({0,1,0})
    else
      color = {0.75,0.25,0.25,0.6}
      if move == true then
        color = colorMove
      end
        self.editButton({index=index, color=color})
        theList[obj.getGUID()] = nil
        obj.highlightOff()
    end
end

--Cancels selection process
function buttonClick_cancel()
    memoryList = memoryListBackup
    moveList = {}
    self.clearButtons()
    if next(memoryList) == nil then
        createSetupButton()
    else
        createMemoryActionButtons()
    end
    removeAllHighlights()
    broadcastToAll("Selection Canceled", {1,1,1})
    moveGuid = nil
end

--Saves selections
function buttonClick_submit()
    fresh = false
    if next(moveList) ~= nil then
        for guid in pairs(moveList) do
            moveGuid = guid
        end
        if memoryListBackup[moveGuid] == nil then
            broadcastToAll("Item selected for moving is not already in memory", {1, 0.25, 0.25})
        else
            broadcastToAll("Moving all items in memory relative to new objects position!", {0.75, 0.75, 1})
            self.clearButtons()
            createMemoryActionButtons()
            local count = 0
            for guid in pairs(moveList) do
                moveGuid = guid
                count = count + 1
                local obj = getObjectFromGUID(guid)
                if obj ~= nil then obj.highlightOff() end
            end
            updateMemoryWithMoves()
            updateSave()
            buttonClick_place()
        end
    elseif next(memoryList) == nil and moveGuid == nil then
      memoryList = memoryListBackup
      broadcastToAll("No selections made.", {0.75, 0.25, 0.25})
    end
    combineMemoryFromBagsWithin()
    self.clearButtons()
    createMemoryActionButtons()
    local count = 0
    for guid in pairs(memoryList) do
        count = count + 1
        local obj = getObjectFromGUID(guid)
        if obj ~= nil then obj.highlightOff() end
    end
    broadcastToAll(count.." Objects Saved", {1,1,1})
    updateSave()
    moveGuid = nil
end

function combineTables(first_table, second_table)
  for k,v in pairs(second_table) do first_table[k] = v end
end

function buttonClick_add()
    fresh = false
    combineTables(memoryList, memoryListBackup)
    broadcastToAll("Adding internal bags and selections to existing memory", {0.25, 0.75, 0.25})
    combineMemoryFromBagsWithin()
    self.clearButtons()
    createMemoryActionButtons()
    local count = 0
    for guid in pairs(memoryList) do
        count = count + 1
        local obj = getObjectFromGUID(guid)
        if obj ~= nil then obj.highlightOff() end
    end
    broadcastToAll(count.." Objects Saved", {1,1,1})
    updateSave()
end

function buttonClick_remove()
        broadcastToAll("Removing Selected Entries From Memory", {1.0, 0.25, 0.25})
        self.clearButtons()
        createMemoryActionButtons()
        local count = 0
        for guid in pairs(memoryList) do
            count = count + 1
            memoryListBackup[guid] = nil
            local obj = getObjectFromGUID(guid)
            if obj ~= nil then obj.highlightOff() end
        end
        broadcastToAll(count.." Objects Removed", {1,1,1})
        memoryList = memoryListBackup
        updateSave()
end

function buttonClick_setNew()
    broadcastToAll("Setting new position relative to items in memory", {0.75, 0.75, 1})
    self.clearButtons()
    createMemoryActionButtons()
    local count = 0
    for _, obj in ipairs(getAllObjects()) do
        guid = obj.guid
        if memoryListBackup[guid] ~= nil then
            count = count + 1
            memoryListBackup[guid].pos = obj.getPosition()
            memoryListBackup[guid].rot = obj.getRotation()
            memoryListBackup[guid].lock = obj.getLock()
        end
    end
    broadcastToAll(count.." Objects Saved", {1,1,1})
    memoryList = memoryListBackup
    updateSave()
end

--Resets bag to starting status
function buttonClick_reset()
    fresh = true
    memoryList = {}
    self.clearButtons()
    createSetupButton()
    removeAllHighlights()
    broadcastToAll("Tool Reset", {1,1,1})
    updateSave()
end


--After Setup


--Creates recall and place buttons
function createMemoryActionButtons()
    self.createButton({
        label="Place", click_function="buttonClick_place", function_owner=self,
        position={0.6,0.1,2.1}, rotation={0,0,0}, height=220, width=500,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })
    self.createButton({
        label="Recall", click_function="buttonClick_recall", function_owner=self,
        position={-0.6,0.1,2.1}, rotation={0,0,0}, height=220, width=500,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })
    self.createButton({
        label="Setup", click_function="buttonClick_setup", function_owner=self,
        position={0,0.1,-2.1}, rotation={0,0,0}, height=220, width=500,
        font_size=130, color={0,0,0}, font_color={1,1,1}
    })
---    self.createButton({
---      label="Move", click_function="buttonClick_transpose", function_owner=self,
---      position={-2.8,0.3,0}, rotation={0,0,0}, height=350, width=800,
---      font_size=250, color={0,0,0}, font_color={0.75,0.75,1}
---    })
end

--Sends objects from bag/table to their saved position/rotation
function buttonClick_place()
    local bagObjList = self.getObjects()
    for guid, entry in pairs(memoryList) do
        local obj = getObjectFromGUID(guid)
        --If obj is out on the table, move it to the saved pos/rot
        if obj ~= nil then
            obj.setPositionSmooth(entry.pos)
            obj.setRotationSmooth(entry.rot)
            obj.setLock(entry.lock)
        else
            --If obj is inside of the bag
            for _, bagObj in ipairs(bagObjList) do
                if bagObj.guid == guid then
                    local item = self.takeObject({
                        guid=guid, position=entry.pos, rotation=entry.rot, smooth=false
                    })
                    item.setLock(entry.lock)
                    break
                end
            end
        end
    end
    broadcastToAll("Objects Placed", {1,1,1})
end

--Recalls objects to bag from table
function buttonClick_recall()
    for guid, entry in pairs(memoryList) do
        local obj = getObjectFromGUID(guid)
        if obj ~= nil then self.putObject(obj) end
    end
    broadcastToAll("Objects Recalled", {1,1,1})
end


--Utility functions


--Find delta (difference) between 2 x/y/z coordinates
function findOffsetDistance(p1, p2, obj)
    local yOffset = 0
    if obj ~= nil then
        local bounds = obj.getBounds()
        yOffset = (bounds.size.y - bounds.offset.y)
    end
    local deltaPos = {}
    deltaPos.x = (p2.x-p1.x)
    deltaPos.y = (p2.y-p1.y) + yOffset
    deltaPos.z = (p2.z-p1.z)
    return deltaPos
end

--Used to rotate a set of coordinates by an angle
function rotateLocalCoordinates(desiredPos, obj)
	local objPos, objRot = obj.getPosition(), obj.getRotation()
    local angle = math.rad(objRot.y)
	local x = desiredPos.x * math.cos(angle) - desiredPos.z * math.sin(angle)
	local z = desiredPos.x * math.sin(angle) + desiredPos.z * math.cos(angle)
	--return {x=objPos.x+x, y=objPos.y+desiredPos.y, z=objPos.z+z}
    return {x=x, y=desiredPos.y, z=z}
end

function rotateMyCoordinates(desiredPos, obj)
	local angle = math.rad(obj.getRotation().y)
  local x = desiredPos.x * math.sin(angle)
	local z = desiredPos.z * math.cos(angle)
    return {x=x, y=desiredPos.y, z=z}
end

--Coroutine delay, in seconds
function wait(time)
    local start = os.time()
    repeat coroutine.yield(0) until os.time() > start + time
end

--Duplicates a table (needed to prevent it making reference to the same objects)
function duplicateTable(oldTable)
    local newTable = {}
    for k, v in pairs(oldTable) do
        newTable[k] = v
    end
    return newTable
end

--Moves scripted highlight from all objects
function removeAllHighlights()
    for _, obj in ipairs(getAllObjects()) do
        obj.highlightOff()
    end
end

--Round number (num) to the Nth decimal (dec)
function round(num, dec)
  local mult = 10^(dec or 0)
  return math.floor(num * mult + 0.5) / mult
end