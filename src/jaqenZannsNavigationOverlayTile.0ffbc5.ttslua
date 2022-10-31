-- SCE Navigation Panel version 1.00

function onLoad(saved_data)
    self.createButton({
        label="",
        tooltip="Display full overlay",
        click_function="displayFull",
        function_owner=self,
        position={0.0,0.1,-0.57},
        height=70,
        width=800,
        scale={x=1, y=1, z=1},
        color={1,0,0,0}
    })
    self.createButton({
        label="",
        tooltip="Display only play area",
        click_function="displayPlayArea",
        function_owner=self,
        position={0.0,0.1,-0.30},
        height=70,
        width=800,
        scale={x=1, y=1, z=1},
        color={1,0,0,0}
    })
    self.createButton({
        label="",
        tooltip="Close overlay",
        click_function="closeOverlay",
        function_owner=self,
        position={0.0,0.1,-0.03},
        height=70,
        width=800,
        scale={x=1, y=1, z=1},
        color={1,0,0,0}
    })
    self.createButton({
        label="",
        tooltip="Modify a camera position",
        click_function="beginSetCamera",
        function_owner=self,
        position={0.0,0.1,0.37},
        height=70,
        width=800,
        scale={x=1, y=1, z=1},
        color={1,0,0,0}
    })
    self.createButton({
        label="",
        tooltip="Reset camera positions to default",
        click_function="resetCameras",
        function_owner=self,
        position={0.0,0.1,0.77},
        height=70,
        width=800,
        scale={x=1, y=1, z=1},
        color={1,0,0,0}
    })

    defaultCameraParams = {
        {position={-1.626, -2.5, -0.064},   pitch=62.964, yaw=90.000,  distance=17.844},   --  1. ActAgenda
        {position={-27.822, -2.5, 0.424},   pitch=75.823, yaw=90.000,  distance=-1.000},   --  2. Map
--        {position={-31.592, -2.5, 26.392},  pitch=74.238, yaw=180.000, distance=19.858},   --  3. Green playmat
        {position={-31.592, -2.5, 26.392},  pitch=74.238, yaw=180.000, distance=-1.000},   --  3. Green playmat
        {position={-55.026, -2.5, 12.052},  pitch=74.238, yaw=90.000,  distance=-1.000},   --  4. White playmat
        {position={-55.026, -2.5, -11.479}, pitch=74.238, yaw=90.000,  distance=-1.000},   --  5. Orange playmat
        {position={-31.592, -2.5, -26.392}, pitch=74.238, yaw=0.000,   distance=-1.000},   --  6. Red playmat
        {position={-2.940, -2.5, 25.160},   pitch=73.556, yaw=90.000,  distance=20.146},   --  7. Victory / SetAside
        {position={-58.216, -2.5, -71.288}, pitch=76.430, yaw=90.000,  distance=20.000},   --  8. Deckbuilder
        {position={46.368, -2.5, 0.328},    pitch=69.491, yaw=90.000,  distance=46.255},   --  9. Campaigns
        {position={13.875, -2.5, 0.328},    pitch=69.491, yaw=90.000,  distance=37.962},   -- 10. Scenarios
        {position={51.940, -2.5, 64.476},   pitch=76.430, yaw=90.000,  distance=48.102},   -- 11. Level 0
        {position={51.302, -2.5, -73.514},  pitch=76.430, yaw=90.000,  distance=48.102},   -- 12. Upgraded
        {position={-27.788, -2.5, 74.662},  pitch=76.430, yaw=90.000,  distance=30.616},   -- 13. Weaknesses
        {position={-61.090, -2.5, 70.762},  pitch=76.430, yaw=90.000,  distance=34.188},   -- 14. Rules
        {position={-18.547, -2.5, -73.514}, pitch=76.430, yaw=90.000,  distance=42.249},   -- 15. Investigators
        {position={-2.144, -2.5, -26.900},  pitch=73.556, yaw=90.000,  distance=20.146},   -- 16. Log
        {position={-45.000, -2.5, -0.228},  pitch=73.556, yaw=90.000,  distance=12.000}    -- 17. BlessCurse
    }

    fullButtonData = {
        { id = "1", width = "84", height = "38", offsetX = "1", offsetY = "-9" },
        { id = "2", width = "78", height = "50", offsetX = "1", offsetY = "-59" },
        { id = "3", width = "36", height = "70", offsetX = "-62", offsetY = "-70" },
        { id = "4", width = "70", height = "40", offsetX = "-36", offsetY = "-130" },
        { id = "5", width = "70", height = "40", offsetX = "39", offsetY = "-130" },
        { id = "6", width = "36", height = "70", offsetX = "64", offsetY = "-70" },
        { id = "7",  width = "36", height = "36", offsetX = "-63", offsetY = "-9" },
        { id = "8", width = "64", height = "64", offsetX = "153", offsetY = "-128" },
        { id = "9", width = "155", height = "70", offsetX = "2", offsetY = "120" },
        { id = "10", width = "155", height = 70, offsetX = "2", offsetY = "47" },
        { id = "11", width = "120", height = "100", offsetX = "-148", offsetY = "101" },
        { id = "12", width = "120", height = "100", offsetX = "150", offsetY = "101" },
        { id = "13", width = "120", height = "80", offsetX = "-150", offsetY = "-55" },
        { id = "14", width = "120", height = "60", offsetX = "-150", offsetY = "-132" },
        { id = "15", width = "110", height = "100", offsetX = "152", offsetY = "-42" },
        { id = "16", width = "36", height = "36", offsetX = "64", offsetY = "-9" },
        { id = "17", width = "44", height = "25", offsetX = "1", offsetY = "-97" }
    }

    playButtonData = {
        { id = "1", width = "84", height = "38", offsetX = "0", offsetY = "59" },
        { id = "2", width = "78", height = "50", offsetX = "0", offsetY = "9" },
        { id = "3", width = "36", height = "70", offsetX = "-62", offsetY = "-1" },
        { id = "4", width = "70", height = "40", offsetX = "-37", offsetY = "-61" },
        { id = "5", width = "70", height = "40", offsetX = "39", offsetY = "-61" },
        { id = "6", width = "36", height = "70", offsetX = "63", offsetY = "-2" },
        { id = "7",  width = "36", height = "36", offsetX = "-64", offsetY = "59" },
        { id = "16", width = "36", height = "36", offsetX = "63", offsetY = "59" },
        { id = "17", width = "44", height = "25", offsetX = "0", offsetY = "-28" }
    }

    playermatData = {
        White = { guid = '8b081b', origin = { x=-54.42, y=0, z=20.96 }, scale = { x=36.63, y=5.10, z=14.59 }, orientation = { x=0, y=270, z=0 }, minX = -61.4, maxX = -48.6, minZ = -2.39, maxZ = 24.53, xOffset = 0.07, zOffset = 0.03 },
        Orange = { guid = 'bd0ff4', origin = { x=-54.42, y=0, z=-20.96 }, scale = { x=36.63, y=5.10, z=14.59 }, orientation = { x=0, y=270, z=0 }, minX = -61.4, maxX = -48.6, minZ = -24.53, maxZ = 2.39, xOffset = 0.07, zOffset = 0.02 },
        Green = { guid = '383d8b', origin = { x=-25.00, y=0, z=26.20 }, scale = { x=31.5, y=5.10, z=14.59 }, orientation = { x=0, y=0, z=0 }, minX = -44.43, maxX = -17.44, minZ = 20.17, maxZ = 32.97, xOffset = -0.07, zOffset = 0.00 },
        Red = { guid = '0840d5', origin = { x=-25.00, y=0, z=-26.60 }, scale = { x=31.5, y=5.10, z=14.59 }, orientation = { x=0, y=180, z=0 }, minX = -44.43, maxX = -17.44, minZ = -32.97, maxZ = -20.17, xOffset = 0.07, zOffset = -0.06 }
    }

    editing = false
    selectedEditButton = -1

    editPos = {0, 0, 0}
    editPitch = 0
    editYaw = 0
    editDistance = 0

    if saved_data ~= "" then
        local loaded_data = JSON.decode(saved_data)

        cameraParams = loaded_data.cameras
        fullVisibility = loaded_data.fullVis
        playVisibility = loaded_data.playVis

        resetOverlay()
    else
        cameraParams = {
            Green = {},
            White = {},
            Orange = {},
            Red = {}
        }

        for iv, v in pairs({'Green', 'White', 'Orange', 'Red'}) do
            cameraParams[v] = {}

            for i = 1,17 do
                cameraParams[v][i] = {}

                cameraParams[v][i].position = defaultCameraParams[i].position
                cameraParams[v][i].pitch = defaultCameraParams[i].pitch
                cameraParams[v][i].yaw = defaultCameraParams[i].yaw
                cameraParams[v][i].distance = defaultCameraParams[i].distance
            end
        end

        fullVisibility = {
            Green = false,
            White = false,
            Orange = false,
            Red = false
        }

        playVisibility = {
            Green = false,
            White = false,
            Orange = false,
            Red = false
        }
    end
end

function onSave()
    return JSON.encode({
        cameras = cameraParams,
        fullVis = fullVisibility,
        playVis = playVisibility
    })

--    return ''
end

function displayFull(object, color)
    local playerCount = getPlayerCount()
    local colors
    if playerCount == 1 then
        colors = { 'Green', 'White', 'Orange', 'Red' }
    else
        colors = { color }
    end

    for i, v in ipairs(colors) do
        fullVisibility[v] = true
        playVisibility[v] = false
    end

    resetOverlay()
end

function displayPlayArea(object, color)
    local playerCount = getPlayerCount()
    local colors
    if playerCount == 1 then
        colors = { 'Green', 'White', 'Orange', 'Red' }
    else
        colors = { color }
    end

    for i, v in ipairs(colors) do
        fullVisibility[v] = false
        playVisibility[v] = true
    end

    resetOverlay()
end

function resetCameras(object, color)
    local playerCount = getPlayerCount()
    local colors

    if playerCount == 1 then
        colors = { 'Green', 'White', 'Orange', 'Red' }
    else
        colors = { color }
    end

    for iv, v in ipairs(colors) do
        for i = 1,17 do
            cameraParams[v][i].position = defaultCameraParams[i].position
            cameraParams[v][i].pitch = defaultCameraParams[i].pitch
            cameraParams[v][i].yaw = defaultCameraParams[i].yaw
            cameraParams[v][i].distance = defaultCameraParams[i].distance
        end
    end
end

function closeOverlay(object, color)
    fullVisibility[color] = false
    playVisibility[color] = false

    resetOverlay()
end

function resetOverlay()
    local guid = self.getGUID()
    local color
    local panel

    local existingXml = UI.getXml()
    local openingXml = ''

    -- try to only remove our panels
    for p = 1,2 do
        i, j = string.find(existingXml, '<Panel id="navPanel')

        if i and i > 1 and string.len(openingXml) == 0 then
            openingXml = string.sub(existingXml, 1, i-1)
        end

        if i then
            local panelXml = string.sub(existingXml, i)
            k, m = string.find(panelXml, '</Panel>')

            existingXml = string.sub(panelXml, m+1)
        else
            break
        end
    end

    local xml = openingXml .. [[
    ]] .. existingXml

    local fullColors = ''
    local playColors = ''

    for i, v in pairs(fullVisibility) do
        if v == true then
            if string.len(fullColors) > 0 then
                fullColors = fullColors .. '|' .. i
            else
                fullColors = i
            end
        end
    end

    for i, v in pairs(playVisibility) do
        if v == true then
            if string.len(playColors) > 0 then
                playColors = playColors .. '|' .. i
            else
                playColors = i
            end
        end
    end

    if string.len(fullColors) > 0 then
        data = fullButtonData

        xml = xml .. [[<Panel id="navPanelFull" height="358" width="455" visibility="]] .. fullColors .. [[" allowDragging="true" returnToOriginalPositionWhenReleased="false" rectAlignment="LowerRight" offsetXY="-40 0">
            <image id="backgroundImage" image="OverlayLarge" />]]

        for i, d in ipairs(data) do
            if editing then
                if selectedEditButton < 0 then
                    color = "rgba(1,1,1,1)"
                elseif tonumber(d.id) == selectedEditButton then
                    color = "rgba(0,1,0,1)"
                else
                    color = "rgba(1,0,0,1)"
                end
            else
                color = "rgba(0,1,0,0)"
            end

            xml = xml .. [[<button
                onClick="]] .. guid .. [[/buttonClicked"
                id="]] .. d.id .. [["
                height="]] .. d.height .. [["
                width="]] .. d.width .. [["
                offsetXY="]] .. d.offsetX .. " " .. d.offsetY .. [["
                color="]] .. color .. [["
            >
            </button>
            ]]
        end

        xml = xml .. [[    </Panel>]]
    end

    if string.len(playColors) > 0 then
        data = playButtonData

        xml = xml .. [[
        <Panel id="navPanelPlay" height="208" width="205" visibility="]] .. playColors .. [[" allowDragging="true" returnToOriginalPositionWhenReleased="false" rectAlignment="LowerRight" offsetXY="-40 0">
            <image id="backgroundImage" image="OverlaySmall" />]]

        for i, d in ipairs(data) do
            if editing then
                if selectedEditButton < 0 then
                    color = "rgba(1,1,1,1)"
                elseif tonumber(d.id) == selectedEditButton then
                    color = "rgba(0,1,0,1)"
                else
                    color = "rgba(1,0,0,1)"
                end
            else
                color = "rgba(0,1,0,0)"
            end

            xml = xml .. [[<button
                onClick="]] .. guid .. [[/buttonClicked"
                id="]] .. d.id .. [["
                height="]] .. d.height .. [["
                width="]] .. d.width .. [["
                offsetXY="]] .. d.offsetX .. " " .. d.offsetY .. [["
                color="]] .. color .. [["
            >
            </button>
            ]]
        end

        xml = xml .. [[    </Panel>]]
    end

    local existingAssets = UI.getCustomAssets()
    local largeOverlay = nil
    local smallOverlay = nil

    for i,v in pairs(existingAssets) do
        for ii,vv in pairs(v) do
            if vv == 'OverlayLarge' then
                largeOverlay = v
            end
            if vv == 'OverlaySmall' then
                smallOverlay = v
            end
        end
    end

    local largeURL = 'http://cloud-3.steamusercontent.com/ugc/1745699502804112656/A34D1F30E0DA0E283F300AE6D6B63F59FFC97730/'
    local smallURL = 'http://cloud-3.steamusercontent.com/ugc/1745699502804112719/CFFC89BF9FB8439204EE19CF94180EC99450CD38/'

    if largeOverlay == nil then
        largeOverlay = { name='OverlayLarge', url=largeURL }
        table.insert(existingAssets, largeOverlay)
    else
        largeOverlay.url = largeURL

    end

    if smallOverlay == nil then
        smallOverlay = { name='OverlaySmall', url=smallURL }
        table.insert(existingAssets, smallOverlay)
    else
        smallOverlay.url = smallURL
    end

    UI.setXml(xml, existingAssets)
end

function buttonClicked(player, _, idValue)
    if editing then
        if selectedEditButton < 0 then
            selectedEditButton = tonumber(idValue)
        else
            if tonumber(idValue) == selectedEditButton and editDistance > 0 then
                local playerCount = getPlayerCount()
                local colors

                if playerCount == 1 then
                    colors = { 'Green', 'White', 'Orange', 'Red' }
                else
                    colors = { player.color }
                end

                for i, v in ipairs(colors) do
                    cameraParams[v][selectedEditButton].position = editPos
                    cameraParams[v][selectedEditButton].pitch = editPitch
                    cameraParams[v][selectedEditButton].yaw = editYaw
                    cameraParams[v][selectedEditButton].distance = editDistance
                end
            end

            editing = false
            selectedEditButton = -1
        end

        resetOverlay()
    else
        loadCamera(player, _, idValue)
    end
end

function loadCamera(player, _, idValue)
    local index = tonumber(idValue)
    local color = player.color

    -- only do map zooming if te camera hasn't been specially set by user
    if index == 2 and cameraParams[color][index].distance <= 0.0 then
        local mapObjects = Physics.cast({
            origin = { x=-29.2, y=0, z=0.0 },
            direction = { x=0, y=1, z=0 },
            type = 3,
            size = { x=36, y=5, z=31.4 },
            orientation = { x=0, y=90, z=0 }
        })

        local minX = 100
        local maxX = -100
        local minZ = 100
        local maxZ = -100

        for i,v in pairs(mapObjects) do
            local obj = v.hit_object

            if obj.type == 'Card' or obj.type == 'Infinite' then
                local bounds = obj.getBounds()

                local x1 = bounds['center'][1] - bounds['size'][1]/2
                local x2 = bounds['center'][1] + bounds['size'][1]/2
                local z1 = bounds['center'][3] - bounds['size'][3]/2
                local z2 = bounds['center'][3] + bounds['size'][3]/2

                if x1 < minX then
                    minX = x1
                end
                if x2 > maxX then
                    maxX = x2
                end
                if z1 < minZ then
                    minZ = z1
                end
                if z2 > maxZ then
                    maxZ = z2
                end
            end
        end

        if minX < 100 then
            local dx = maxX - minX
            local dz = (maxZ - minZ) / (1.6)  -- screen ratio * 1.2 (for my macbook pro, no idea how to generalize this)
            local centerX = (minX + maxX) / 2 - dx*0.12   -- offset is to move it a bit up, so the cards don't block anything
            local centerZ = (minZ + maxZ) / 2

            local scale = dx
            if dz > dx then
                scale = dz
            end

            -- regression line from the following data points, seems linear
            -- rows 1 scale 4.5   d 12
            -- rows 2 scale 11    d 16
            -- rows 3 scale 14.5  d 19.6
            -- rows 4 scale 19.6  d 25
            -- rows 5 scale 23.25 d 28
            -- rows 6 scale 30.8  d 34

            -- local d = 0.8685 * scale + 7.4505

            -- modified by testing
    --        local d = 0.8685 * scale + 5
            local d = 1.04 * scale + 5

            player.lookAt({position={centerX, 0, centerZ}, pitch=75.823, yaw=90.000,  distance=d})
        else
            player.lookAt({position={-33.667, 0, 0.014}, pitch=75.823, yaw=90.000,  distance=36})
        end
    elseif index >= 3 and index <= 6 then
        local matColor = nil

        if index == 3 then
            matColor = 'Green'
        elseif index == 4 then
            matColor = 'White'
        elseif index == 5 then
            matColor = 'Orange'
        elseif index == 6 then
            matColor = 'Red'
        end

        if matColor ~= nil then
            local playerCount = getPlayerCount()

            if playerCount <= 1 then
                player.changeColor(matColor)
            end
        end

        if cameraParams[color][index].distance <= 0.0 then
            local matObjects = Physics.cast({
                origin = playermatData[matColor].origin,
                direction = { x=0, y=1, z=0 },
                type = 3,
                size = playermatData[matColor].scale,
                orientation = playermatData[matColor].orientation,
--                debug=true
            })

            local minX = playermatData[matColor].minX
            local maxX = playermatData[matColor].maxX
            local minZ = playermatData[matColor].minZ
            local maxZ = playermatData[matColor].maxZ

            for i,v in pairs(matObjects) do
                local obj = v.hit_object

                if obj.type == 'Card' or obj.type == 'Infinite' then
                    local bounds = obj.getBounds()

                    local x1 = bounds['center'][1] - bounds['size'][1]/2
                    local x2 = bounds['center'][1] + bounds['size'][1]/2
                    local z1 = bounds['center'][3] - bounds['size'][3]/2
                    local z2 = bounds['center'][3] + bounds['size'][3]/2

                    if x1 < minX then
                        minX = x1
                    end
                    if x2 > maxX then
                        maxX = x2
                    end
                    if z1 < minZ then
                        minZ = z1
                    end
                    if z2 > maxZ then
                        maxZ = z2
                    end
                end
            end

            local dx
            local dz
            local centerX
            local centerZ
            local scale
            local yaw
            local d

            -- White/Orange
            if index > 3 and index < 6 then
                dx = maxX - minX
                dz = (maxZ - minZ) / (1.6)  -- screen ratio * 1.2 (for my macbook pro, no idea how to generalize this)

                centerX = (minX + maxX) / 2 - dx*playermatData[matColor].xOffset   -- offset is to move it a bit up, so the cards don't block anything
                centerZ = (minZ + maxZ) / 2 + dz*playermatData[matColor].zOffset   -- offset is to move it right a bit, so the toolbar doesn't block anything
                yaw = 90

                scale = dx
                if dz > dx then
                    scale = dz
                end

                d = 0.64 * scale + 7
            else    -- Green/Red
                dx = (maxX - minX) / (1.6)  -- screen ratio * 1.2 (for my macbook pro, no idea how to generalize this)
                dz = maxZ - minZ

                centerX = (minX + maxX) / 2 + dx*playermatData[matColor].zOffset   -- offset is to move it right a bit, so the toolbar doesn't block anything
                centerZ = (minZ + maxZ) / 2 - dz*playermatData[matColor].xOffset   -- offset is to move it a bit up, so the cards don't block anything
                yaw = playermatData[matColor].orientation.y + 180

                scale = dz
                if dx > dz then
                    scale = dx
                end

                d = 0.64 * scale + 7
            end

            -- 15.46 -> 17.081
            -- 18.88 -> 19.33
            -- 24.34 -> 22.6

            -- need to wait if the player color changed
            Wait.frames(function() player.lookAt({position={centerX, 0, centerZ}, pitch=75.823, yaw=yaw,  distance=d}) end, 2)
        else
            Wait.frames(function() player.lookAt(cameraParams[color][index]) end, 2)
        end
    else
        player.lookAt(cameraParams[color][index])
    end
end

function beginSetCamera(object, color)
    editing = true

    resetOverlay()
end

function updateEditCamera(params)
    editPos = params[1]
    editPitch = params[2]
    editYaw = params[3]
    editDistance = params[4]
end

function getPlayerCount()
    local playerCount = 0

    local playerList = getSeatedPlayers()

    for i, v in ipairs(playerList) do
        if v == 'Green' or v == 'White' or v == 'Orange' or v == 'Red' then
            playerCount = playerCount + 1
        end
    end

    return playerCount
end
