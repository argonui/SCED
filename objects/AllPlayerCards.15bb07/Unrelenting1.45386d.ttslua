ASSEMBLY_POSITION = {69.08, 4, 36.45}

function onload()
    chaosbag = getChaosBag()
    manager = getObjectFromGUID("5933fb")
    sealedTokens = { }
    IMAGE_TOKEN_MAP = { }
    for i,v in pairs(Global.getVar("IMAGE_TOKEN_MAP")) do
        IMAGE_TOKEN_MAP[i] = v
    end

    readBag()
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
    local name = obj.getName()
    if name == "Bless" or name == "Curse" then
        local tokensTaken = manager.getVar("tokensTaken")
        table.insert(tokensTaken[name], guid)
        manager.setVar("tokensTaken", tokensTaken)
        manager.setVar("mode", name)
        printToAll("Sealing " .. name .. " token " .. manager.call("getTokenCount"))
    end
end

function releaseTokens(playerColor)
    if #sealedTokens == 0 then return end
    for i,token in ipairs(sealedTokens) do
        local guid = token.getGUID()
        local name = token.getName()
        chaosbag.putObject(token)
        if name == "Bless" or name == "Curse" then
            local tokensTaken = manager.getVar("tokensTaken")
            for i,v in ipairs(tokensTaken[name]) do
                if v == guid then
                    table.remove(tokensTaken[name], i)
                    break
                end
            end
            manager.setVar("tokensTaken", tokensTaken)
            manager.setVar("mode", name)
            printToAll("Releasing " .. name .. " token" .. manager.call("getTokenCount"))
        end
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

function readBag()
    -- add menu items
    self.clearContextMenu()
    self.addContextMenuItem("Release Tokens", releaseTokens)

    local bagTokens = { }
    local tokens = chaosbag.getObjects()
    for i,token in ipairs(tokens) do
        bagTokens[token.name] = true
    end

    for url,token in pairs(IMAGE_TOKEN_MAP) do
        if bagTokens[token] then
            self.addContextMenuItem("Seal " .. token, function(playerColor) sealToken(url, playerColor) end, true)
        end
    end
    self.addContextMenuItem("Refresh Seal Options", readBag)
end
