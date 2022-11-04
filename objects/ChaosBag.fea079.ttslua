function filterObjectEnter(obj)
    local props = obj.getCustomObject()
    if props ~= nil and props.image ~= nil then
        obj.setName(Global.call("getTokenName", { url=props.image }))
    end
    return true
end

function onCollisionEnter(collision_info)
    self.shuffle()
    self.shuffle()
    self.shuffle()
end