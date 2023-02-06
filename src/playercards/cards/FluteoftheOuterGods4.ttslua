function onload()
    mode = "Curse"
    chaosbag = getChaosBag()
    manager = getObjectFromGUID("5933fb")
    sealedTokens = { }
    IMAGE_TOKEN_MAP = { }
    for i,v in pairs(Global.getVar("IMAGE_TOKEN_MAP")) do
        IMAGE_TOKEN_MAP[i] = v
    end

    -- add menu items
    self.clearContextMenu()
    self.addContextMenuItem("Release Token", releaseTokens, true)
    for url,name in pairs(IMAGE_TOKEN_MAP) do
        if name == mode then
            self.addContextMenuItem("Seal " .. mode, function(playerColor) sealToken(url, playerColor) end, true)
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
                smooth=false,
                callback_function=_sealToken
            })
            return
        end
    end
    printToColor(name .. " token not found in bag", playerColor)
end

function _sealToken(obj)
    table.insert(sealedTokens, obj)
    local guid = obj.getGUID()
    local tokensTaken = manager.getVar("tokensTaken")
    table.insert(tokensTaken[mode], guid)
    manager.setVar("tokensTaken", tokensTaken)
    manager.setVar("mode", mode)
    printToAll("Sealing " .. mode .. " token " .. manager.call("getTokenCount"))
end

function releaseTokens(playerColor)
    if #sealedTokens == 0 then return end
    local token = sealedTokens[#sealedTokens]
    if token ~= nil then
        local guid = token.getGUID()
        chaosbag.putObject(token)
        local tokensTaken = manager.getVar("tokensTaken")
        for i,v in ipairs(tokensTaken[mode]) do
            if v == guid then
                table.remove(tokensTaken[mode], i)
                break
            end
        end
        manager.setVar("tokensTaken", tokensTaken)
        manager.setVar("mode", mode)
        printToAll("Releasing " .. mode .. " token" .. manager.call("getTokenCount"))
    end

    table.remove(sealedTokens)
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
