function onload()
    chaosbag = getChaosBag()
    IMAGE_TOKEN_MAP = { }
    for i,v in pairs(Global.getVar("IMAGE_TOKEN_MAP")) do
        IMAGE_TOKEN_MAP[i] = v
    end

    -- add menu items
    self.clearContextMenu()
    for url,name in pairs(IMAGE_TOKEN_MAP) do
        if name == "0" then
            self.addContextMenuItem("Seal 0", function(playerColor) sealToken(url, playerColor) end)
        end
    end
end

function sealToken(url, playerColor)
    local pos = self.getPosition()

    local name = IMAGE_TOKEN_MAP[url]
    for i,obj in ipairs(chaosbag.getObjects()) do
        if obj.name == name then
            chaosbag.takeObject({
                position={ pos.x, pos.y + 1, pos.z },
                index=i-1,
                smooth=false
            })
            return
        end
    end
    printToColor(name .. " token not found in bag", playerColor)
end

function getChaosBag()
    local items = getObjectFromGUID("83ef06").getObjects()
    local chaosbag = nil
    for i,v in ipairs(items) do
        if v.getDescription() == "Chaos Bag" then
            chaosbag = getObjectFromGUID(v.getGUID())
            break
        end
    end
    if chaosbag == nil then printToAll("No chaos bag found") end
    return chaosbag
end