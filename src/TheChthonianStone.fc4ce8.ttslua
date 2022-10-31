VALID_TOKENS = {
    Skull=true,
    Cultist=true,
    Tablet=true,
    ["Elder Thing"]=true
}

function onload()
    chaosbag = getChaosBag()
    sealedTokens = { }
    IMAGE_TOKEN_MAP = { }
    for i,v in pairs(Global.getVar("IMAGE_TOKEN_MAP")) do
        IMAGE_TOKEN_MAP[i] = v
    end

    -- add menu items
    self.clearContextMenu()
    self.addContextMenuItem("Release Token", releaseTokens)
    for url,name in pairs(IMAGE_TOKEN_MAP) do
        if VALID_TOKENS[name] ~= nil then
            self.addContextMenuItem("Seal " .. name, function(playerColor) sealToken(url, playerColor) end)
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
end

function releaseTokens(playerColor)
    printToColor("Releasing token", playerColor)
    for i,obj in ipairs(sealedTokens) do
        chaosbag.putObject(obj)
    end
    sealedTokens = { }
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